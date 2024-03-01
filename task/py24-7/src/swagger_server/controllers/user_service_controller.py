import connexion
import six
import os
import uuid
import json
import http

from swagger_server.models.rpc_status import RpcStatus  # noqa: E501
from swagger_server.models.v1_create_user_request import V1CreateUserRequest  # noqa: E501
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


def user_service_create_user(body):  # noqa: E501
    """user_service_create_user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: V1User
    """
    if connexion.request.is_json:
        body = V1CreateUserRequest.from_dict(connexion.request.get_json())  # noqa: E501
    uid = str(uuid.uuid4())
    try:
        users = user_model.create_user(uid , body.name, body.age)
    except Exception as e:
        print(e)
        return err(400,"invalid request")
    print(users)
    json_data = {
        "id": uid,
        "name": body.name,
        "age": body.age
    }
    return json_data


def user_service_delete_user(id_):  # noqa: E501
    """user_service_delete_user

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: V1User
    """
    try:
        user = user_model.get_user(id_)
        if user == []:
            raise ValueError("no user Error")
        user_model.delete_user(id_)
    except ValueError as e:
        print(e)
        return err(400,"no user Error")
    except Exception as e:
        print(e)
        return {}, http.HTTPStatus.BAD_REQUEST
    
    return {
        "id": id_,
        "name": user[1],
        "age": user[2]
    }


def user_service_delete_users():  # noqa: E501
    """user_service_delete_users

     # noqa: E501


    :rtype: V1Users
    """
    try:
        user_model.delete_all()
    except Exception as e:
        print(e)
        return err(400,"can't delete all users")
    return {"status":"delete: all"}


def user_service_get_users(name= None):  # noqa: E501
    """user_service_get_users

     # noqa: E501

    :param name: 
    :type name: str

    :rtype: V1Users
    """
    try:
        if name is None:
            users = user_model.get_all_users()
        else:
            print(name)
            users = user_model.get_search_user(name)
    except Exception as e:
        print(e)
        return err(400,"cant't search Error")
    print(users)
    json_data = []
    for user in users:
        json_data.append({
            "id": user[0],
            "name": user[1],
            "age": user[2]
        })
    return json_data

def err (err, message: str):
    if err == 400:
        return {"error": message}, http.HTTPStatus.BAD_REQUEST