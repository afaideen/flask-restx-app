from flask_restx import Resource, Namespace

# from .api_models import course_model, student_model, course_input_model, student_input_model
from .extensions import db
# from .models import Course, Student

ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {"hello": "restx"}