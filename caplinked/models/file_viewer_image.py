# coding: utf-8

"""
    CapLinked API v1.0

    Core information security endpoints for managing files/folders, users/groups, uploads/downloads, and more.

    OpenAPI spec version: 2017-05-23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FileViewerImage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'status': 'str',
        'page_number': 'int',
        'expiring_url': 'str',
        'expiring_thumbnail_url': 'str'
    }

    attribute_map = {
        'status': 'status',
        'page_number': 'page_number',
        'expiring_url': 'expiring_url',
        'expiring_thumbnail_url': 'expiring_thumbnail_url'
    }

    def __init__(self, status=None, page_number=None, expiring_url=None, expiring_thumbnail_url=None):
        """
        FileViewerImage - a model defined in Swagger
        """

        self._status = None
        self._page_number = None
        self._expiring_url = None
        self._expiring_thumbnail_url = None

        if status is not None:
          self.status = status
        if page_number is not None:
          self.page_number = page_number
        if expiring_url is not None:
          self.expiring_url = expiring_url
        if expiring_thumbnail_url is not None:
          self.expiring_thumbnail_url = expiring_thumbnail_url

    @property
    def status(self):
        """
        Gets the status of this FileViewerImage.

        :return: The status of this FileViewerImage.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this FileViewerImage.

        :param status: The status of this FileViewerImage.
        :type: str
        """

        self._status = status

    @property
    def page_number(self):
        """
        Gets the page_number of this FileViewerImage.

        :return: The page_number of this FileViewerImage.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """
        Sets the page_number of this FileViewerImage.

        :param page_number: The page_number of this FileViewerImage.
        :type: int
        """

        self._page_number = page_number

    @property
    def expiring_url(self):
        """
        Gets the expiring_url of this FileViewerImage.

        :return: The expiring_url of this FileViewerImage.
        :rtype: str
        """
        return self._expiring_url

    @expiring_url.setter
    def expiring_url(self, expiring_url):
        """
        Sets the expiring_url of this FileViewerImage.

        :param expiring_url: The expiring_url of this FileViewerImage.
        :type: str
        """

        self._expiring_url = expiring_url

    @property
    def expiring_thumbnail_url(self):
        """
        Gets the expiring_thumbnail_url of this FileViewerImage.

        :return: The expiring_thumbnail_url of this FileViewerImage.
        :rtype: str
        """
        return self._expiring_thumbnail_url

    @expiring_thumbnail_url.setter
    def expiring_thumbnail_url(self, expiring_thumbnail_url):
        """
        Sets the expiring_thumbnail_url of this FileViewerImage.

        :param expiring_thumbnail_url: The expiring_thumbnail_url of this FileViewerImage.
        :type: str
        """

        self._expiring_thumbnail_url = expiring_thumbnail_url

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
        if not isinstance(other, FileViewerImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
