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

class Fund(object):
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
        'announced_on': 'date',
        'created_at': 'datetime',
        'entity_def_id': 'str',
        'identifier': 'AllOfFundIdentifier',
        'image_id': 'str',
        'investor_identifiers': 'list[EntityIdentifier]',
        'money_raised': 'AllOfFundMoneyRaised',
        'name': 'str',
        'num_investors': 'float',
        'owner_identifier': 'AllOfFundOwnerIdentifier',
        'permalink': 'str',
        'short_description': 'str',
        'started_on': 'AllOfFundStartedOn',
        'updated_at': 'datetime',
        'uuid': 'str'
    }

    attribute_map = {
        'announced_on': 'announced_on',
        'created_at': 'created_at',
        'entity_def_id': 'entity_def_id',
        'identifier': 'identifier',
        'image_id': 'image_id',
        'investor_identifiers': 'investor_identifiers',
        'money_raised': 'money_raised',
        'name': 'name',
        'num_investors': 'num_investors',
        'owner_identifier': 'owner_identifier',
        'permalink': 'permalink',
        'short_description': 'short_description',
        'started_on': 'started_on',
        'updated_at': 'updated_at',
        'uuid': 'uuid'
    }

    def __init__(self, announced_on=None, created_at=None, entity_def_id=None, identifier=None, image_id=None, investor_identifiers=None, money_raised=None, name=None, num_investors=None, owner_identifier=None, permalink=None, short_description=None, started_on=None, updated_at=None, uuid=None):  # noqa: E501
        """Fund - a model defined in Swagger"""  # noqa: E501
        self._announced_on = None
        self._created_at = None
        self._entity_def_id = None
        self._identifier = None
        self._image_id = None
        self._investor_identifiers = None
        self._money_raised = None
        self._name = None
        self._num_investors = None
        self._owner_identifier = None
        self._permalink = None
        self._short_description = None
        self._started_on = None
        self._updated_at = None
        self._uuid = None
        self.discriminator = None
        if announced_on is not None:
            self.announced_on = announced_on
        if created_at is not None:
            self.created_at = created_at
        if entity_def_id is not None:
            self.entity_def_id = entity_def_id
        self.identifier = identifier
        if image_id is not None:
            self.image_id = image_id
        if investor_identifiers is not None:
            self.investor_identifiers = investor_identifiers
        if money_raised is not None:
            self.money_raised = money_raised
        if name is not None:
            self.name = name
        if num_investors is not None:
            self.num_investors = num_investors
        if owner_identifier is not None:
            self.owner_identifier = owner_identifier
        if permalink is not None:
            self.permalink = permalink
        if short_description is not None:
            self.short_description = short_description
        if started_on is not None:
            self.started_on = started_on
        if updated_at is not None:
            self.updated_at = updated_at
        if uuid is not None:
            self.uuid = uuid

    @property
    def announced_on(self):
        """Gets the announced_on of this Fund.  # noqa: E501

        Date when a fund raised is announced\\ Field Type: date\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :return: The announced_on of this Fund.  # noqa: E501
        :rtype: date
        """
        return self._announced_on

    @announced_on.setter
    def announced_on(self, announced_on):
        """Sets the announced_on of this Fund.

        Date when a fund raised is announced\\ Field Type: date\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :param announced_on: The announced_on of this Fund.  # noqa: E501
        :type: date
        """

        self._announced_on = announced_on

    @property
    def created_at(self):
        """Gets the created_at of this Fund.  # noqa: E501

        Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :return: The created_at of this Fund.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Fund.

        Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :param created_at: The created_at of this Fund.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def entity_def_id(self):
        """Gets the entity_def_id of this Fund.  # noqa: E501

        Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * fund - Fund   # noqa: E501

        :return: The entity_def_id of this Fund.  # noqa: E501
        :rtype: str
        """
        return self._entity_def_id

    @entity_def_id.setter
    def entity_def_id(self, entity_def_id):
        """Sets the entity_def_id of this Fund.

        Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * fund - Fund   # noqa: E501

        :param entity_def_id: The entity_def_id of this Fund.  # noqa: E501
        :type: str
        """

        self._entity_def_id = entity_def_id

    @property
    def identifier(self):
        """Gets the identifier of this Fund.  # noqa: E501

        Name of the Fund\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :return: The identifier of this Fund.  # noqa: E501
        :rtype: AllOfFundIdentifier
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Fund.

        Name of the Fund\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :param identifier: The identifier of this Fund.  # noqa: E501
        :type: AllOfFundIdentifier
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def image_id(self):
        """Gets the image_id of this Fund.  # noqa: E501

        Field Type: image_id\\ Searchable: No   # noqa: E501

        :return: The image_id of this Fund.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this Fund.

        Field Type: image_id\\ Searchable: No   # noqa: E501

        :param image_id: The image_id of this Fund.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def investor_identifiers(self):
        """Gets the investor_identifiers of this Fund.  # noqa: E501

        Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all   # noqa: E501

        :return: The investor_identifiers of this Fund.  # noqa: E501
        :rtype: list[EntityIdentifier]
        """
        return self._investor_identifiers

    @investor_identifiers.setter
    def investor_identifiers(self, investor_identifiers):
        """Sets the investor_identifiers of this Fund.

        Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all   # noqa: E501

        :param investor_identifiers: The investor_identifiers of this Fund.  # noqa: E501
        :type: list[EntityIdentifier]
        """

        self._investor_identifiers = investor_identifiers

    @property
    def money_raised(self):
        """Gets the money_raised of this Fund.  # noqa: E501

        Amount raised by the Fund\\ Field Type: money\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq   # noqa: E501

        :return: The money_raised of this Fund.  # noqa: E501
        :rtype: AllOfFundMoneyRaised
        """
        return self._money_raised

    @money_raised.setter
    def money_raised(self, money_raised):
        """Sets the money_raised of this Fund.

        Amount raised by the Fund\\ Field Type: money\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq   # noqa: E501

        :param money_raised: The money_raised of this Fund.  # noqa: E501
        :type: AllOfFundMoneyRaised
        """

        self._money_raised = money_raised

    @property
    def name(self):
        """Gets the name of this Fund.  # noqa: E501

        Name of the Fund\\ Field Type: text_blob\\ Searchable: No   # noqa: E501

        :return: The name of this Fund.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Fund.

        Name of the Fund\\ Field Type: text_blob\\ Searchable: No   # noqa: E501

        :param name: The name of this Fund.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def num_investors(self):
        """Gets the num_investors of this Fund.  # noqa: E501

        Total number of investment firms and individual investors\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq   # noqa: E501

        :return: The num_investors of this Fund.  # noqa: E501
        :rtype: float
        """
        return self._num_investors

    @num_investors.setter
    def num_investors(self, num_investors):
        """Sets the num_investors of this Fund.

        Total number of investment firms and individual investors\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq   # noqa: E501

        :param num_investors: The num_investors of this Fund.  # noqa: E501
        :type: float
        """

        self._num_investors = num_investors

    @property
    def owner_identifier(self):
        """Gets the owner_identifier of this Fund.  # noqa: E501

        Name of the fund owner\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :return: The owner_identifier of this Fund.  # noqa: E501
        :rtype: AllOfFundOwnerIdentifier
        """
        return self._owner_identifier

    @owner_identifier.setter
    def owner_identifier(self, owner_identifier):
        """Sets the owner_identifier of this Fund.

        Name of the fund owner\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :param owner_identifier: The owner_identifier of this Fund.  # noqa: E501
        :type: AllOfFundOwnerIdentifier
        """

        self._owner_identifier = owner_identifier

    @property
    def permalink(self):
        """Gets the permalink of this Fund.  # noqa: E501

        Field Type: permalink\\ Searchable: No   # noqa: E501

        :return: The permalink of this Fund.  # noqa: E501
        :rtype: str
        """
        return self._permalink

    @permalink.setter
    def permalink(self, permalink):
        """Sets the permalink of this Fund.

        Field Type: permalink\\ Searchable: No   # noqa: E501

        :param permalink: The permalink of this Fund.  # noqa: E501
        :type: str
        """

        self._permalink = permalink

    @property
    def short_description(self):
        """Gets the short_description of this Fund.  # noqa: E501

        A short description of the Fund\\ Field Type: text_long\\ Searchable: Yes\\ Search Operators: blank, contains, not_contains   # noqa: E501

        :return: The short_description of this Fund.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this Fund.

        A short description of the Fund\\ Field Type: text_long\\ Searchable: Yes\\ Search Operators: blank, contains, not_contains   # noqa: E501

        :param short_description: The short_description of this Fund.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def started_on(self):
        """Gets the started_on of this Fund.  # noqa: E501

        Date when Fund Owner started invested the Fund\\ Field Type: date_precision\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :return: The started_on of this Fund.  # noqa: E501
        :rtype: AllOfFundStartedOn
        """
        return self._started_on

    @started_on.setter
    def started_on(self, started_on):
        """Sets the started_on of this Fund.

        Date when Fund Owner started invested the Fund\\ Field Type: date_precision\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :param started_on: The started_on of this Fund.  # noqa: E501
        :type: AllOfFundStartedOn
        """

        self._started_on = started_on

    @property
    def updated_at(self):
        """Gets the updated_at of this Fund.  # noqa: E501

        Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :return: The updated_at of this Fund.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Fund.

        Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :param updated_at: The updated_at of this Fund.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def uuid(self):
        """Gets the uuid of this Fund.  # noqa: E501

        Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes   # noqa: E501

        :return: The uuid of this Fund.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Fund.

        Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes   # noqa: E501

        :param uuid: The uuid of this Fund.  # noqa: E501
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
        if issubclass(Fund, dict):
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
        if not isinstance(other, Fund):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
