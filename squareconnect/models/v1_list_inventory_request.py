# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class V1ListInventoryRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, limit=None, batch_token=None):
        """
        V1ListInventoryRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'limit': 'int',
            'batch_token': 'str'
        }

        self.attribute_map = {
            'limit': 'limit',
            'batch_token': 'batch_token'
        }

        self._limit = limit
        self._batch_token = batch_token

    @property
    def limit(self):
        """
        Gets the limit of this V1ListInventoryRequest.
        The maximum number of inventory entries to return in a single response. This value cannot exceed 1000.

        :return: The limit of this V1ListInventoryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this V1ListInventoryRequest.
        The maximum number of inventory entries to return in a single response. This value cannot exceed 1000.

        :param limit: The limit of this V1ListInventoryRequest.
        :type: int
        """

        self._limit = limit

    @property
    def batch_token(self):
        """
        Gets the batch_token of this V1ListInventoryRequest.
        A pagination cursor to retrieve the next set of results for your original query to the endpoint.

        :return: The batch_token of this V1ListInventoryRequest.
        :rtype: str
        """
        return self._batch_token

    @batch_token.setter
    def batch_token(self, batch_token):
        """
        Sets the batch_token of this V1ListInventoryRequest.
        A pagination cursor to retrieve the next set of results for your original query to the endpoint.

        :param batch_token: The batch_token of this V1ListInventoryRequest.
        :type: str
        """

        self._batch_token = batch_token

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other