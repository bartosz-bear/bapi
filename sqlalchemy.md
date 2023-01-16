# SQLAlchemy

## How to connect to a DB from Python?

```python
import sqlalchemy

from sqlalchemy import create_engine

engine = create_engine('postgresql://user_name:passoword@localhost:5432/Database_Name')
```

## How to show tables in the database?

```python
print(engine.table_names())
```

## How to read data using SQLAlchemy and pandas?

```python
import pandas as pd

df = pd.read_sql('select * from datacamp_courses', engine)

df.head()
```

```python

```
