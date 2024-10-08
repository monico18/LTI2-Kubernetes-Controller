# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.29.4+k3s1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class IoTraefikV1alpha1TLSStoreSpecDefaultGeneratedCertDomain(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'main': 'str',
        'sans': 'list[str]'
    }

    attribute_map = {
        'main': 'main',
        'sans': 'sans'
    }

    def __init__(self, main=None, sans=None, _configuration=None):  # noqa: E501
        """IoTraefikV1alpha1TLSStoreSpecDefaultGeneratedCertDomain - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._main = None
        self._sans = None
        self.discriminator = None

        if main is not None:
            self.main = main
        if sans is not None:
            self.sans = sans

    @property
    def main(self):
        """Gets the main of this IoTraefikV1alpha1TLSStoreSpecDefaultGeneratedCertDomain.  # noqa: E501

        Main defines the main domain name.  # noqa: E501

        :return: The main of this IoTraefikV1alpha1TLSStoreSpecDefaultGeneratedCertDomain.  # noqa: E501
        :rtype: str
        """
        return self._main

    @main.setter
    def main(self, main):
        """Sets the main of this IoTraefikV1alpha1TLSStoreSpecDefaultGeneratedCertDomain.

        Main defines the main domain name.  # noqa: E501

        :param main: The main of this IoTraefikV1alpha1TLSStoreSpecDefaultGeneratedCertDomain.  # noqa: E501
        :type: str
        """

        self._main = main

    @property
    def sans(self):
        """Gets the sans of this IoTraefikV1alpha1TLSStoreSpecDefaultGeneratedCertDomain.  # noqa: E501

        SANs defines the subject alternative domain names.  # noqa: E501

        :return: The sans of this IoTraefikV1alpha1TLSStoreSpecDefaultGeneratedCertDomain.  # noqa: E501
        :rtype: list[str]
        """
        return self._sans

    @sans.setter
    def sans(self, sans):
        """Sets the sans of this IoTraefikV1alpha1TLSStoreSpecDefaultGeneratedCertDomain.

        SANs defines the subject alternative domain names.  # noqa: E501

        :param sans: The sans of this IoTraefikV1alpha1TLSStoreSpecDefaultGeneratedCertDomain.  # noqa: E501
        :type: list[str]
        """

        self._sans = sans

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(IoTraefikV1alpha1TLSStoreSpecDefaultGeneratedCertDomain, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IoTraefikV1alpha1TLSStoreSpecDefaultGeneratedCertDomain):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoTraefikV1alpha1TLSStoreSpecDefaultGeneratedCertDomain):
            return True

        return self.to_dict() != other.to_dict()
