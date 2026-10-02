# neuralnine-flask

A collection of Flask learning projects and experiments covering the fundamentals of Python web development and progressively more structured Flask applications.

The repository contains smaller Flask examples in `firstapp` and a more structured application using Flask Blueprints, SQLAlchemy, and Flask-Migrate in `blueprintapp`.

## Topics Covered

- Flask application setup
- Routing and URL parameters
- Query parameters
- HTTP methods
- Custom responses and status codes
- Jinja2 templates
- Custom Jinja2 template filters
- Redirects and URL generation
- Static files
- Cookies
- Sessions
- SQLAlchemy
- Flask-Migrate and Alembic
- Flask Blueprints
- Database-backed applications
- Flask-Login
- Flask-Bcrypt
- Docker

## Repository Structure

~~~text
neuralnine-flask/
├── blueprintapp/
│   ├── blueprints/
│   │   ├── core/
│   │   ├── people/
│   │   └── todos/
│   ├── templates/
│   └── app.py
├── firstapp/
│   ├── dbapplication/
│   ├── dbappPractice/
│   ├── static/
│   ├── templates/
│   ├── app.py
│   ├── app2.py
│   ├── app3.py
│   ├── app4.py
│   ├── flask5.py
│   ├── flask6.py
│   ├── flask6Practice.py
│   └── onemore.py
├── dockerfile
├── requirements.txt
├── run.py
├── .gitignore
└── README.md
~~~

## Blueprint Application

The `blueprintapp` directory contains a more structured Flask application built around Flask Blueprints.

It includes three areas:

### Core

Provides the main application page.

### People

Provides a database-backed interface for creating and viewing people.

The `Person` model contains:

- ID
- Name
- Age
- Job

### Todos

Provides a database-backed todo application.

The `Todo` model contains:

- ID
- Title
- Description
- Completion status

The application uses Flask-SQLAlchemy for database access and Flask-Migrate for database migrations.

## Firstapp

The `firstapp` directory contains progressively developed Flask examples.

The examples cover:

- Basic Flask routes
- Dynamic URL parameters
- Query parameters
- Request methods
- Custom HTTP responses
- Jinja2 template rendering
- Custom template filters
- Redirects
- Static files
- Cookies
- Sessions
- SQLAlchemy
- Flask-Migrate
- User authentication with Flask-Login
- Password handling with Flask-Bcrypt

The `dbapplication` example also demonstrates a basic user model with login and logout functionality.

## Docker

The repository includes a Dockerfile for running the Blueprint application.

The container installs the root requirements, initializes the Flask-Migrate database structure, and starts the application through `run.py`.

## Technologies

- Python
- Flask
- Jinja2
- Flask-SQLAlchemy
- SQLAlchemy
- Flask-Migrate
- Alembic
- Flask-Login
- Flask-Bcrypt
- SQLite
- Docker

## Purpose

This repository was built while learning Flask and backend web development. It contains the progression from simple Flask routes and templates to database-backed applications, authentication, migrations, Blueprints, and containerization.
