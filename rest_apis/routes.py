from rest_apis import app, api
from rest_apis.modules.auth.users import Users

api.add_resource(Users, "/users")
