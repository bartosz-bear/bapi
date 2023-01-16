# Utils

## Anaconda

Good Anaconda guide

<https://towardsdatascience.com/introduction-to-conda-virtual-environments-eaea4ac84e28>

<https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/>

## SQLAlchemy

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

SQLAcademy generates SQL statements from Python code, and psycopg2 sends SQL statements to the database. SQLAcademy depends on psycopg2 or other database drivers to communicate with a database.

<https://www.sqlalchemy.org/>

## psycopg

psycopg is the most popular PostgreSQL adapter (database driver) for Python. It's core is a complete implementation of the Python DB API 2.0 specifications

<https://www.psycopg.org/>

## decouple module

Decouple helps you to organize your settings so that you can change parameters without having to redeploy your app.

It also makes it easy for you to:

1. store parameters in `ini` or `.env` files
2. define comprehensive default values
3. have only one configuration module to rule all of your instances

It was originally designed for Django, but became an independent generic tool for separating settings from code.

<https://pypi.org/project/python-decouple/>

## How to use python decouple module?

See the first answer

<https://stackoverflow.com/questions/64208678/hiding-secret-key-in-django-project-on-github-after-uploading-project>

## PIP - How to create a `requirements.txt` file?

```powershell
pip freeze > requirements.txt
```