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


class IoK8sApiFlowcontrolV1FlowSchemaCondition(object):
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
        'last_transition_time': 'IoK8sApimachineryPkgApisMetaV1Time',
        'message': 'str',
        'reason': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'last_transition_time': 'lastTransitionTime',
        'message': 'message',
        'reason': 'reason',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, last_transition_time=None, message=None, reason=None, status=None, type=None, _configuration=None):  # noqa: E501
        """IoK8sApiFlowcontrolV1FlowSchemaCondition - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._last_transition_time = None
        self._message = None
        self._reason = None
        self._status = None
        self._type = None
        self.discriminator = None

        if last_transition_time is not None:
            self.last_transition_time = last_transition_time
        if message is not None:
            self.message = message
        if reason is not None:
            self.reason = reason
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def last_transition_time(self):
        """Gets the last_transition_time of this IoK8sApiFlowcontrolV1FlowSchemaCondition.  # noqa: E501

        `lastTransitionTime` is the last time the condition transitioned from one status to another.  # noqa: E501

        :return: The last_transition_time of this IoK8sApiFlowcontrolV1FlowSchemaCondition.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time):
        """Sets the last_transition_time of this IoK8sApiFlowcontrolV1FlowSchemaCondition.

        `lastTransitionTime` is the last time the condition transitioned from one status to another.  # noqa: E501

        :param last_transition_time: The last_transition_time of this IoK8sApiFlowcontrolV1FlowSchemaCondition.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._last_transition_time = last_transition_time

    @property
    def message(self):
        """Gets the message of this IoK8sApiFlowcontrolV1FlowSchemaCondition.  # noqa: E501

        `message` is a human-readable message indicating details about last transition.  # noqa: E501

        :return: The message of this IoK8sApiFlowcontrolV1FlowSchemaCondition.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this IoK8sApiFlowcontrolV1FlowSchemaCondition.

        `message` is a human-readable message indicating details about last transition.  # noqa: E501

        :param message: The message of this IoK8sApiFlowcontrolV1FlowSchemaCondition.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def reason(self):
        """Gets the reason of this IoK8sApiFlowcontrolV1FlowSchemaCondition.  # noqa: E501

        `reason` is a unique, one-word, CamelCase reason for the condition's last transition.  # noqa: E501

        :return: The reason of this IoK8sApiFlowcontrolV1FlowSchemaCondition.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this IoK8sApiFlowcontrolV1FlowSchemaCondition.

        `reason` is a unique, one-word, CamelCase reason for the condition's last transition.  # noqa: E501

        :param reason: The reason of this IoK8sApiFlowcontrolV1FlowSchemaCondition.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def status(self):
        """Gets the status of this IoK8sApiFlowcontrolV1FlowSchemaCondition.  # noqa: E501

        `status` is the status of the condition. Can be True, False, Unknown. Required.  # noqa: E501

        :return: The status of this IoK8sApiFlowcontrolV1FlowSchemaCondition.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IoK8sApiFlowcontrolV1FlowSchemaCondition.

        `status` is the status of the condition. Can be True, False, Unknown. Required.  # noqa: E501

        :param status: The status of this IoK8sApiFlowcontrolV1FlowSchemaCondition.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this IoK8sApiFlowcontrolV1FlowSchemaCondition.  # noqa: E501

        `type` is the type of the condition. Required.  # noqa: E501

        :return: The type of this IoK8sApiFlowcontrolV1FlowSchemaCondition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoK8sApiFlowcontrolV1FlowSchemaCondition.

        `type` is the type of the condition. Required.  # noqa: E501

        :param type: The type of this IoK8sApiFlowcontrolV1FlowSchemaCondition.  # noqa: E501
        :type: str
        """

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
        if issubclass(IoK8sApiFlowcontrolV1FlowSchemaCondition, dict):
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
        if not isinstance(other, IoK8sApiFlowcontrolV1FlowSchemaCondition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiFlowcontrolV1FlowSchemaCondition):
            return True

        return self.to_dict() != other.to_dict()
