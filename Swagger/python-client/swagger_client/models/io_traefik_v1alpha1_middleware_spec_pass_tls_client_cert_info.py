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


class IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo(object):
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
        'issuer': 'IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer',
        'not_after': 'bool',
        'not_before': 'bool',
        'sans': 'bool',
        'serial_number': 'bool',
        'subject': 'IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoSubject'
    }

    attribute_map = {
        'issuer': 'issuer',
        'not_after': 'notAfter',
        'not_before': 'notBefore',
        'sans': 'sans',
        'serial_number': 'serialNumber',
        'subject': 'subject'
    }

    def __init__(self, issuer=None, not_after=None, not_before=None, sans=None, serial_number=None, subject=None, _configuration=None):  # noqa: E501
        """IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._issuer = None
        self._not_after = None
        self._not_before = None
        self._sans = None
        self._serial_number = None
        self._subject = None
        self.discriminator = None

        if issuer is not None:
            self.issuer = issuer
        if not_after is not None:
            self.not_after = not_after
        if not_before is not None:
            self.not_before = not_before
        if sans is not None:
            self.sans = sans
        if serial_number is not None:
            self.serial_number = serial_number
        if subject is not None:
            self.subject = subject

    @property
    def issuer(self):
        """Gets the issuer of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501


        :return: The issuer of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501
        :rtype: IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.


        :param issuer: The issuer of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501
        :type: IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer
        """

        self._issuer = issuer

    @property
    def not_after(self):
        """Gets the not_after of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501

        NotAfter defines whether to add the Not After information from the Validity part.  # noqa: E501

        :return: The not_after of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501
        :rtype: bool
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.

        NotAfter defines whether to add the Not After information from the Validity part.  # noqa: E501

        :param not_after: The not_after of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501
        :type: bool
        """

        self._not_after = not_after

    @property
    def not_before(self):
        """Gets the not_before of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501

        NotBefore defines whether to add the Not Before information from the Validity part.  # noqa: E501

        :return: The not_before of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501
        :rtype: bool
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.

        NotBefore defines whether to add the Not Before information from the Validity part.  # noqa: E501

        :param not_before: The not_before of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501
        :type: bool
        """

        self._not_before = not_before

    @property
    def sans(self):
        """Gets the sans of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501

        Sans defines whether to add the Subject Alternative Name information from the Subject Alternative Name part.  # noqa: E501

        :return: The sans of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501
        :rtype: bool
        """
        return self._sans

    @sans.setter
    def sans(self, sans):
        """Sets the sans of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.

        Sans defines whether to add the Subject Alternative Name information from the Subject Alternative Name part.  # noqa: E501

        :param sans: The sans of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501
        :type: bool
        """

        self._sans = sans

    @property
    def serial_number(self):
        """Gets the serial_number of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501

        SerialNumber defines whether to add the client serialNumber information.  # noqa: E501

        :return: The serial_number of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501
        :rtype: bool
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.

        SerialNumber defines whether to add the client serialNumber information.  # noqa: E501

        :param serial_number: The serial_number of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501
        :type: bool
        """

        self._serial_number = serial_number

    @property
    def subject(self):
        """Gets the subject of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501


        :return: The subject of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501
        :rtype: IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.


        :param subject: The subject of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo.  # noqa: E501
        :type: IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoSubject
        """

        self._subject = subject

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
        if issubclass(IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo, dict):
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
        if not isinstance(other, IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfo):
            return True

        return self.to_dict() != other.to_dict()
