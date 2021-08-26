import os
from re import search
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import Course, Instructor, setup_db, db_drop_and_create_all


class TriviaTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['DATABASE_URL'] = "postgresql://localhost:5432/zacademy_test"
        setup_db(self.app, self.database_path)

        # TOKEN 
        self.instructor_token = os.environ['instructor_token']
        self.admin_token = os.environ['admin_token']
        
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_instructor = {
            'name': 'mohammed bin zain',
            'phone': '098762999',
            'email': 'asq@gmail.com'
        }
        self.new_instructor_bad_req = {
            'name': 'mohammed bin zain',
            'phone': '098762999',
        }
        self.new_course = {
            'name': 'AI',
            'type': 'programming'
        }
        self.new_class = {
            "course_id": 1,
            "end_time": "01-01-2021",
            "instructor_id": 1,
            "start_time": "01-02-2021"
        }
        self.edit = {
            'email': 'udacity@udacity.com'
        }
        self.edit_type = {
            'type': 'udacity programming course'

        }

    def tearDown(self):
        db_drop_and_create_all()
        """Executed after reach test"""
        pass

# Auth test
    def test_403_instructor(self):
        res = self.client().post('/instructor', json=self.new_instructor, headers={"Authorization": 'bearer ' + self.instructor_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        
    def test_401_instructor(self):
        res = self.client().post('/instructor', json=self.new_instructor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        
    def test_get_instructors(self):
        res = self.client().get('/instructors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_instructor(self):
        res = self.client().post('/instructor', json=self.new_instructor, headers={"Authorization": 'bearer ' + self.admin_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_500_server_error_instructor(self):
        res = self.client().post('/instructor', json=self.new_instructor_bad_req, headers={"Authorization": 'bearer ' + self.admin_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['success'], False)

    def test_edit_instructor(self):
        res = self.client().patch('/instructor/1', json=self.edit, headers={"Authorization": 'bearer ' + self.admin_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_if_instructor_not_exist(self):
        res = self.client().delete('/instructor/1000', json=self.edit, headers={"Authorization": 'bearer ' + self.admin_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_404_remove_instructor_not_exist(self):
        res = self.client().delete('/instructor/1000', headers={"Authorization": 'bearer ' + self.admin_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    # ///////////////////////////////COURSE//////////////////////////////////////////

    def test_get_courses(self):
        res = self.client().get('/courses')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_course(self):
        res = self.client().post('/course', json=self.new_course, headers={"Authorization": 'bearer ' + self.instructor_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_500_server_error_course(self):
        res = self.client().post('/course', json=self.new_instructor_bad_req, headers={"Authorization": 'bearer ' + self.admin_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['success'], False)

    def test_edit_course(self):
        res = self.client().patch('/course/1', json=self.edit_type, headers={"Authorization": 'bearer ' + self.admin_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_if_course_not_exist(self):
        res = self.client().delete('/course/1000', json=self.edit_type, headers={"Authorization": 'bearer ' + self.admin_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_404_remove_course_not_exist(self):
        res = self.client().delete('/course/1000', headers={"Authorization": 'bearer ' + self.admin_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    # //////////////////////////////////CLASSES///////////////////////////////////////

    def test_get_classes(self):
        res = self.client().get('/class')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_class(self):
        res = self.client().post('/class', json=self.new_class, headers={"Authorization": 'bearer ' + self.instructor_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_500_server_error_class(self):
        res = self.client().post('/class', json=self.new_instructor_bad_req, headers={"Authorization": 'bearer ' + self.admin_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['success'], False)

    def test_404_remove_course_not_exist(self):
        res = self.client().delete('/course/1000', headers={"Authorization": 'bearer ' + self.admin_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    # Remove

    def test_remove_class(self):
        res = self.client().delete('/class/1', headers={"Authorization": 'bearer ' + self.admin_token})
        data = json.loads(res.data)
        cou = Course.query.get(1)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertEqual(cou, None)

    def test_remove_course(self):
        res = self.client().delete('/course/1', headers={"Authorization": 'bearer ' + self.admin_token})
        data = json.loads(res.data)
        cou = Course.query.get(1)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertEqual(cou, None)

    def test_remove_instructor(self):
        res = self.client().delete('/instructor/1', headers={"Authorization": 'bearer ' + self.admin_token})
        data = json.loads(res.data)
        inst = Instructor.query.get(1)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertEqual(inst, None)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
