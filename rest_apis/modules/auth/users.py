import sys
from flask import request
from flask_restful import Resource
from rest_apis.modules.models.user_model import UserModel
from rest_apis.modules.Helpers.response_helper import ResponseHelper


class Users(Resource):
    def __init__(self):
        self.user_model = UserModel()


    def get(self):
        try:
            result = self.user_model.get_all()
            return ResponseHelper().success_response({'data': result})
        except Exception as e:
            return ResponseHelper().error_response({'msg': str(e)})


    def post(self):
        try:
            data = request.get_json()
            self.user_model.add_user(data['user'])
            return ResponseHelper().success_response({'msg': 'User added successfully'})
        except Exception as e:
            return ResponseHelper().error_response({'msg': str(e)})

    def put(self):
        try:
            data = request.get_json()
            self.user_model.update_user(data['user']['id'], data['user'])
            return ResponseHelper().success_response({'msg': 'User updated successfully'})
        except Exception as e:
            return ResponseHelper().error_response({'msg': str(e)})

    def patch(self):
        return self.put()

    def delete(self):
        try:
            data = request.get_json()
            self.user_model.delete_user(str(data['id']))
            return ResponseHelper().success_response({'msg': 'User deleted successfully'})
        except Exception as e:
            return ResponseHelper().error_response({'msg': str(e)})

    