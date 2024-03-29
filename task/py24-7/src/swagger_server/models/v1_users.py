# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.v1_user import V1User
from swagger_server import util


class V1Users(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, users: List[V1User]=None):  # noqa: E501
        """V1Users - a model defined in Swagger

        :param users: The users of this V1Users.  # noqa: E501
        :type users: List[V1User]
        """
        self.swagger_types = {
            'users': List[V1User]
        }

        self.attribute_map = {
            'users': 'users'
        }

        self._users = users

    @classmethod
    def from_dict(cls, dikt) -> 'V1Users':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v1Users of this V1Users.  # noqa: E501
        :rtype: V1Users
        """
        return util.deserialize_model(dikt, cls)

    @property
    def users(self) -> List[V1User]:
        """Gets the users of this V1Users.


        :return: The users of this V1Users.
        :rtype: List[V1User]
        """
        return self._users

    @users.setter
    def users(self, users: List[V1User]):
        """Sets the users of this V1Users.


        :param users: The users of this V1Users.
        :type users: List[V1User]
        """

        self._users = users
