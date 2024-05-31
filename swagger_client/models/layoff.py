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

class Layoff(object):
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
        'identifier': 'EntityIdentifier',
        'key_event_date': 'date',
        'organization_identifier': 'AllOfLayoffOrganizationIdentifier',
        'updated_at': 'datetime',
        'uuid': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'entity_def_id': 'entity_def_id',
        'identifier': 'identifier',
        'key_event_date': 'key_event_date',
        'organization_identifier': 'organization_identifier',
        'updated_at': 'updated_at',
        'uuid': 'uuid'
    }

    def __init__(self, created_at=None, entity_def_id=None, identifier=None, key_event_date=None, organization_identifier=None, updated_at=None, uuid=None):  # noqa: E501
        """Layoff - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._entity_def_id = None
        self._identifier = None
        self._key_event_date = None
        self._organization_identifier = None
        self._updated_at = None
        self._uuid = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if entity_def_id is not None:
            self.entity_def_id = entity_def_id
        self.identifier = identifier
        if key_event_date is not None:
            self.key_event_date = key_event_date
        if organization_identifier is not None:
            self.organization_identifier = organization_identifier
        if updated_at is not None:
            self.updated_at = updated_at
        if uuid is not None:
            self.uuid = uuid

    @property
    def created_at(self):
        """Gets the created_at of this Layoff.  # noqa: E501

        Laoyff entity creation date\\ Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :return: The created_at of this Layoff.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Layoff.

        Laoyff entity creation date\\ Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :param created_at: The created_at of this Layoff.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def entity_def_id(self):
        """Gets the entity_def_id of this Layoff.  # noqa: E501

        Layoff Signal\\ Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * layoff - layoff   # noqa: E501

        :return: The entity_def_id of this Layoff.  # noqa: E501
        :rtype: str
        """
        return self._entity_def_id

    @entity_def_id.setter
    def entity_def_id(self, entity_def_id):
        """Sets the entity_def_id of this Layoff.

        Layoff Signal\\ Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * layoff - layoff   # noqa: E501

        :param entity_def_id: The entity_def_id of this Layoff.  # noqa: E501
        :type: str
        """

        self._entity_def_id = entity_def_id

    @property
    def identifier(self):
        """Gets the identifier of this Layoff.  # noqa: E501


        :return: The identifier of this Layoff.  # noqa: E501
        :rtype: EntityIdentifier
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Layoff.


        :param identifier: The identifier of this Layoff.  # noqa: E501
        :type: EntityIdentifier
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def key_event_date(self):
        """Gets the key_event_date of this Layoff.  # noqa: E501

        Date when the news article was posted\\ Field Type: date\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :return: The key_event_date of this Layoff.  # noqa: E501
        :rtype: date
        """
        return self._key_event_date

    @key_event_date.setter
    def key_event_date(self, key_event_date):
        """Sets the key_event_date of this Layoff.

        Date when the news article was posted\\ Field Type: date\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :param key_event_date: The key_event_date of this Layoff.  # noqa: E501
        :type: date
        """

        self._key_event_date = key_event_date

    @property
    def organization_identifier(self):
        """Gets the organization_identifier of this Layoff.  # noqa: E501

        Organization that had a layoff mentioned\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :return: The organization_identifier of this Layoff.  # noqa: E501
        :rtype: AllOfLayoffOrganizationIdentifier
        """
        return self._organization_identifier

    @organization_identifier.setter
    def organization_identifier(self, organization_identifier):
        """Sets the organization_identifier of this Layoff.

        Organization that had a layoff mentioned\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :param organization_identifier: The organization_identifier of this Layoff.  # noqa: E501
        :type: AllOfLayoffOrganizationIdentifier
        """

        self._organization_identifier = organization_identifier

    @property
    def updated_at(self):
        """Gets the updated_at of this Layoff.  # noqa: E501

        Entity Updating date\\ Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :return: The updated_at of this Layoff.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Layoff.

        Entity Updating date\\ Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :param updated_at: The updated_at of this Layoff.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def uuid(self):
        """Gets the uuid of this Layoff.  # noqa: E501

        Entity UUID\\ Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes   # noqa: E501

        :return: The uuid of this Layoff.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Layoff.

        Entity UUID\\ Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes   # noqa: E501

        :param uuid: The uuid of this Layoff.  # noqa: E501
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
        if issubclass(Layoff, dict):
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
        if not isinstance(other, Layoff):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
