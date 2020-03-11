from sqlalchemy import create_engine
import os


def get_instance():
    connection_info = os.getenv("MYSQL_CONNECTION_INFO")
    mysql_engine = create_engine(connection_info)
    return mysql_engine.connect()


def get_engine():
    connection_info = os.getenv("MYSQL_CONNECTION_INFO")
    return create_engine(connection_info)
