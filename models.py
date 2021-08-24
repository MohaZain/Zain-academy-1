from sqlalchemy import Column, Integer, String, create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

import json
import os
# database_name = "zacademy"
# database_path = "postgresql://{}/{}".format('localhost:5432', database_name)
# = "postgresql://localhost:5432/zacademy"
database_path = os.environ['DATABASE_URL'] = 'postgresql://ujvxkjclrtmyji:ca394ea08e752d105afda1402a94b627c130dfcc0f7ef263b5cdd929fb945f45@ec2-54-236-234-167.compute-1.amazonaws.com:5432/d7ik7isoh6bokr'
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Instructor
'''


class Instructor(db.Model):
    __tablename__ = 'instructors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    # Relation with Course
    Course = relationship("Course", secondary="instructor_course")

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email}


'''
Course
'''


class Course(db.Model):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    # Relation with Artists
    instructors = relationship("Instructor", secondary="instructor_course")

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type}


'''
Instructor Course
'''


class InstructorCourse(db.Model):
    __tablename__ = 'instructor_course'

    id = Column(Integer, primary_key=True)
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructors.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, instructor_id, course_id, start_time, end_time):
        self.instructor_id = instructor_id
        self.course_id = course_id
        self.start_time = start_time
        self.end_time = end_time

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        course = Course.query.get(self.course_id)
        instructor = Instructor.query.get(self.instructor_id)
        return {
            'id': self.id,
            'instructor_name': instructor.name,
            'course_name': course.name,
            'start_time': self.start_time,
            'end_time': self.end_time}
