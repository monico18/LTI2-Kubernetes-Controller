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


class IoTraefikV1alpha1MiddlewareSpecBasicAuth(object):
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
        'header_field': 'str',
        'realm': 'str',
        'remove_header': 'bool',
        'secret': 'str'
    }

    attribute_map = {
        'header_field': 'headerField',
        'realm': 'realm',
        'remove_header': 'removeHeader',
        'secret': 'secret'
    }

    def __init__(self, header_field=None, realm=None, remove_header=None, secret=None, _configuration=None):  # noqa: E501
        """IoTraefikV1alpha1MiddlewareSpecBasicAuth - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._header_field = None
        self._realm = None
        self._remove_header = None
        self._secret = None
        self.discriminator = None

        if header_field is not None:
            self.header_field = header_field
        if realm is not None:
            self.realm = realm
        if remove_header is not None:
            self.remove_header = remove_header
        if secret is not None:
            self.secret = secret

    @property
    def header_field(self):
        """Gets the header_field of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.  # noqa: E501

        HeaderField defines a header field to store the authenticated user. More info: https://doc.traefik.io/traefik/v2.10/middlewares/http/basicauth/#headerfield  # noqa: E501

        :return: The header_field of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.  # noqa: E501
        :rtype: str
        """
        return self._header_field

    @header_field.setter
    def header_field(self, header_field):
        """Sets the header_field of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.

        HeaderField defines a header field to store the authenticated user. More info: https://doc.traefik.io/traefik/v2.10/middlewares/http/basicauth/#headerfield  # noqa: E501

        :param header_field: The header_field of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.  # noqa: E501
        :type: str
        """

        self._header_field = header_field

    @property
    def realm(self):
        """Gets the realm of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.  # noqa: E501

        Realm allows the protected resources on a server to be partitioned into a set of protection spaces, each with its own authentication scheme. Default: traefik.  # noqa: E501

        :return: The realm of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.  # noqa: E501
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.

        Realm allows the protected resources on a server to be partitioned into a set of protection spaces, each with its own authentication scheme. Default: traefik.  # noqa: E501

        :param realm: The realm of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.  # noqa: E501
        :type: str
        """

        self._realm = realm

    @property
    def remove_header(self):
        """Gets the remove_header of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.  # noqa: E501

        RemoveHeader sets the removeHeader option to true to remove the authorization header before forwarding the request to your service. Default: false.  # noqa: E501

        :return: The remove_header of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.  # noqa: E501
        :rtype: bool
        """
        return self._remove_header

    @remove_header.setter
    def remove_header(self, remove_header):
        """Sets the remove_header of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.

        RemoveHeader sets the removeHeader option to true to remove the authorization header before forwarding the request to your service. Default: false.  # noqa: E501

        :param remove_header: The remove_header of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.  # noqa: E501
        :type: bool
        """

        self._remove_header = remove_header

    @property
    def secret(self):
        """Gets the secret of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.  # noqa: E501

        Secret is the name of the referenced Kubernetes Secret containing user credentials.  # noqa: E501

        :return: The secret of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.

        Secret is the name of the referenced Kubernetes Secret containing user credentials.  # noqa: E501

        :param secret: The secret of this IoTraefikV1alpha1MiddlewareSpecBasicAuth.  # noqa: E501
        :type: str
        """

        self._secret = secret

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
        if issubclass(IoTraefikV1alpha1MiddlewareSpecBasicAuth, dict):
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
        if not isinstance(other, IoTraefikV1alpha1MiddlewareSpecBasicAuth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoTraefikV1alpha1MiddlewareSpecBasicAuth):
            return True

        return self.to_dict() != other.to_dict()
