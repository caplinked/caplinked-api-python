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


class FolderList(object):
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
        'id': 'int',
        'id_tree': 'int',
        'name': 'str',
        'view': 'bool',
        'download': 'bool',
        'upload': 'bool',
        'position': 'int',
        'index': 'int',
        'is_mixed_view': 'bool',
        'is_mixed_download': 'bool',
        'is_mixed_upload': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'id_tree': 'id_tree',
        'name': 'name',
        'view': 'view',
        'download': 'download',
        'upload': 'upload',
        'position': 'position',
        'index': 'index',
        'is_mixed_view': 'is_mixed_view',
        'is_mixed_download': 'is_mixed_download',
        'is_mixed_upload': 'is_mixed_upload'
    }

    def __init__(self, id=None, id_tree=None, name=None, view=None, download=None, upload=None, position=None, index=None, is_mixed_view=None, is_mixed_download=None, is_mixed_upload=None):
        """
        FolderList - a model defined in Swagger
        """

        self._id = None
        self._id_tree = None
        self._name = None
        self._view = None
        self._download = None
        self._upload = None
        self._position = None
        self._index = None
        self._is_mixed_view = None
        self._is_mixed_download = None
        self._is_mixed_upload = None

        if id is not None:
          self.id = id
        if id_tree is not None:
          self.id_tree = id_tree
        if name is not None:
          self.name = name
        if view is not None:
          self.view = view
        if download is not None:
          self.download = download
        if upload is not None:
          self.upload = upload
        if position is not None:
          self.position = position
        if index is not None:
          self.index = index
        if is_mixed_view is not None:
          self.is_mixed_view = is_mixed_view
        if is_mixed_download is not None:
          self.is_mixed_download = is_mixed_download
        if is_mixed_upload is not None:
          self.is_mixed_upload = is_mixed_upload

    @property
    def id(self):
        """
        Gets the id of this FolderList.

        :return: The id of this FolderList.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FolderList.

        :param id: The id of this FolderList.
        :type: int
        """

        self._id = id

    @property
    def id_tree(self):
        """
        Gets the id_tree of this FolderList.

        :return: The id_tree of this FolderList.
        :rtype: int
        """
        return self._id_tree

    @id_tree.setter
    def id_tree(self, id_tree):
        """
        Sets the id_tree of this FolderList.

        :param id_tree: The id_tree of this FolderList.
        :type: int
        """

        self._id_tree = id_tree

    @property
    def name(self):
        """
        Gets the name of this FolderList.

        :return: The name of this FolderList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FolderList.

        :param name: The name of this FolderList.
        :type: str
        """

        self._name = name

    @property
    def view(self):
        """
        Gets the view of this FolderList.

        :return: The view of this FolderList.
        :rtype: bool
        """
        return self._view

    @view.setter
    def view(self, view):
        """
        Sets the view of this FolderList.

        :param view: The view of this FolderList.
        :type: bool
        """

        self._view = view

    @property
    def download(self):
        """
        Gets the download of this FolderList.

        :return: The download of this FolderList.
        :rtype: bool
        """
        return self._download

    @download.setter
    def download(self, download):
        """
        Sets the download of this FolderList.

        :param download: The download of this FolderList.
        :type: bool
        """

        self._download = download

    @property
    def upload(self):
        """
        Gets the upload of this FolderList.

        :return: The upload of this FolderList.
        :rtype: bool
        """
        return self._upload

    @upload.setter
    def upload(self, upload):
        """
        Sets the upload of this FolderList.

        :param upload: The upload of this FolderList.
        :type: bool
        """

        self._upload = upload

    @property
    def position(self):
        """
        Gets the position of this FolderList.

        :return: The position of this FolderList.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this FolderList.

        :param position: The position of this FolderList.
        :type: int
        """

        self._position = position

    @property
    def index(self):
        """
        Gets the index of this FolderList.

        :return: The index of this FolderList.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this FolderList.

        :param index: The index of this FolderList.
        :type: int
        """

        self._index = index

    @property
    def is_mixed_view(self):
        """
        Gets the is_mixed_view of this FolderList.

        :return: The is_mixed_view of this FolderList.
        :rtype: bool
        """
        return self._is_mixed_view

    @is_mixed_view.setter
    def is_mixed_view(self, is_mixed_view):
        """
        Sets the is_mixed_view of this FolderList.

        :param is_mixed_view: The is_mixed_view of this FolderList.
        :type: bool
        """

        self._is_mixed_view = is_mixed_view

    @property
    def is_mixed_download(self):
        """
        Gets the is_mixed_download of this FolderList.

        :return: The is_mixed_download of this FolderList.
        :rtype: bool
        """
        return self._is_mixed_download

    @is_mixed_download.setter
    def is_mixed_download(self, is_mixed_download):
        """
        Sets the is_mixed_download of this FolderList.

        :param is_mixed_download: The is_mixed_download of this FolderList.
        :type: bool
        """

        self._is_mixed_download = is_mixed_download

    @property
    def is_mixed_upload(self):
        """
        Gets the is_mixed_upload of this FolderList.

        :return: The is_mixed_upload of this FolderList.
        :rtype: bool
        """
        return self._is_mixed_upload

    @is_mixed_upload.setter
    def is_mixed_upload(self, is_mixed_upload):
        """
        Sets the is_mixed_upload of this FolderList.

        :param is_mixed_upload: The is_mixed_upload of this FolderList.
        :type: bool
        """

        self._is_mixed_upload = is_mixed_upload

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
        if not isinstance(other, FolderList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other