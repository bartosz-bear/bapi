import pandas as pd
import numpy as np

from datetime import date, timedelta

import os

def transform_finance():

  # Read Data
  cwd = os.getcwd() + '/bapi_django_app/scripts/'

  clients = pd.read_csv(cwd + 'clients.csv')
  transfers = pd.read_csv(cwd + 'transfers.csv')
  counties = pd.read_csv(cwd + 'counties.csv')

  # Checks Container
  checks = []

  ## Data Clean-Up

  ### clients CLEAN-UP

  #### CHECK IF ALL IDS IN `CLIENT_ID` ARE UNIQUE
  checks.append({'check': 'CHECK IF ALL IDS IN `CLIENT_ID` ARE UNIQUE', 'results': clients['CLIENT_ID'].is_unique})

  #### CHECK IF ANY CLIENT HAS MORE THAN ONE ACCOUNT AND IF ANY ACCOUNT BELONGS TO MORE THAN ONE PERSON
  client_customer_id = clients['CLIENT_ID'].astype(str) + '-' + clients['ACCOUNT_ID'].astype(str)
  checks.append({'check': 'CHECK IF ANY CLIENT HAS MORE THAN ONE ACCOUNT AND IF ANY ACCOUNT BELONGS TO MORE THAN ONE PERSON', 'results': client_customer_id.is_unique})

  #### CHECK IF ALL VALUES IN `GENDER` COLUMNS ARE EITHER 'F' OR 'M'
  checks.append({'check': "CHECK IF ALL VALUES IN `GENDER` COLUMNS ARE EITHER 'F' OR 'M'", 'results': clients.groupby('GENDER').count().axes[0].values.tolist() == ['F', 'M']})

  #### CONVERT DATE TO PANDAS' `DATETIME` FORMAT
  clients['datetime'] = pd.to_datetime(clients['BIRTH_DT'], format="%Y%m%d")
  clients['datetime'].head()

  ### CHECK IF 'BIRTH_DT' IS IN PANDAS' 'DATETIME' FORMAT
  checks.append({'check': "CHECK IF 'BIRTH_DT' IS IN PANDAS' 'DATETIME' FORMAT", 'results': clients['datetime'].dtype == np.dtype('<M8[ns]')})

  #### CHECK FOR BIRTHDATE OUTLIERS
  clients['today'] = pd.to_datetime(date.today().strftime('%Y%m%d'), format="%Y%m%d")
  clients['age'] = (clients['today'] - clients['datetime']) / timedelta(days=365)
  clients['age'] = np.floor(clients['age']).astype('int')
  checks.append({'check': "CHECK FOR BIRTHDATE OUTLIERS", 'results': (clients['age'].max() < 120) & (clients['age'].min() >= 18)})

  #### CHECK IF ALL VALUES IN `SET_SPLIT` COLUMN ARE EITHER `TEST` OR `TRAIN`
  checks.append({'check': "CHECK IF ALL VALUES IN `SET_SPLIT` COLUMN ARE EITHER `TEST` OR `TRAIN`", 'results': clients.groupby('SET_SPLIT').count().axes[0].values.tolist() == ['TEST', 'TRAIN']})

  #### CONVERT 'NaN's TO ZEROS
  '''Quick glance at the 'NaN' records suggests that these records represent legit accounts. Distribution betwen genders, district ID and enough randomness in date of birth indicate that these
     records are valid but miss the `LOAN` information. Most of the birth dates for the clients with 'Nan' value are seniors (born before 1960). I will assume that these people became clients
     before loan product was offered by the bank. We don't need this distinction for our analysis, and since they are marked as '1' in `ACTIVE` column, I will assume that they are active clients
     without an active loan. Therefore I will convert all 'NaN's to zero. Another hypothesis why certain records hold 'NaN' value is that data can come from a SQL database. In SQL 'Nan' values
     can be represented as 'Null'. 'Null' indicates state of 'unknown'. In our case, it would mean that we don't know if a customer has a loan or he hasn't. Since we can't be sure, we CAN'T mark
     it as zero (no loan). However, this situation seems extremely unlikely because we are dealing with bank data and assuming that a bank isn't aware of it's own loans is extremely unlikely.
     Therefore I will reject this hypothesis and update 'NaN' values to zeros.
  '''
  
  #### CHECK FOR `NULLS` IN THE `LOAN` COLUMN 
  clients['LOAN'] = clients['LOAN'].fillna(0)
  checks.append({'check': "CHECK FOR `NULLS` IN THE `LOAN` COLUMN", 'results': not clients['LOAN'].hasnans})

  #### CONVERT `LOAN` DATA TYPE FROM 'FLOAT' TO 'INT'
  clients['LOAN'] = clients['LOAN'].astype('int')

  #### CHECK IF 'LOAN' COLUMN IS OF TYPE 'INT'
  checks.append({'check': "CHECK IF 'LOAN' COLUMN IS OF TYPE 'INT'", 'results': clients['LOAN'].dtype == np.int32})

  #### REMOVE UNNEEDED COLUMNS
  #clients.drop(['BIRTH_DT', 'today', 'datetime'], axis=1, inplace=True)

  #### SUMMARY - `clients` TABLE AFTER CLEAN-UP
  ### 'transfers' TABLE CLEAN-UP

  #### CHECK IF `TRANSFER_ID` VALUES ARE UNIQUE
  transfers['TRANSFER_ID'].is_unique

  #### INVESTIGATE DUPLICATES
  transfers['TRANSFER_ID'].duplicated().groupby(transfers['TRANSFER_ID'].duplicated()).count()
  transfers[transfers.duplicated(keep=False)]

  '''There are close to 5000 duplicate values. There should be no duplicate transfers in the table as each each `TRANSFER_ID` should be unique. I will remove the duplicates as the number
     of duplicates is very low (less than half percent of all transfers) and it seems like duplicates were added by mistake as previously mentioned.
  '''

  #### REMOVE DUPLICATES
  transfers.drop_duplicates('TRANSFER_ID', inplace=True)
  transfers['TRANSFER_ID'].is_unique
  checks.append({'check': "CHECK IF `TRANSFER_ID` VALUES ARE UNIQUE", 'results': transfers['TRANSFER_ID'].is_unique})

  #### CHECK FOR MISSING VALUES IN ACCOUNT_ID
  transfers.isna().sum()

  '''There are 5000 missing values in the `ACCOUNT_ID` column which is less than half percent of all transfers. The 'misising values' sample is homogenous as shown by the 'summary-describe()'
     tables. Ratios of "transfers in a particular category (eg. 'CC_WITHDRAWAL')" vs "total transfers" are very similar in both the sample and total population set. `ACCOUNT_ID` missing value
     can be a problem for certain types of future operations (eg. joins over tables) because database consistency is not maintained.
  '''

  #HOMOGENEITY CHECK
  only_nulls = transfers.loc[transfers['ACCOUNT_ID'].isnull()]
  full_set_without_nulls = transfers.dropna(subset='ACCOUNT_ID')

  def homogeneity_check(dataset):
      
      grouped_set = dataset.groupby('OPERATION').count()
      grouped_set['ratio'] = grouped_set['TRANSFER_ID'] / dataset['TRANSFER_ID'].count()
      grouped_set['ratio'] = grouped_set['ratio'].map('{:.1%}'.format)
      
      return grouped_set[['ratio']].values.tolist()


  only_nulls_summary = homogeneity_check(only_nulls)
  full_set_without_nulls_summary = homogeneity_check(full_set_without_nulls)

  '''We can see that the ratio values for each `OPERATION` category (eg. 'CREDIT_IN_CASH', 'COLLECTION_FROM_BANK', etc) are very similar in both sets. Therefore the sample set is homogenous
     with the population set. This gives us confidence to remove the 'NaN' values without a high risk of negatively influencing the results of further analysis.
  '''

  transfers.dropna(subset='ACCOUNT_ID', inplace=True)
  transfers.isna().sum()

  #### CHECK IF A COMBINATION OF TRANSACTION ID AND ACCOUNT IS UNIQUE
  transfers_account_id = transfers['TRANSFER_ID'].astype(str) + '-' + transfers['ACCOUNT_ID'].astype(str)
  transfers_account_id.is_unique
  checks.append({'check': "CHECK IF A COMBINATION OF TRANSACTION ID AND ACCOUNT IS UNIQUE", 'results': transfers_account_id.is_unique})


  #### CHECK IF THERE ARE ANY 'NaN' VALUES IN ANY OTHER COLUMN
  transfers.isna().sum()
  "{:.0%}".format(transfers.isna().sum()['OPERATION'] / len(transfers.index))

  '''There are 180k missing transfers with missing 'OPERATION' value which is 17% of total transfers. My hypothesis is that these belong to the sixth 'OPERATION' category. Most likely the
     missing category is 'CREDIT_TO_CC'. The rationale behind this hypothesis is that there are three types of transfers (Credit Card related, Cash related and Bank Transfer related).
     For the two of these categories: Cash and Bank Transfer, we can see both credit and debit type. However, for Credit Card category we can only see credit type. Therefore, most likely
     the missing values belong to Credit part of Credit Card category.
  '''
     
  transfers.groupby('OPERATION', dropna=False).count()

  '''Another clue which led me to my hypothesis was mean transation amount accross different 'OPERATION' categories. Credit card transfers are generally of lower value than bank transfers and
     cash withdrawals/deposits in the bank. Summary statistics of the dataset confirm this: 'CC_WITHDRAVAL' category has the lowest value mean among the categories. And the data set which consists
     of 'NaN' values has the lowest mean among all categories. Which is another reason to believe that this dataset is really 'CREDIT_TO_CC' category.
  '''

  transfers.groupby('OPERATION', dropna=False).mean(numeric_only=True)['AMOUNT'].astype('int').sort_values(ascending=False)

  #Based on the reasons described above I'm going to replace 'Nan's with 'CREDIT_TO_CC' tag.
  transfers['OPERATION'] = transfers['OPERATION'].map(lambda x: 'CC_CREDIT' if pd.isna(x) else x)
  transfers.isna().sum()
  checks.append({'check': "CHECK IF THERE ARE ANY 'NaN' VALUES IN ANY OTHER COLUMN", 'results': transfers.isna().sum().sum() == 0})

  #### CHECK IF THERE ARE ANY transfers WITH ZERO VALUE
  len(transfers[transfers['AMOUNT'] == 0].index)
  transfers[transfers['AMOUNT'] == 0]

  '''There are 14 transfers with 'zero' amount. Since they have no impact on the aggregate statistics of the remaining transfers, I'm going to remove them from the dataset. However, I will keep
     them as a separate table to investigate the reason for transfers with zero amount. They are probably some kind of systems' related transfers as all of them take place at the last day of th
     calendar month.
  '''
     
  count_before = len(transfers.index)
  transfers.drop(transfers[transfers.AMOUNT == 0].index, inplace=True)
  (count_before - len(transfers.index)) == 14

  #### CHECK TYPE COLUMN
  transfers.groupby('TYPE').groups.keys()

  '''These two categories represent account inflows and outflows, therefore there is no need for signed transfers. I expect to see no negative amount records in the next check.
  '''

  #### CHECK IF THERE ARE ANY transfers WHERE 'AMOUNT' IS LOWER THAN 0
  len(transfers[transfers['AMOUNT'] < 0].index) == 0
  checks.append({'check': "CHECK IF THERE ARE ANY transfers WHERE 'AMOUNT' IS LOWER THAN 0", 'results': len(transfers[transfers['AMOUNT'] < 0].index) == 0})

  #### CHECK FOR OUTLIERS IN TRANSACTION AMOUNT AND TRANSACTION BALANCE**
  transfers['AMOUNT'].max()

  '''The highest transaction amount is 87 thousands, so nothing irregular here.
  '''
  
  transfers['BALANCE'].max()
  transfers['BALANCE'].min()

  '''Both maximum and minimum balance in all transfers is the range -42k to 210k so nothing unusual.
  '''
  
  checks.append({'check': "CHECK FOR OUTLIERS IN TRANSACTION AMOUNT AND TRANSACTION BALANCE", 'results': (transfers['BALANCE'].max() < 1000000) & (transfers['BALANCE'].min() > -1000000)})

  #FORMAT DATE TO BE MORE READABLE
  transfers['DATE'] = transfers['DATE'].map(lambda x: ('0' + str(x)) if (len(str(x)) == 7) else x)
  transfers['DATE'] = pd.to_datetime(transfers['DATE'], format="%d%m%Y")
  transfers['DATE'].head()

  ### counties CLEAN-UP
  #### **CHECK IF THERE ARE ANY 'NaN' VALUES IN COUNTIES TABLE**
  checks.append({'check': "CHECK IF THERE ARE ANY 'NaN' VALUES IN COUNTIES TABLE", 'results': counties.isna().sum().sum() == 0})

  #### CHECK FOR OUTLIERS IN EACH CATEGORY

  def check_outliers(table):
      check = {}
      for i in table.columns.tolist():
          check[i] = [{'max': table[i].max()}, {'min': table[i].min()}]
      return check

  check_outliers(counties)

  '''All these numbers look reasonable for each category, and as a bonus we got to see that 'UNEMP_95' has some weird values: '?', which we are going to investigate futher.
  '''
  
  #### FIND RECORDS WITH '?' VALUES IN COLUMNS `UNEMP_95` AND `CRIME_95`
  counties[counties['UNEMP_95'] == '?']
  counties[counties['CRIME_95'] == '?']

  '''It's the same row in both column. It's the column with 'COUNTY_ID' = 69. We don't want to remove this row as this would break consistency among the table. If we ever wanted to join tables
     using 'COUNTY_ID' key, we would be missing some relationships. Instead, we are are going to use avarage change in unemployment and crime between 1995 and 1996 for similar records and update
     the missing values using the mean. By similar we understand records who have close values in the following columns: 'N_INHAB', 'URBAN_RATION', 'AVG_SALARY', 'UNEMP_96' and 'CRIME_96'.
     This is going to be partially manual process, we will filter the data using only one column and try to fit to a subset of counties which look similar. Not very scientific but good enough
     for just one record.
  '''
     
  counties[counties['COUNTY_ID'] == 69]
  similar_counties = counties[(counties['AVG_SALARY'] > 8000) & (counties['AVG_SALARY'] < 8300)]
  similar_counties = similar_counties[similar_counties['COUNTY_ID'] != 69]
  similar_counties.head(50)

  '''We will use this subset to calculate the average change of employment between 1995 and 1996.
  '''

  #### BROKEN UNEMPLOYMENT VALUE UPDATE
  similar_counties['unemp_change'] = similar_counties['UNEMP_96'] - similar_counties['UNEMP_95'].astype('float')
  mean_unemp_change = similar_counties['unemp_change'].mean()

  '''We are going to update `COUNTY_ID` 69, which is represented by Index 68 in the `counties` table
  '''
  
  counties.at[68, 'UNEMP_95'] = counties.iloc[68]['UNEMP_96'] - mean_unemp_change

  '''We are also going to update data type for the full column
  '''
  
  counties['UNEMP_95'] = counties['UNEMP_95'].astype('float')
  counties.iloc[68]

  '''And repeat the process for `CRIME_95` column
  '''
  
  #### CRIME VALUE UPDATE

  similar_counties['crime_change'] = similar_counties['CRIME_96'] - similar_counties['CRIME_95'].astype('float')
  mean_crime_change = similar_counties['crime_change'].mean()
  counties.at[68, 'CRIME_95'] = counties.iloc[68]['CRIME_96'] - mean_crime_change
  counties['CRIME_95'] = counties['CRIME_95'].astype('int64')
  counties.iloc[68]

  '''And finally, check all columns for outliers again.
  '''
  
  ## CHECKS SUMMARY
  checks_summary = []
  for c in checks:
      if c['results']:
          checks_summary.append({'check': c['check'], 'results': 'Pass'})
      else:
          checks_summary.append({'check': c['check'], 'results': 'Fail'})

  ## PRE-SQL CLEAN-UP
  clients.drop(['age', 'today', 'datetime'], axis=1, inplace=True)
  clients['BIRTH_DT'] = pd.to_datetime(clients['BIRTH_DT'], format="%Y%m%d")
  counties.round({'URBAN_RATIO': 2, 'UNEMP_95': 2, 'UNEMP_96': 2})

  return {'checks_summary': checks_summary, 'clients': clients, 'transfers': transfers, 'counties': counties}