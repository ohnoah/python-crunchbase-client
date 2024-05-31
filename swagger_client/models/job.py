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

class Job(object):
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
        'employee_featured_order': 'float',
        'ended_on': 'AllOfJobEndedOn',
        'entity_def_id': 'str',
        'identifier': 'AllOfJobIdentifier',
        'is_current': 'bool',
        'job_type': 'str',
        'name': 'str',
        'organization_identifier': 'AllOfJobOrganizationIdentifier',
        'permalink': 'str',
        'person_identifier': 'AllOfJobPersonIdentifier',
        'short_description': 'str',
        'started_on': 'AllOfJobStartedOn',
        'title': 'str',
        'updated_at': 'datetime',
        'uuid': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'employee_featured_order': 'employee_featured_order',
        'ended_on': 'ended_on',
        'entity_def_id': 'entity_def_id',
        'identifier': 'identifier',
        'is_current': 'is_current',
        'job_type': 'job_type',
        'name': 'name',
        'organization_identifier': 'organization_identifier',
        'permalink': 'permalink',
        'person_identifier': 'person_identifier',
        'short_description': 'short_description',
        'started_on': 'started_on',
        'title': 'title',
        'updated_at': 'updated_at',
        'uuid': 'uuid'
    }

    def __init__(self, created_at=None, employee_featured_order=None, ended_on=None, entity_def_id=None, identifier=None, is_current=None, job_type=None, name=None, organization_identifier=None, permalink=None, person_identifier=None, short_description=None, started_on=None, title=None, updated_at=None, uuid=None):  # noqa: E501
        """Job - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._employee_featured_order = None
        self._ended_on = None
        self._entity_def_id = None
        self._identifier = None
        self._is_current = None
        self._job_type = None
        self._name = None
        self._organization_identifier = None
        self._permalink = None
        self._person_identifier = None
        self._short_description = None
        self._started_on = None
        self._title = None
        self._updated_at = None
        self._uuid = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if employee_featured_order is not None:
            self.employee_featured_order = employee_featured_order
        if ended_on is not None:
            self.ended_on = ended_on
        if entity_def_id is not None:
            self.entity_def_id = entity_def_id
        self.identifier = identifier
        if is_current is not None:
            self.is_current = is_current
        if job_type is not None:
            self.job_type = job_type
        if name is not None:
            self.name = name
        if organization_identifier is not None:
            self.organization_identifier = organization_identifier
        if permalink is not None:
            self.permalink = permalink
        if person_identifier is not None:
            self.person_identifier = person_identifier
        if short_description is not None:
            self.short_description = short_description
        if started_on is not None:
            self.started_on = started_on
        if title is not None:
            self.title = title
        if updated_at is not None:
            self.updated_at = updated_at
        if uuid is not None:
            self.uuid = uuid

    @property
    def created_at(self):
        """Gets the created_at of this Job.  # noqa: E501

        Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :return: The created_at of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Job.

        Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :param created_at: The created_at of this Job.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def employee_featured_order(self):
        """Gets the employee_featured_order of this Job.  # noqa: E501

        These are the featured employees of an organization\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq   # noqa: E501

        :return: The employee_featured_order of this Job.  # noqa: E501
        :rtype: float
        """
        return self._employee_featured_order

    @employee_featured_order.setter
    def employee_featured_order(self, employee_featured_order):
        """Sets the employee_featured_order of this Job.

        These are the featured employees of an organization\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq   # noqa: E501

        :param employee_featured_order: The employee_featured_order of this Job.  # noqa: E501
        :type: float
        """

        self._employee_featured_order = employee_featured_order

    @property
    def ended_on(self):
        """Gets the ended_on of this Job.  # noqa: E501

        End date of the Person's Job\\ Field Type: date_precision\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :return: The ended_on of this Job.  # noqa: E501
        :rtype: AllOfJobEndedOn
        """
        return self._ended_on

    @ended_on.setter
    def ended_on(self, ended_on):
        """Sets the ended_on of this Job.

        End date of the Person's Job\\ Field Type: date_precision\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :param ended_on: The ended_on of this Job.  # noqa: E501
        :type: AllOfJobEndedOn
        """

        self._ended_on = ended_on

    @property
    def entity_def_id(self):
        """Gets the entity_def_id of this Job.  # noqa: E501

        Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * job - Job   # noqa: E501

        :return: The entity_def_id of this Job.  # noqa: E501
        :rtype: str
        """
        return self._entity_def_id

    @entity_def_id.setter
    def entity_def_id(self, entity_def_id):
        """Sets the entity_def_id of this Job.

        Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * job - Job   # noqa: E501

        :param entity_def_id: The entity_def_id of this Job.  # noqa: E501
        :type: str
        """

        self._entity_def_id = entity_def_id

    @property
    def identifier(self):
        """Gets the identifier of this Job.  # noqa: E501

        Position name field (e.g. Steve Jobs, Founder @ Pixar)\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :return: The identifier of this Job.  # noqa: E501
        :rtype: AllOfJobIdentifier
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Job.

        Position name field (e.g. Steve Jobs, Founder @ Pixar)\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :param identifier: The identifier of this Job.  # noqa: E501
        :type: AllOfJobIdentifier
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def is_current(self):
        """Gets the is_current of this Job.  # noqa: E501

        This indicates whether the Job is current or not\\ Field Type: boolean\\ Searchable: Yes\\ Search Operators: blank, eq   # noqa: E501

        :return: The is_current of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._is_current

    @is_current.setter
    def is_current(self, is_current):
        """Sets the is_current of this Job.

        This indicates whether the Job is current or not\\ Field Type: boolean\\ Searchable: Yes\\ Search Operators: blank, eq   # noqa: E501

        :param is_current: The is_current of this Job.  # noqa: E501
        :type: bool
        """

        self._is_current = is_current

    @property
    def job_type(self):
        """Gets the job_type of this Job.  # noqa: E501

        Select a job type that best represent your role at the organization\\ Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * advisor - Advisor  * board_member - Board Member  * board_observer - Board Observer  * employee - Non-Executive Employee  * executive - Executive   # noqa: E501

        :return: The job_type of this Job.  # noqa: E501
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this Job.

        Select a job type that best represent your role at the organization\\ Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * advisor - Advisor  * board_member - Board Member  * board_observer - Board Observer  * employee - Non-Executive Employee  * executive - Executive   # noqa: E501

        :param job_type: The job_type of this Job.  # noqa: E501
        :type: str
        """

        self._job_type = job_type

    @property
    def name(self):
        """Gets the name of this Job.  # noqa: E501

        Field Type: text_blob\\ Searchable: No   # noqa: E501

        :return: The name of this Job.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Job.

        Field Type: text_blob\\ Searchable: No   # noqa: E501

        :param name: The name of this Job.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organization_identifier(self):
        """Gets the organization_identifier of this Job.  # noqa: E501

        This is the name of the organization\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :return: The organization_identifier of this Job.  # noqa: E501
        :rtype: AllOfJobOrganizationIdentifier
        """
        return self._organization_identifier

    @organization_identifier.setter
    def organization_identifier(self, organization_identifier):
        """Sets the organization_identifier of this Job.

        This is the name of the organization\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :param organization_identifier: The organization_identifier of this Job.  # noqa: E501
        :type: AllOfJobOrganizationIdentifier
        """

        self._organization_identifier = organization_identifier

    @property
    def permalink(self):
        """Gets the permalink of this Job.  # noqa: E501

        Field Type: permalink\\ Searchable: No   # noqa: E501

        :return: The permalink of this Job.  # noqa: E501
        :rtype: str
        """
        return self._permalink

    @permalink.setter
    def permalink(self, permalink):
        """Sets the permalink of this Job.

        Field Type: permalink\\ Searchable: No   # noqa: E501

        :param permalink: The permalink of this Job.  # noqa: E501
        :type: str
        """

        self._permalink = permalink

    @property
    def person_identifier(self):
        """Gets the person_identifier of this Job.  # noqa: E501

        First and last name of a Person\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :return: The person_identifier of this Job.  # noqa: E501
        :rtype: AllOfJobPersonIdentifier
        """
        return self._person_identifier

    @person_identifier.setter
    def person_identifier(self, person_identifier):
        """Sets the person_identifier of this Job.

        First and last name of a Person\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts   # noqa: E501

        :param person_identifier: The person_identifier of this Job.  # noqa: E501
        :type: AllOfJobPersonIdentifier
        """

        self._person_identifier = person_identifier

    @property
    def short_description(self):
        """Gets the short_description of this Job.  # noqa: E501

        Text of Job Description\\ Field Type: text_long\\ Searchable: Yes\\ Search Operators: blank, contains, not_contains   # noqa: E501

        :return: The short_description of this Job.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this Job.

        Text of Job Description\\ Field Type: text_long\\ Searchable: Yes\\ Search Operators: blank, contains, not_contains   # noqa: E501

        :param short_description: The short_description of this Job.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def started_on(self):
        """Gets the started_on of this Job.  # noqa: E501

        Start date of the Person's Job\\ Field Type: date_precision\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :return: The started_on of this Job.  # noqa: E501
        :rtype: AllOfJobStartedOn
        """
        return self._started_on

    @started_on.setter
    def started_on(self, started_on):
        """Sets the started_on of this Job.

        Start date of the Person's Job\\ Field Type: date_precision\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :param started_on: The started_on of this Job.  # noqa: E501
        :type: AllOfJobStartedOn
        """

        self._started_on = started_on

    @property
    def title(self):
        """Gets the title of this Job.  # noqa: E501

        Title of a Person's Job\\ Field Type: text_short\\ Searchable: Yes\\ Search Operators: blank, contains, eq, not_contains, not_eq, starts   # noqa: E501

        :return: The title of this Job.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Job.

        Title of a Person's Job\\ Field Type: text_short\\ Searchable: Yes\\ Search Operators: blank, contains, eq, not_contains, not_eq, starts   # noqa: E501

        :param title: The title of this Job.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def updated_at(self):
        """Gets the updated_at of this Job.  # noqa: E501

        Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :return: The updated_at of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Job.

        Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte   # noqa: E501

        :param updated_at: The updated_at of this Job.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def uuid(self):
        """Gets the uuid of this Job.  # noqa: E501

        Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes   # noqa: E501

        :return: The uuid of this Job.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Job.

        Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes   # noqa: E501

        :param uuid: The uuid of this Job.  # noqa: E501
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
        if issubclass(Job, dict):
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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
