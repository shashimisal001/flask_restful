import urllib, jsonify
from rest_apis.config import Config
import sqlalchemy


class Connect:
    sa_engine = None
    sa_conn = None

    def __init__(self):
        db_conf = Config.DB_SETTINGS['SQL_SERVER']
        server = db_conf['SERVER_NAME']  # to specify an alternate port
        database = db_conf['DB_NAME']
        username = db_conf['USERNAME']
        password = db_conf['PASSWORD']
        params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                         "SERVER="+server+";"
                                         "DATABASE="+database+";"
                                         "UID="+username+";"
                                         "PWD="+password)
        self.sa_engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
        self.sa_conn = self.sa_engine.connect()


