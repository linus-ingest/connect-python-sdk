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


class CustomerCreationSourceFilter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, values=None, rule=None):
        """
        CustomerCreationSourceFilter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'values': 'list[str]',
            'rule': 'str'
        }

        self.attribute_map = {
            'values': 'values',
            'rule': 'rule'
        }

        self._values = values
        self._rule = rule

    @property
    def values(self):
        """
        Gets the values of this CustomerCreationSourceFilter.
        The list of creation sources used as filtering criteria. See [CustomerCreationSource](#type-customercreationsource) for possible values

        :return: The values of this CustomerCreationSourceFilter.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this CustomerCreationSourceFilter.
        The list of creation sources used as filtering criteria. See [CustomerCreationSource](#type-customercreationsource) for possible values

        :param values: The values of this CustomerCreationSourceFilter.
        :type: list[str]
        """

        self._values = values

    @property
    def rule(self):
        """
        Gets the rule of this CustomerCreationSourceFilter.
        Indicates whether a customer profile matching the filter criteria should be included in the result or excluded from the result. Default: `INCLUDE`. See [CustomerInclusionExclusion](#type-customerinclusionexclusion) for possible values

        :return: The rule of this CustomerCreationSourceFilter.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """
        Sets the rule of this CustomerCreationSourceFilter.
        Indicates whether a customer profile matching the filter criteria should be included in the result or excluded from the result. Default: `INCLUDE`. See [CustomerInclusionExclusion](#type-customerinclusionexclusion) for possible values

        :param rule: The rule of this CustomerCreationSourceFilter.
        :type: str
        """

        self._rule = rule

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
