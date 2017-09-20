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


class CatalogModifierOverride(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, modifier_id=None, on_by_default=None):
        """
        CatalogModifierOverride - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'modifier_id': 'str',
            'on_by_default': 'bool'
        }

        self.attribute_map = {
            'modifier_id': 'modifier_id',
            'on_by_default': 'on_by_default'
        }

        self._modifier_id = modifier_id
        self._on_by_default = on_by_default

    @property
    def modifier_id(self):
        """
        Gets the modifier_id of this CatalogModifierOverride.
        The ID of the [CatalogModifier](#type-catalogmodifier) whose default behavior is being overridden.

        :return: The modifier_id of this CatalogModifierOverride.
        :rtype: str
        """
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, modifier_id):
        """
        Sets the modifier_id of this CatalogModifierOverride.
        The ID of the [CatalogModifier](#type-catalogmodifier) whose default behavior is being overridden.

        :param modifier_id: The modifier_id of this CatalogModifierOverride.
        :type: str
        """

        if modifier_id is None:
            raise ValueError("Invalid value for `modifier_id`, must not be `None`")
        if len(modifier_id) < 1:
            raise ValueError("Invalid value for `modifier_id`, length must be greater than or equal to `1`")

        self._modifier_id = modifier_id

    @property
    def on_by_default(self):
        """
        Gets the on_by_default of this CatalogModifierOverride.
        If `true`, this [CatalogModifier](#type-catalogmodifier) should be selected by default for this [CatalogItem](#type-catalogitem).

        :return: The on_by_default of this CatalogModifierOverride.
        :rtype: bool
        """
        return self._on_by_default

    @on_by_default.setter
    def on_by_default(self, on_by_default):
        """
        Sets the on_by_default of this CatalogModifierOverride.
        If `true`, this [CatalogModifier](#type-catalogmodifier) should be selected by default for this [CatalogItem](#type-catalogitem).

        :param on_by_default: The on_by_default of this CatalogModifierOverride.
        :type: bool
        """

        self._on_by_default = on_by_default

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
