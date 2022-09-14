# tms-shop
Simple REST API build with Django-rest-framework

## Simple REST API build with Django-rest-framework
- primitive API for a shop
- displaying products
- displaying a list of categories
- displaying products in a specific category
- receiving feedback and storing information in the database

## Running locally:

1 - To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

2 - Insert your own db configuration settings:


`SECRET_KEY`<br />
`DB_NAME`<br />
`DB_USER`<br />
`DB_PASSWORD`<br />

3 - Migrate db models to PostgreSQL:

`python3 manage.py migrate`

4 - Run app:

`python3 manage.py runserver`