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


class IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec(object):
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
        'exempt': 'IoK8sApiFlowcontrolV1beta3ExemptPriorityLevelConfiguration',
        'limited': 'IoK8sApiFlowcontrolV1beta3LimitedPriorityLevelConfiguration',
        'type': 'str'
    }

    attribute_map = {
        'exempt': 'exempt',
        'limited': 'limited',
        'type': 'type'
    }

    def __init__(self, exempt=None, limited=None, type=None, _configuration=None):  # noqa: E501
        """IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._exempt = None
        self._limited = None
        self._type = None
        self.discriminator = None

        if exempt is not None:
            self.exempt = exempt
        if limited is not None:
            self.limited = limited
        self.type = type

    @property
    def exempt(self):
        """Gets the exempt of this IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec.  # noqa: E501

        `exempt` specifies how requests are handled for an exempt priority level. This field MUST be empty if `type` is `\"Limited\"`. This field MAY be non-empty if `type` is `\"Exempt\"`. If empty and `type` is `\"Exempt\"` then the default values for `ExemptPriorityLevelConfiguration` apply.  # noqa: E501

        :return: The exempt of this IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec.  # noqa: E501
        :rtype: IoK8sApiFlowcontrolV1beta3ExemptPriorityLevelConfiguration
        """
        return self._exempt

    @exempt.setter
    def exempt(self, exempt):
        """Sets the exempt of this IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec.

        `exempt` specifies how requests are handled for an exempt priority level. This field MUST be empty if `type` is `\"Limited\"`. This field MAY be non-empty if `type` is `\"Exempt\"`. If empty and `type` is `\"Exempt\"` then the default values for `ExemptPriorityLevelConfiguration` apply.  # noqa: E501

        :param exempt: The exempt of this IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec.  # noqa: E501
        :type: IoK8sApiFlowcontrolV1beta3ExemptPriorityLevelConfiguration
        """

        self._exempt = exempt

    @property
    def limited(self):
        """Gets the limited of this IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec.  # noqa: E501

        `limited` specifies how requests are handled for a Limited priority level. This field must be non-empty if and only if `type` is `\"Limited\"`.  # noqa: E501

        :return: The limited of this IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec.  # noqa: E501
        :rtype: IoK8sApiFlowcontrolV1beta3LimitedPriorityLevelConfiguration
        """
        return self._limited

    @limited.setter
    def limited(self, limited):
        """Sets the limited of this IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec.

        `limited` specifies how requests are handled for a Limited priority level. This field must be non-empty if and only if `type` is `\"Limited\"`.  # noqa: E501

        :param limited: The limited of this IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec.  # noqa: E501
        :type: IoK8sApiFlowcontrolV1beta3LimitedPriorityLevelConfiguration
        """

        self._limited = limited

    @property
    def type(self):
        """Gets the type of this IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec.  # noqa: E501

        `type` indicates whether this priority level is subject to limitation on request execution.  A value of `\"Exempt\"` means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels.  A value of `\"Limited\"` means that (a) requests of this priority level _are_ subject to limits and (b) some of the server's limited capacity is made available exclusively to this priority level. Required.  # noqa: E501

        :return: The type of this IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec.

        `type` indicates whether this priority level is subject to limitation on request execution.  A value of `\"Exempt\"` means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels.  A value of `\"Limited\"` means that (a) requests of this priority level _are_ subject to limits and (b) some of the server's limited capacity is made available exclusively to this priority level. Required.  # noqa: E501

        :param type: The type of this IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec, dict):
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
        if not isinstance(other, IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiFlowcontrolV1beta3PriorityLevelConfigurationSpec):
            return True

        return self.to_dict() != other.to_dict()
