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


class IoTraefikV1alpha1MiddlewareSpecInFlightReq(object):
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
        'amount': 'int',
        'source_criterion': 'IoTraefikV1alpha1MiddlewareSpecInFlightReqSourceCriterion'
    }

    attribute_map = {
        'amount': 'amount',
        'source_criterion': 'sourceCriterion'
    }

    def __init__(self, amount=None, source_criterion=None, _configuration=None):  # noqa: E501
        """IoTraefikV1alpha1MiddlewareSpecInFlightReq - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount = None
        self._source_criterion = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if source_criterion is not None:
            self.source_criterion = source_criterion

    @property
    def amount(self):
        """Gets the amount of this IoTraefikV1alpha1MiddlewareSpecInFlightReq.  # noqa: E501

        Amount defines the maximum amount of allowed simultaneous in-flight request. The middleware responds with HTTP 429 Too Many Requests if there are already amount requests in progress (based on the same sourceCriterion strategy).  # noqa: E501

        :return: The amount of this IoTraefikV1alpha1MiddlewareSpecInFlightReq.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this IoTraefikV1alpha1MiddlewareSpecInFlightReq.

        Amount defines the maximum amount of allowed simultaneous in-flight request. The middleware responds with HTTP 429 Too Many Requests if there are already amount requests in progress (based on the same sourceCriterion strategy).  # noqa: E501

        :param amount: The amount of this IoTraefikV1alpha1MiddlewareSpecInFlightReq.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def source_criterion(self):
        """Gets the source_criterion of this IoTraefikV1alpha1MiddlewareSpecInFlightReq.  # noqa: E501


        :return: The source_criterion of this IoTraefikV1alpha1MiddlewareSpecInFlightReq.  # noqa: E501
        :rtype: IoTraefikV1alpha1MiddlewareSpecInFlightReqSourceCriterion
        """
        return self._source_criterion

    @source_criterion.setter
    def source_criterion(self, source_criterion):
        """Sets the source_criterion of this IoTraefikV1alpha1MiddlewareSpecInFlightReq.


        :param source_criterion: The source_criterion of this IoTraefikV1alpha1MiddlewareSpecInFlightReq.  # noqa: E501
        :type: IoTraefikV1alpha1MiddlewareSpecInFlightReqSourceCriterion
        """

        self._source_criterion = source_criterion

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
        if issubclass(IoTraefikV1alpha1MiddlewareSpecInFlightReq, dict):
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
        if not isinstance(other, IoTraefikV1alpha1MiddlewareSpecInFlightReq):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoTraefikV1alpha1MiddlewareSpecInFlightReq):
            return True

        return self.to_dict() != other.to_dict()
