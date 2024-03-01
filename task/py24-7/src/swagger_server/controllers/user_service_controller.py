import connexion
import six
import os
from swagger_server.models.rpc_status import RpcStatus  # noqa: E501
from swagger_server.models.v1_user import V1User  # noqa: E501
from swagger_server.models.v1_users import V1Users  # noqa: E501
from swagger_server import util
from swagger_server.repository.mysql import MySQLConnection
from swagger_server.repository.user import UserRepo

mysql_conn = MySQLConnection(
    host= os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'), 
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    name=os.getenv('DB_NAME')
)

user_model = UserRepo(mysql_conn.connect())


def user_service_create_user(name=None, age=None):  # noqa: E501
    """user_service_create_user

     # noqa: E501

    :param name: 
    :type name: str
    :param age: 
    :type age: int

    :rtype: V1User
    """
    users = user_model.create_user("1","kataoka",50)
    
    print(users)
    
    return users


def user_service_delete_user(id):  # noqa: E501
    """user_service_delete_user

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: V1User
    """
    return 'do some magic!'


def user_service_delete_users():  # noqa: E501
    """user_service_delete_users

     # noqa: E501


    :rtype: V1Users
    """
    return 'do some magic!'


def user_service_get_users(name=None):  # noqa: E501
    """user_service_get_users

     # noqa: E501

    :param name: 
    :type name: str

    :rtype: V1Users
    """
    
    users = user_model.get_all_users()
    print(users)
    return 'do some magic!'
