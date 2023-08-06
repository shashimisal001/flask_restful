from sqlalchemy import Table, Column, Integer, String, MetaData
from rest_apis.modules.db.sql_alchemy import Connect


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
