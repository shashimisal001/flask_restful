from sqlalchemy import Table, Column, Integer, String, MetaData, text
from rest_apis.modules.db.sql_alchemy import Connect
import sys


class UserModel:
    metadata_obj = MetaData()
    users_table = Table(
        "users",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("name", String(30)),
        Column("manager_id", Integer)
    )

    def __init__(self):
        self.sql_alchemy = Connect()

    def get_all(self):
        stmt = self.users_table.select()
        result = self.sql_alchemy.sa_conn.execute(stmt)
        results = [dict(row) for row in result]
        return results

    def add_user(self, data):
        stmt = self.users_table.insert().values(data)
        return self.sql_alchemy.sa_conn.execute(stmt)

    def delete_user(self, user_id):
        stmt = self.users_table.delete().where(text("id = '"+user_id+"'"))
        self.sql_alchemy.sa_conn.execute(stmt)

    def update_user(self, user_id, data):
        data.pop('id')
        stmt = self.users_table.update().values(data).where(text("id = '" + str(user_id) + "'"))
        self.sql_alchemy.sa_conn.execute(stmt)
