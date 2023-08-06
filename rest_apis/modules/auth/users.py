import sys
from flask_restful import Resource
from rest_apis.modules.models.user_model import UserModel


class Users(Resource):
    def __init__(self):
        self.user_model = UserModel()


    def get(self):
        return {'data': self.user_model.get_all(), 'status': 'success'}, 200

    def post(self):
        return {"data": "User added", "status": "success"}, 200

    def put(self):
        return {"data": "User completely updated", "status": "success"}, 200

    def patch(self):
        return {"data": "User partially updated", "status": "success"}, 200

    def delete(self):
        return {"data": "User deleted", "status": "success"}, 200

    