import os

from flask_sqlalchemy import SQLAlchemy

# initialize sql-alchemy
db = SQLAlchemy(engine_options={"pool_pre_ping": True, "pool_recycle": 1800})


def get_tablename(tablename):
    name = os.getenv("APIREST_SERVICE_NAME")
    if name:
        return "{}_{}".format(name, tablename)
    return tablename


gt = get_tablename
