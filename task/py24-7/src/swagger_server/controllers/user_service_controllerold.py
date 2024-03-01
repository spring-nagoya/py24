import connexion
import six
import os
import uuid
import json
from swagger_server.models.rpc_status import RpcStatus  # noqa: E501
from swagger_server.models.v1_user import V1User  # noqa: E501
from swagger_server.models.v1_users import V1Users  # noqa: E501
from swagger_server import util
from swagger_server.repository.mysql import MySQLConnection
from swagger_server.repository.user import UserRepo

mysql_conn = MySQLConnection(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    name=os.getenv("DB_NAME"),
)

user_model = UserRepo(mysql_conn.connect())


def user_service_create_user(name, age):  # noqa: E501
    """user_service_create_user

     # noqa: E501

    :param name:
    :type name: str
    :param age:
    :type age: int

    :rtype: V1User
    """
    id = str(uuid.uuid4())
    try:
        users = user_model.create_user(id , name, age)
    except Exception as e:
        print(e)
        return json.dumps({"error":"error"})
    print(users)
    return json.dumps(users)

def user_service_delete_user(id):  # noqa: E501
    """user_service_delete_user

     # noqa: E501

    :param id:
    :type id: str

    :rtype: V1User
    """
    try:
        user_model.delete_user(id)
    except Exception as e:
        print(e)
        return json.dumps({"error":"error"})
    return json.dumps({"status":"delete: " + id})


def user_service_delete_users():  # noqa: E501
    """user_service_delete_users

     # noqa: E501


    :rtype: V1Users
    """
    try:
        user_model.delete_all()
    except Exception as e:
        print(e)
        return json.dumps({"error":"error"})
    return json.dumps({"status":"delete: all"})


def user_service_get_users(name):  # noqa: E501
    """user_service_get_users

     # noqa: E501

    :param name:
    :type name: str

    :rtype: V1Users
    """
    try:
        if 'name' in locals():
            users = user_model.get_all_users()
        else:
            users = user_model.get_user(name)
    except Exception as e:
        print(e)
        return json.dumps({"error":"error"})
    print(users)
    return json.dumps(users)
