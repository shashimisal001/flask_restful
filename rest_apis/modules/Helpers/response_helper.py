class ResponseHelper:
    def success_response(self, data):
        data.setdefault('data', {})
        data.setdefault('msg', '')
        return {'data': data['data'], 'msg': data['msg'], 'status': 'success'}, 200

    def error_response(self, data):
        return {'msg': data['msg'], 'status': 'failure'}, 400
