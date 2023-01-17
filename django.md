# Django

## How to start a development server?

```
python manage.py runserver
```

## How to start a server on a different port and/or different IP?

```
python manage.py runserver 8080

python manage.py runserver 0.0.0.0:8000
```

## How to exit a running server?

```
Ctrl + C
```

## Database Migrations

We have to run this command every time anything changes in the `models.py`

```powershell
python manage.py makemigrations # migrations preparation step

python manage.py migrate # apply migrations
```

The `migrate` command looks at the `INSTALLED_APPS` setting and creates any necessary database tables according to the database settings in your `mysite/settings.py`, as well as database migrations shipped with the app.

## How to set up PostgreSQL in Django?

<https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8>

## How to create a new Django app?

```powershell
django-admin startproject my_new_appp
```

## Difference between a project and an app?

A project is a collection of configuration and apps for a particular website. An app is part of a website (project) which is responsible for a particular functionality (eg. a poll app or a database of public records).

## How `path(route, view, kwargs, name)` function works?

`route` is a string that contains a URL pattern. Patterns don't search `GET` and `POST` parameters, or the domain name. For example, in a request to `https://www.example.com/myapp/`, the URLconf will look for `myapp/`. In a request to `https://www.example.com/myapp/?page=3`, the URLconf will also look for `myapp/`.

`view` - when Django finds a matching pattern, it calls the specified view function with an `HttpRequest` object as the first argument and any 'captured' values from the `route` as keyword arguments.

`name` - naming your URL lets you refer to it unambiguously from elsewhere in Django, especially form within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.