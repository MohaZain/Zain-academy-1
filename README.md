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
1. **Instructor**  - Instructor Can Access {post:instructor-course}  {post:course}
2. **admin**  - Admin Have Access to all endpoint 
>_note_: **I provieded a user token for each roles in setup.sh **

## API
**Error Codes**  
1. **404**  Resource not found

2. **422** Unprocessable

3. **400** Bad request

4. **500** Internal server error

5. **405** Methods not allowed

6. **401** Unuthorized

**Example**
``` 
"success": False
"error": 405,
"message": "Method Not Allowed"
```
**Instructor**   
```
GET '/instructors'
- Fetches a list of instructors 
- Returns: list of instructors information 
{
'success': True,
"instructor": [
        {
            "email": "FSND@udacity.com",
            "id": 1,
            "name": "Mohammed zain",
            "phone": "966788738"
        },
        {
            "email": "FSND-web@udacity.com",
            "id": 2,
            "name": "Hanna qasm",
            "phone": "9668883838"
        }]
}

```
```
POST '/instructor'
- Sends a post request in order to add a new instructor
- Request Body: 
{
    "name":"jaber ali",
    "phone":"123123",
    "email":"qwe@gmail.com"
}
- Returns: 
{
'success': True
}
```
```
PATCH '/instructor/${id:int}'
- Sends a PATCH request in order to edit instructors information 
- Request Arguments: id - integer
- Request Body: 
{
    "email":"qwe@udacity-99.com"
}
- Returns: 
{
'success': True
'instructor_before':{
                     'name':"jaber ali",
                     'phone':'123123',
                     'email':'qwe@gmail.com'
                     },
'instructor_after': {
                     'name':"jaber ali",
                     'phone':'123123',
                     'email':'qwe@udacity-99.com'
                    }
}
```
```
DELETE '/instructor/${id}'
- Deletes a specified instructor using the id of the instructor
- Request Arguments: id - integer
- Returns: Deleted id
{
'success': True,
'deleted': instructor_id
}
```
**Course** 
```
GET '/courses'
- Fetches a list of courses 
- Returns: list of courses information 
{
'success': True,
"course": [
        {
            "name": "OOP",
            "type": "programming",
        },
        {
            "name": "algorithms",
            "type": "math",
        }]
}

```
```
POST '/course'
- Sends a post request in order to add a new course 
- Request Body: 
{
    "name":"Artificial Intelligence",
    "type":"AI",
}
- Returns: 
{
'success': True
}
```
```
PATCH '/course/${id:int}'
- Sends a PATCH request in order to edit course information 
- Request Arguments: id - integer
- Request Body: 
{
    "name":"Object-oriented programming "
}
- Returns: 
{
'success': True
'course_before':{
            "name": "OOP",
            "type": "programming",
                     },
'instructor_after': {
            "name": "Object-oriented programming",
            "type": "programming",
                    }
}
```
```
DELETE '/course/${id}'
- Deletes a specified course using the course id
- Request Arguments: id - integer
- Returns: Deleted id
{
'success': True,
'deleted': course_id
}
```
**Class** 
```
GET '/class'
- Fetches a list of classes 
- Returns: list of class information 
{
'success': True,
"class": [
        {
            "start_time": "01-01-2021",
            "end_time": "01-02-2021",
            "id": 1,
            "instructor_name": "Mohammed zain",
            "course_name": "algorithms"
        }
        ]
}
```
```
POST '/class'
- Sends a post request in order to add a new class 
- Request Body: 
{
          "instructor_id"=1,
          "course_id"=1,
          start_time='01-01-2020',
          end_time='01-02-2020'
}
- Returns: 
{
'success': True
}
```
```
DELETE '/class/${id}'
- Deletes a specified class using the class id
- Request Arguments: id - integer
- Returns: Deleted id
{
'success': True,
'deleted': class_id
}
```
[API Documents](https://documenter.getpostman.com/view/16467666/TzzEpaVn)  
Replace {{host}} with https://zain-academy-dep.herokuapp.com/
