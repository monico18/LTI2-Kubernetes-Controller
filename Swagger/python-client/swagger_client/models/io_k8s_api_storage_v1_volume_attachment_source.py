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


class IoK8sApiStorageV1VolumeAttachmentSource(object):
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
        'inline_volume_spec': 'IoK8sApiCoreV1PersistentVolumeSpec',
        'persistent_volume_name': 'str'
    }

    attribute_map = {
        'inline_volume_spec': 'inlineVolumeSpec',
        'persistent_volume_name': 'persistentVolumeName'
    }

    def __init__(self, inline_volume_spec=None, persistent_volume_name=None, _configuration=None):  # noqa: E501
        """IoK8sApiStorageV1VolumeAttachmentSource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._inline_volume_spec = None
        self._persistent_volume_name = None
        self.discriminator = None

        if inline_volume_spec is not None:
            self.inline_volume_spec = inline_volume_spec
        if persistent_volume_name is not None:
            self.persistent_volume_name = persistent_volume_name

    @property
    def inline_volume_spec(self):
        """Gets the inline_volume_spec of this IoK8sApiStorageV1VolumeAttachmentSource.  # noqa: E501

        inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is beta-level and is only honored by servers that enabled the CSIMigration feature.  # noqa: E501

        :return: The inline_volume_spec of this IoK8sApiStorageV1VolumeAttachmentSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1PersistentVolumeSpec
        """
        return self._inline_volume_spec

    @inline_volume_spec.setter
    def inline_volume_spec(self, inline_volume_spec):
        """Sets the inline_volume_spec of this IoK8sApiStorageV1VolumeAttachmentSource.

        inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is beta-level and is only honored by servers that enabled the CSIMigration feature.  # noqa: E501

        :param inline_volume_spec: The inline_volume_spec of this IoK8sApiStorageV1VolumeAttachmentSource.  # noqa: E501
        :type: IoK8sApiCoreV1PersistentVolumeSpec
        """

        self._inline_volume_spec = inline_volume_spec

    @property
    def persistent_volume_name(self):
        """Gets the persistent_volume_name of this IoK8sApiStorageV1VolumeAttachmentSource.  # noqa: E501

        persistentVolumeName represents the name of the persistent volume to attach.  # noqa: E501

        :return: The persistent_volume_name of this IoK8sApiStorageV1VolumeAttachmentSource.  # noqa: E501
        :rtype: str
        """
        return self._persistent_volume_name

    @persistent_volume_name.setter
    def persistent_volume_name(self, persistent_volume_name):
        """Sets the persistent_volume_name of this IoK8sApiStorageV1VolumeAttachmentSource.

        persistentVolumeName represents the name of the persistent volume to attach.  # noqa: E501

        :param persistent_volume_name: The persistent_volume_name of this IoK8sApiStorageV1VolumeAttachmentSource.  # noqa: E501
        :type: str
        """

        self._persistent_volume_name = persistent_volume_name

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
        if issubclass(IoK8sApiStorageV1VolumeAttachmentSource, dict):
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
        if not isinstance(other, IoK8sApiStorageV1VolumeAttachmentSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiStorageV1VolumeAttachmentSource):
            return True

        return self.to_dict() != other.to_dict()
