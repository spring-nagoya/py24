# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class V1User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, age: int=None):  # noqa: E501
        """V1User - a model defined in Swagger

        :param id: The id of this V1User.  # noqa: E501
        :type id: str
        :param name: The name of this V1User.  # noqa: E501
        :type name: str
        :param age: The age of this V1User.  # noqa: E501
        :type age: int
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'age': int
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'age': 'age'
        }

        self._id = id
        self._name = name
        self._age = age

    @classmethod
    def from_dict(cls, dikt) -> 'V1User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v1User of this V1User.  # noqa: E501
        :rtype: V1User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this V1User.


        :return: The id of this V1User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this V1User.


        :param id: The id of this V1User.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this V1User.


        :return: The name of this V1User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this V1User.


        :param name: The name of this V1User.
        :type name: str
        """

        self._name = name

    @property
    def age(self) -> int:
        """Gets the age of this V1User.


        :return: The age of this V1User.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age: int):
        """Sets the age of this V1User.


        :param age: The age of this V1User.
        :type age: int
        """

        self._age = age
