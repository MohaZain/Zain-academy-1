import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Course, Instructor, InstructorCourse, setup_db
from auth import AuthError, requires_auth
import sys


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/instructors')
    def get_instructors():
        try:
            instructors_all = Instructor.query.order_by(Instructor.id).all()
            instructor = [instructor.format()
                          for instructor in instructors_all]
        except BaseException:
            print(sys.exc_info())
            abort(422)
        return jsonify({
            'success': True,
            'instructor': instructor
        })

    @app.route('/instructor', methods=['POST'])
    @requires_auth('post:instructor')
    def add_instructor(payload):
        instructor_data = request.get_json()
        print(instructor_data)
        try:
            instructor = Instructor(
                name=instructor_data['name'],
                phone=instructor_data['phone'],
                email=instructor_data['email']
            )
            instructor.insert()
        except BaseException:
            print(sys.exc_info())
            abort(500)
        return jsonify({
            'success': True
        })

    @app.route('/instructor/<int:instructor_id>', methods=['PATCH'])
    @requires_auth('patch:instructor')
    def edit_instructor_data(payload, instructor_id):
        body = request.get_json()
        instructor_data = Instructor.query.filter(
            Instructor.id == instructor_id).one_or_none()
        if instructor_data is None:
            abort(404)
        try:
            instructor_before = instructor_data.format()
            name_data = body.get('name')
            phone_data = body.get('phone')
            email_data = body.get('email')
            if name_data:
                instructor_data.name = name_data
            if phone_data:
                instructor_data.phone = phone_data
            if email_data:
                instructor_data.email = email_data
            instructor_data.update()

        except BaseException:
            abort(500)

        return jsonify({
            'success': True,
            'instructor_before': instructor_before,
            'instructor_after': instructor_data.format()
        })

    @app.route('/instructor/<int:instructor_id>', methods=['DELETE'])
    @requires_auth('delete:instructor')
    def delete_instructor(payload, instructor_id):
        instructor = Instructor.query.get(instructor_id)
        if instructor is None:
            abort(404)
        try:
            instructor.delete()
        except BaseException:
            print(sys.exc_info())
            abort(500)

        return jsonify({
            'success': True,
            'deleted': instructor_id,
        })
# -----------------------------------------------------------------

    @app.route('/courses')
    def get_courses():
        try:
            courses = Course.query.order_by(Course.id).all()
            course = [course.format()
                      for course in courses]
        except BaseException:
            print(sys.exc_info())
            abort(422)
        return jsonify({
            'success': True,
            'courses': course
        })

    @app.route('/course', methods=['POST'])
    @requires_auth('post:course')
    def add_course(payload):
        course_data = request.get_json()
        try:
            course = Course(
                name=course_data['name'],
                type=course_data['type']
            )
            course.insert()
        except BaseException:
            print(sys.exc_info())
            abort(500)
        return jsonify({
            'success': True
        })

    @app.route('/course/<int:course_id>', methods=['PATCH'])
    @requires_auth('patch:course')
    def edit_course_data(payload, course_id):
        body = request.get_json()
        course_data = Course.query.filter(
            Course.id == course_id).one_or_none()
        if course_data is None:
            abort(404)
        try:
            course_before = course_data.format()
            name_data = body.get('name')
            type_data = body.get('type')
            if name_data:
                course_data.name = name_data
            if type_data:
                course_data.type = type_data

            course_data.update()

        except BaseException:
            abort(500)

        return jsonify({
            'success': True,
            'course_before': course_before,
            'course_after': course_data.format()
        })

    @app.route('/course/<int:course_id>', methods=['DELETE'])
    @requires_auth('delete:course')
    def delete_course(payload, course_id):
        course = Course.query.get(course_id)
        if course is None:
            abort(404)
        try:
            course.delete()
        except BaseException:
            print(sys.exc_info())
            abort(500)

        return jsonify({
            'success': True,
            'deleted': course_id,
        })
  # -------------------------------------------------------------------

    @app.route('/class')
    def get_classes():
        try:
            instrcutor_course = InstructorCourse.query.order_by(
                InstructorCourse.id).all()
            course = [course.format()
                      for course in instrcutor_course]
        except BaseException:
            print(sys.exc_info())
            abort(422)
        return jsonify({
            'success': True,
            'courses_details': course
        })

    @app.route('/class', methods=['POST'])
    @requires_auth('post:instructor_course')
    def add_class(payload):
        data = request.get_json()
        try:
            class_data = InstructorCourse(
                instructor_id=data['instructor_id'],
                course_id=data['course_id'],
                start_time=data['start_time'],
                end_time=data['end_time']
            )
            class_data.insert()
        except BaseException:
            print(sys.exc_info())
            abort(500)
        return jsonify({
            'success': True
        })

    @app.route('/class/<int:class_id>', methods=['DELETE'])
    @requires_auth('delete:instructor_course')
    def remove_class(payload, class_id):
        class_data = InstructorCourse.query.get(class_id)
        if class_data is None:
            abort(404)
        try:
            class_data.delete()
        except BaseException:
            print(sys.exc_info())
            abort(500)

        return jsonify({
            'success': True,
            'deleted': class_id,
        })

    # Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def internal_server(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
