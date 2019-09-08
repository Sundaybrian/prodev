# Prodev

### 06/09/2019

## By **[Brian Sunday](https://github.com/Sundaybrian/prodev)**

## Description

The application will allow a user to post a project he/she has created and get it reviewed by his/her peers.Users can rate the website.View other submissions of other users.A user can delete a submission or update.

## User Stories

As a user I would like:

* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page

## Specifications

| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Register to be a user | Your email : john@doe.com  Username : jonDoo  Password : doe | New user is registered |
| User Log in | Your email : john@doe.com  Password : doe | Logged in |
| Create Post | Click Add Button |Authenticated User is redirected to a form page to create a new post|
| View Post | Click on Post title | Redirected to a page that has that single post|
| Rate a post | Fill the form field provided | Authenticated user is allowed to make a review|
| Delete a Post | Click Trash Icon| Authenticated user i.e owner of the post is prompted to delete|
| Update a Post | Click Update Icon| Authenticated user i.e owner of the post is redirected to a form field to update the post|
| Update profile | Click edit profile | Pop up modal to update your details |
| Search | type on search field| Redirect to a results page if query exists |


## Setup/Installation Requirements

* `$ git clone` [prodev](https://github.com/Sundaybrian/prodev)
* `$ cd prodev`


    ```python
    #create a .env file
    SECRET_KEY = '<Secret_key>'
    DBNAME = 'prodev2'
    USER = '<username>'
    PASSWORD = '<password>'
    DEBUG = True

    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = '<your-email>'
    EMAIL_HOST_PASSWORD = '<your-password>'
    ```    

* `$ python3.6 -m venv virtual` to create a  virtual environment
* `$ source virtual/bin/activate` to activate the virtual environment
* `$ psql` to activate the postgres server
* `$ username=create database pixels` create db with the name prodev2
* run `$ python3.6 -m pip install -r requirements.txt ` to install dependencies
* `$ python3.6 manage.py makemigrations` to initialize database migrations
* `$ python3.6 manage.py migrate` to commit the migration you are running
* `$ python3.6 manage.py runserver` to run the app
* open `localhost:8000` to view the app

## Known Bugs

* No known Bugs

## Technologies Used

* Python3.6
* Django 2.2.4
* Javascript
* Masonry Grid
* Bootstrap
* Postgres Database
* CSS
* HTML
* Heroku

### License

MIT (c) 2019 **[Brian Sunday](https://github.com/Sundaybrian/prodev)**


