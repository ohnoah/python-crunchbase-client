# coding: utf-8

"""
    Crunchbase Enterprise API

    Crunchbase Enterprise API, 2021-07-16  # noqa: E501

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Ownership(object):
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
        'created_at': 'datetime',
        'entity_def_id': 'str',
        'identifier': 'AllOfOwnershipIdentifier',
        'name': 'str',
        'ownee_identifier': 'AllOfOwnershipOwneeIdentifier',
        'owner_identifier': 'AllOfOwnershipOwnerIdentifier',
        'ownership_type': 'str',
        'permalink': 'str',
        'updated_at': 'datetime',
        'uuid': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'entity_def_id': 'entity_def_id',
        'identifier': 'identifier',
        'name': 'name',
        'ownee_identifier': 'ownee_identifier',
        'owner_identifier': 'owner_identifier',
        'ownership_type': 'ownership_type',
        'permalink': 'permalink',
        'updated_at': 'updated_at',
        'uuid': 'uuid'
    }

    def __init__(self, created_at=None, entity_def_id=None, identifier=None, name=None, ownee_identifier=None, owner_identifier=None, ownership_type=None, permalink=None, updated_at=None, uuid=None):  # noqa: E501
        """Ownership - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._entity_def_id = None
        self._identifier = None
        self._name = None
        self._ownee_identifier = None
        self._owner_identifier = None
        self._ownership_type = None
        self._permalink = None
        self._updated_at = None
        self._uuid = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if entity_def_id is not None:
            self.entity_def_id = entity_def_id
        self.identifier = identifier
        if name is not None:
            self.name = name
        if ownee_identifier is not None:
            self.ownee_identifier = ownee_identifier
        if owner_identifier is not None:
            self.owner_identifier = owner_identifier
        if ownership_type is not None:
            self.ownership_type = ownership_type
        if permalink is not None:
            self.permalink = permalink
        if updated_at is not None:
            self.updated_at = updated_at
        if uuid is not None:
            self.uuid = uuid

    @property
    def created_at(self):
        """Gets the created_at of this Ownership.  # noqa: E501

        Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :return: The created_at of this Ownership.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Ownership.

        Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :param created_at: The created_at of this Ownership.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def entity_def_id(self):
        """Gets the entity_def_id of this Ownership.  # noqa: E501

        Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * ownership - Ownership   # noqa: E501

        :return: The entity_def_id of this Ownership.  # noqa: E501
        :rtype: str
        """
        return self._entity_def_id

    @entity_def_id.setter
    def entity_def_id(self, entity_def_id):
        """Sets the entity_def_id of this Ownership.

        Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * ownership - Ownership   # noqa: E501

        :param entity_def_id: The entity_def_id of this Ownership.  # noqa: E501
        :type: str
        """

        self._entity_def_id = entity_def_id

    @property
    def identifier(self):
        """Gets the identifier of this Ownership.  # noqa: E501

        Short description of the ownership (e.g. Google owns YouTube)\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :return: The identifier of this Ownership.  # noqa: E501
        :rtype: AllOfOwnershipIdentifier
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Ownership.

        Short description of the ownership (e.g. Google owns YouTube)\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :param identifier: The identifier of this Ownership.  # noqa: E501
        :type: AllOfOwnershipIdentifier
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this Ownership.  # noqa: E501

        Field Type: text_blob\\ Searchable: No   # noqa: E501

        :return: The name of this Ownership.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Ownership.

        Field Type: text_blob\\ Searchable: No   # noqa: E501

        :param name: The name of this Ownership.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ownee_identifier(self):
        """Gets the ownee_identifier of this Ownership.  # noqa: E501

        Name of the sub-organization that is related to a parent organization\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :return: The ownee_identifier of this Ownership.  # noqa: E501
        :rtype: AllOfOwnershipOwneeIdentifier
        """
        return self._ownee_identifier

    @ownee_identifier.setter
    def ownee_identifier(self, ownee_identifier):
        """Sets the ownee_identifier of this Ownership.

        Name of the sub-organization that is related to a parent organization\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :param ownee_identifier: The ownee_identifier of this Ownership.  # noqa: E501
        :type: AllOfOwnershipOwneeIdentifier
        """

        self._ownee_identifier = ownee_identifier

    @property
    def owner_identifier(self):
        """Gets the owner_identifier of this Ownership.  # noqa: E501

        Name of the organization that has sub-organizations\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :return: The owner_identifier of this Ownership.  # noqa: E501
        :rtype: AllOfOwnershipOwnerIdentifier
        """
        return self._owner_identifier

    @owner_identifier.setter
    def owner_identifier(self, owner_identifier):
        """Sets the owner_identifier of this Ownership.

        Name of the organization that has sub-organizations\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :param owner_identifier: The owner_identifier of this Ownership.  # noqa: E501
        :type: AllOfOwnershipOwnerIdentifier
        """

        self._owner_identifier = owner_identifier

    @property
    def ownership_type(self):
        """Gets the ownership_type of this Ownership.  # noqa: E501

        This is the relationship defining how a sub-organization is related to a parent organization\\ Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * affiliated_company - Affiliated Company  * division - Division  * investment_arm - Investment Arm  * joint_venture - Joint Venture  * subsidiary - Subsidiary   # noqa: E501

        :return: The ownership_type of this Ownership.  # noqa: E501
        :rtype: str
        """
        return self._ownership_type

    @ownership_type.setter
    def ownership_type(self, ownership_type):
        """Sets the ownership_type of this Ownership.

        This is the relationship defining how a sub-organization is related to a parent organization\\ Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * affiliated_company - Affiliated Company  * division - Division  * investment_arm - Investment Arm  * joint_venture - Joint Venture  * subsidiary - Subsidiary   # noqa: E501

        :param ownership_type: The ownership_type of this Ownership.  # noqa: E501
        :type: str
        """

        self._ownership_type = ownership_type

    @property
    def permalink(self):
        """Gets the permalink of this Ownership.  # noqa: E501

        Field Type: permalink\\ Searchable: No   # noqa: E501

        :return: The permalink of this Ownership.  # noqa: E501
        :rtype: str
        """
        return self._permalink

    @permalink.setter
    def permalink(self, permalink):
        """Sets the permalink of this Ownership.

        Field Type: permalink\\ Searchable: No   # noqa: E501

        :param permalink: The permalink of this Ownership.  # noqa: E501
        :type: str
        """

        self._permalink = permalink

    @property
    def updated_at(self):
        """Gets the updated_at of this Ownership.  # noqa: E501

        Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :return: The updated_at of this Ownership.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Ownership.

        Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :param updated_at: The updated_at of this Ownership.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def uuid(self):
        """Gets the uuid of this Ownership.  # noqa: E501

        Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes   # noqa: E501

        :return: The uuid of this Ownership.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Ownership.

        Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes   # noqa: E501

        :param uuid: The uuid of this Ownership.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(Ownership, dict):
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
        if not isinstance(other, Ownership):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
