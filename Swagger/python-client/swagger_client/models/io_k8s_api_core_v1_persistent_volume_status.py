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


class IoK8sApiCoreV1PersistentVolumeStatus(object):
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
        'last_phase_transition_time': 'IoK8sApimachineryPkgApisMetaV1Time',
        'message': 'str',
        'phase': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'last_phase_transition_time': 'lastPhaseTransitionTime',
        'message': 'message',
        'phase': 'phase',
        'reason': 'reason'
    }

    def __init__(self, last_phase_transition_time=None, message=None, phase=None, reason=None, _configuration=None):  # noqa: E501
        """IoK8sApiCoreV1PersistentVolumeStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._last_phase_transition_time = None
        self._message = None
        self._phase = None
        self._reason = None
        self.discriminator = None

        if last_phase_transition_time is not None:
            self.last_phase_transition_time = last_phase_transition_time
        if message is not None:
            self.message = message
        if phase is not None:
            self.phase = phase
        if reason is not None:
            self.reason = reason

    @property
    def last_phase_transition_time(self):
        """Gets the last_phase_transition_time of this IoK8sApiCoreV1PersistentVolumeStatus.  # noqa: E501

        lastPhaseTransitionTime is the time the phase transitioned from one to another and automatically resets to current time everytime a volume phase transitions. This is a beta field and requires the PersistentVolumeLastPhaseTransitionTime feature to be enabled (enabled by default).  # noqa: E501

        :return: The last_phase_transition_time of this IoK8sApiCoreV1PersistentVolumeStatus.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._last_phase_transition_time

    @last_phase_transition_time.setter
    def last_phase_transition_time(self, last_phase_transition_time):
        """Sets the last_phase_transition_time of this IoK8sApiCoreV1PersistentVolumeStatus.

        lastPhaseTransitionTime is the time the phase transitioned from one to another and automatically resets to current time everytime a volume phase transitions. This is a beta field and requires the PersistentVolumeLastPhaseTransitionTime feature to be enabled (enabled by default).  # noqa: E501

        :param last_phase_transition_time: The last_phase_transition_time of this IoK8sApiCoreV1PersistentVolumeStatus.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._last_phase_transition_time = last_phase_transition_time

    @property
    def message(self):
        """Gets the message of this IoK8sApiCoreV1PersistentVolumeStatus.  # noqa: E501

        message is a human-readable message indicating details about why the volume is in this state.  # noqa: E501

        :return: The message of this IoK8sApiCoreV1PersistentVolumeStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this IoK8sApiCoreV1PersistentVolumeStatus.

        message is a human-readable message indicating details about why the volume is in this state.  # noqa: E501

        :param message: The message of this IoK8sApiCoreV1PersistentVolumeStatus.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def phase(self):
        """Gets the phase of this IoK8sApiCoreV1PersistentVolumeStatus.  # noqa: E501

        phase indicates if a volume is available, bound to a claim, or released by a claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase  Possible enum values:  - `\"Available\"` used for PersistentVolumes that are not yet bound Available volumes are held by the binder and matched to PersistentVolumeClaims  - `\"Bound\"` used for PersistentVolumes that are bound  - `\"Failed\"` used for PersistentVolumes that failed to be correctly recycled or deleted after being released from a claim  - `\"Pending\"` used for PersistentVolumes that are not available  - `\"Released\"` used for PersistentVolumes where the bound PersistentVolumeClaim was deleted released volumes must be recycled before becoming available again this phase is used by the persistent volume claim binder to signal to another process to reclaim the resource  # noqa: E501

        :return: The phase of this IoK8sApiCoreV1PersistentVolumeStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this IoK8sApiCoreV1PersistentVolumeStatus.

        phase indicates if a volume is available, bound to a claim, or released by a claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase  Possible enum values:  - `\"Available\"` used for PersistentVolumes that are not yet bound Available volumes are held by the binder and matched to PersistentVolumeClaims  - `\"Bound\"` used for PersistentVolumes that are bound  - `\"Failed\"` used for PersistentVolumes that failed to be correctly recycled or deleted after being released from a claim  - `\"Pending\"` used for PersistentVolumes that are not available  - `\"Released\"` used for PersistentVolumes where the bound PersistentVolumeClaim was deleted released volumes must be recycled before becoming available again this phase is used by the persistent volume claim binder to signal to another process to reclaim the resource  # noqa: E501

        :param phase: The phase of this IoK8sApiCoreV1PersistentVolumeStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["Available", "Bound", "Failed", "Pending", "Released"]  # noqa: E501
        if (self._configuration.client_side_validation and
                phase not in allowed_values):
            raise ValueError(
                "Invalid value for `phase` ({0}), must be one of {1}"  # noqa: E501
                .format(phase, allowed_values)
            )

        self._phase = phase

    @property
    def reason(self):
        """Gets the reason of this IoK8sApiCoreV1PersistentVolumeStatus.  # noqa: E501

        reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI.  # noqa: E501

        :return: The reason of this IoK8sApiCoreV1PersistentVolumeStatus.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this IoK8sApiCoreV1PersistentVolumeStatus.

        reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI.  # noqa: E501

        :param reason: The reason of this IoK8sApiCoreV1PersistentVolumeStatus.  # noqa: E501
        :type: str
        """

        self._reason = reason

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
        if issubclass(IoK8sApiCoreV1PersistentVolumeStatus, dict):
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
        if not isinstance(other, IoK8sApiCoreV1PersistentVolumeStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiCoreV1PersistentVolumeStatus):
            return True

        return self.to_dict() != other.to_dict()
