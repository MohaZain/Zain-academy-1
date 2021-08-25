# Zain-Academy
 ### Interductions
 Zain Academy is an online platform help to connect teachers with thier targeted students and make thier knowladge available to the community.
 
 ### Website Link
 [https://zain-academy-dep.herokuapp.com/instructors](https://zain-academy-dep.herokuapp.com/instructors)
 
 ### Installing Dependencies
 
 1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip3 install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

### Running the server

From within the `./zain-academy-1` directory.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
### Database Setup
From the zain-academy-1 folder in terminal run:
```createdb data_name```

```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

```
### Authentication
  **Roles**
1. **Instructor** 
2. **admin** 
>_note_: **I provieded a user token for each roles in token file**
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

```
## API

[API Documents](https://documenter.getpostman.com/view/16467666/TzzEpaVn)  
Replace {{host}} with https://zain-academy-dep.herokuapp.com/
