CREATE TABLE clients (
  id SERIAL PRIMARY KEY,
  client_id INT NOT NULL UNIQUE,
  account_id INT NOT NULL UNIQUE,
  gender VARCHAR(50) NOT NULL CHECK (gender IN ('m', 'f')),
  birth_dt DATE NOT NULL,
  active BOOLEAN NOT NULL,
  loan BOOLEAN NOT NULL,
  county_id INT NOT NULL,
  set_split VARCHAR(50) NOT NULL CHECK (set_split IN ('test', 'train'))
);

CREATE TABLE transfers (
  id SERIAL PRIMARY KEY,
  transfer_id INT NOT NULL UNIQUE,
  account_id INT NOT NULL UNIQUE,
  date DATE NOT NULL,
  amount MONEY NOT NULL,
  balance MONEY NOT NULL,
  type VARCHAR(50) NOT NULL CHECK (type IN ('CREDIT', 'WITHDRAWAL')),
  operation VARCHAR(50) NOT NULL CHECK (type IN ('CC_WITHDRAWAL', 'COLLECTION_FROM_OTHER_BANK', 'CREDIT_IN_CASH', 'REMITTANCE_TO_OTHER_BANK', 'WITHDRAWAL_IN_CASH', 'CREDIT_TO_CC'))
);

CREATE TABLE counties (
  id SERIAL PRIMARY KEY,
  county_id INT NOT NULL UNIQUE,
  n_inhab INT NOT NULL,
  n_cities INT NOT NULL,
  urban_ratio DECIMAL(2) NOT NULL,
  avg_salary MONEY NOT NULL,
  unemp_95 DECIMAL(2) NOT NULL,
  unemp_96 DECIMAL(2) NOT NULL,
  n_entr INT NOT NULL,
  crime_95 INT NOT NULL,
  crime_96 INT NOT NULL
);