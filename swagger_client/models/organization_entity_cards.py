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

class OrganizationEntityCards(object):
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
        'acquiree_acquisitions': 'list[Acquisition]',
        'acquirer_acquisitions': 'list[Acquisition]',
        'child_organizations': 'list[Organization]',
        'child_ownerships': 'list[Ownership]',
        'event_appearances': 'list[EventAppearance]',
        'fields': 'Organization',
        'founders': 'list[Person]',
        'headquarters_address': 'list[Address]',
        'investors': 'list[Principal]',
        'ipos': 'list[Ipo]',
        'jobs': 'list[Job]',
        'key_employee_changes': 'list[KeyEmployeeChange]',
        'layoffs': 'list[Layoff]',
        'parent_organization': 'list[Organization]',
        'parent_ownership': 'list[Ownership]',
        'participated_funding_rounds': 'list[FundingRound]',
        'participated_funds': 'list[Fund]',
        'participated_investments': 'list[Investment]',
        'press_references': 'list[PressReference]',
        'raised_funding_rounds': 'list[FundingRound]',
        'raised_funds': 'list[Fund]',
        'raised_investments': 'list[Investment]'
    }

    attribute_map = {
        'acquiree_acquisitions': 'acquiree_acquisitions',
        'acquirer_acquisitions': 'acquirer_acquisitions',
        'child_organizations': 'child_organizations',
        'child_ownerships': 'child_ownerships',
        'event_appearances': 'event_appearances',
        'fields': 'fields',
        'founders': 'founders',
        'headquarters_address': 'headquarters_address',
        'investors': 'investors',
        'ipos': 'ipos',
        'jobs': 'jobs',
        'key_employee_changes': 'key_employee_changes',
        'layoffs': 'layoffs',
        'parent_organization': 'parent_organization',
        'parent_ownership': 'parent_ownership',
        'participated_funding_rounds': 'participated_funding_rounds',
        'participated_funds': 'participated_funds',
        'participated_investments': 'participated_investments',
        'press_references': 'press_references',
        'raised_funding_rounds': 'raised_funding_rounds',
        'raised_funds': 'raised_funds',
        'raised_investments': 'raised_investments'
    }

    def __init__(self, acquiree_acquisitions=None, acquirer_acquisitions=None, child_organizations=None, child_ownerships=None, event_appearances=None, fields=None, founders=None, headquarters_address=None, investors=None, ipos=None, jobs=None, key_employee_changes=None, layoffs=None, parent_organization=None, parent_ownership=None, participated_funding_rounds=None, participated_funds=None, participated_investments=None, press_references=None, raised_funding_rounds=None, raised_funds=None, raised_investments=None):  # noqa: E501
        """OrganizationEntityCards - a model defined in Swagger"""  # noqa: E501
        self._acquiree_acquisitions = None
        self._acquirer_acquisitions = None
        self._child_organizations = None
        self._child_ownerships = None
        self._event_appearances = None
        self._fields = None
        self._founders = None
        self._headquarters_address = None
        self._investors = None
        self._ipos = None
        self._jobs = None
        self._key_employee_changes = None
        self._layoffs = None
        self._parent_organization = None
        self._parent_ownership = None
        self._participated_funding_rounds = None
        self._participated_funds = None
        self._participated_investments = None
        self._press_references = None
        self._raised_funding_rounds = None
        self._raised_funds = None
        self._raised_investments = None
        self.discriminator = None
        if acquiree_acquisitions is not None:
            self.acquiree_acquisitions = acquiree_acquisitions
        if acquirer_acquisitions is not None:
            self.acquirer_acquisitions = acquirer_acquisitions
        if child_organizations is not None:
            self.child_organizations = child_organizations
        if child_ownerships is not None:
            self.child_ownerships = child_ownerships
        if event_appearances is not None:
            self.event_appearances = event_appearances
        if fields is not None:
            self.fields = fields
        if founders is not None:
            self.founders = founders
        if headquarters_address is not None:
            self.headquarters_address = headquarters_address
        if investors is not None:
            self.investors = investors
        if ipos is not None:
            self.ipos = ipos
        if jobs is not None:
            self.jobs = jobs
        if key_employee_changes is not None:
            self.key_employee_changes = key_employee_changes
        if layoffs is not None:
            self.layoffs = layoffs
        if parent_organization is not None:
            self.parent_organization = parent_organization
        if parent_ownership is not None:
            self.parent_ownership = parent_ownership
        if participated_funding_rounds is not None:
            self.participated_funding_rounds = participated_funding_rounds
        if participated_funds is not None:
            self.participated_funds = participated_funds
        if participated_investments is not None:
            self.participated_investments = participated_investments
        if press_references is not None:
            self.press_references = press_references
        if raised_funding_rounds is not None:
            self.raised_funding_rounds = raised_funding_rounds
        if raised_funds is not None:
            self.raised_funds = raised_funds
        if raised_investments is not None:
            self.raised_investments = raised_investments

    @property
    def acquiree_acquisitions(self):
        """Gets the acquiree_acquisitions of this OrganizationEntityCards.  # noqa: E501


        :return: The acquiree_acquisitions of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Acquisition]
        """
        return self._acquiree_acquisitions

    @acquiree_acquisitions.setter
    def acquiree_acquisitions(self, acquiree_acquisitions):
        """Sets the acquiree_acquisitions of this OrganizationEntityCards.


        :param acquiree_acquisitions: The acquiree_acquisitions of this OrganizationEntityCards.  # noqa: E501
        :type: list[Acquisition]
        """

        self._acquiree_acquisitions = acquiree_acquisitions

    @property
    def acquirer_acquisitions(self):
        """Gets the acquirer_acquisitions of this OrganizationEntityCards.  # noqa: E501


        :return: The acquirer_acquisitions of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Acquisition]
        """
        return self._acquirer_acquisitions

    @acquirer_acquisitions.setter
    def acquirer_acquisitions(self, acquirer_acquisitions):
        """Sets the acquirer_acquisitions of this OrganizationEntityCards.


        :param acquirer_acquisitions: The acquirer_acquisitions of this OrganizationEntityCards.  # noqa: E501
        :type: list[Acquisition]
        """

        self._acquirer_acquisitions = acquirer_acquisitions

    @property
    def child_organizations(self):
        """Gets the child_organizations of this OrganizationEntityCards.  # noqa: E501


        :return: The child_organizations of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Organization]
        """
        return self._child_organizations

    @child_organizations.setter
    def child_organizations(self, child_organizations):
        """Sets the child_organizations of this OrganizationEntityCards.


        :param child_organizations: The child_organizations of this OrganizationEntityCards.  # noqa: E501
        :type: list[Organization]
        """

        self._child_organizations = child_organizations

    @property
    def child_ownerships(self):
        """Gets the child_ownerships of this OrganizationEntityCards.  # noqa: E501


        :return: The child_ownerships of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Ownership]
        """
        return self._child_ownerships

    @child_ownerships.setter
    def child_ownerships(self, child_ownerships):
        """Sets the child_ownerships of this OrganizationEntityCards.


        :param child_ownerships: The child_ownerships of this OrganizationEntityCards.  # noqa: E501
        :type: list[Ownership]
        """

        self._child_ownerships = child_ownerships

    @property
    def event_appearances(self):
        """Gets the event_appearances of this OrganizationEntityCards.  # noqa: E501


        :return: The event_appearances of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[EventAppearance]
        """
        return self._event_appearances

    @event_appearances.setter
    def event_appearances(self, event_appearances):
        """Sets the event_appearances of this OrganizationEntityCards.


        :param event_appearances: The event_appearances of this OrganizationEntityCards.  # noqa: E501
        :type: list[EventAppearance]
        """

        self._event_appearances = event_appearances

    @property
    def fields(self):
        """Gets the fields of this OrganizationEntityCards.  # noqa: E501


        :return: The fields of this OrganizationEntityCards.  # noqa: E501
        :rtype: Organization
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this OrganizationEntityCards.


        :param fields: The fields of this OrganizationEntityCards.  # noqa: E501
        :type: Organization
        """

        self._fields = fields

    @property
    def founders(self):
        """Gets the founders of this OrganizationEntityCards.  # noqa: E501


        :return: The founders of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Person]
        """
        return self._founders

    @founders.setter
    def founders(self, founders):
        """Sets the founders of this OrganizationEntityCards.


        :param founders: The founders of this OrganizationEntityCards.  # noqa: E501
        :type: list[Person]
        """

        self._founders = founders

    @property
    def headquarters_address(self):
        """Gets the headquarters_address of this OrganizationEntityCards.  # noqa: E501


        :return: The headquarters_address of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Address]
        """
        return self._headquarters_address

    @headquarters_address.setter
    def headquarters_address(self, headquarters_address):
        """Sets the headquarters_address of this OrganizationEntityCards.


        :param headquarters_address: The headquarters_address of this OrganizationEntityCards.  # noqa: E501
        :type: list[Address]
        """

        self._headquarters_address = headquarters_address

    @property
    def investors(self):
        """Gets the investors of this OrganizationEntityCards.  # noqa: E501


        :return: The investors of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Principal]
        """
        return self._investors

    @investors.setter
    def investors(self, investors):
        """Sets the investors of this OrganizationEntityCards.


        :param investors: The investors of this OrganizationEntityCards.  # noqa: E501
        :type: list[Principal]
        """

        self._investors = investors

    @property
    def ipos(self):
        """Gets the ipos of this OrganizationEntityCards.  # noqa: E501


        :return: The ipos of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Ipo]
        """
        return self._ipos

    @ipos.setter
    def ipos(self, ipos):
        """Sets the ipos of this OrganizationEntityCards.


        :param ipos: The ipos of this OrganizationEntityCards.  # noqa: E501
        :type: list[Ipo]
        """

        self._ipos = ipos

    @property
    def jobs(self):
        """Gets the jobs of this OrganizationEntityCards.  # noqa: E501


        :return: The jobs of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Job]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this OrganizationEntityCards.


        :param jobs: The jobs of this OrganizationEntityCards.  # noqa: E501
        :type: list[Job]
        """

        self._jobs = jobs

    @property
    def key_employee_changes(self):
        """Gets the key_employee_changes of this OrganizationEntityCards.  # noqa: E501


        :return: The key_employee_changes of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[KeyEmployeeChange]
        """
        return self._key_employee_changes

    @key_employee_changes.setter
    def key_employee_changes(self, key_employee_changes):
        """Sets the key_employee_changes of this OrganizationEntityCards.


        :param key_employee_changes: The key_employee_changes of this OrganizationEntityCards.  # noqa: E501
        :type: list[KeyEmployeeChange]
        """

        self._key_employee_changes = key_employee_changes

    @property
    def layoffs(self):
        """Gets the layoffs of this OrganizationEntityCards.  # noqa: E501


        :return: The layoffs of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Layoff]
        """
        return self._layoffs

    @layoffs.setter
    def layoffs(self, layoffs):
        """Sets the layoffs of this OrganizationEntityCards.


        :param layoffs: The layoffs of this OrganizationEntityCards.  # noqa: E501
        :type: list[Layoff]
        """

        self._layoffs = layoffs

    @property
    def parent_organization(self):
        """Gets the parent_organization of this OrganizationEntityCards.  # noqa: E501


        :return: The parent_organization of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Organization]
        """
        return self._parent_organization

    @parent_organization.setter
    def parent_organization(self, parent_organization):
        """Sets the parent_organization of this OrganizationEntityCards.


        :param parent_organization: The parent_organization of this OrganizationEntityCards.  # noqa: E501
        :type: list[Organization]
        """

        self._parent_organization = parent_organization

    @property
    def parent_ownership(self):
        """Gets the parent_ownership of this OrganizationEntityCards.  # noqa: E501


        :return: The parent_ownership of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Ownership]
        """
        return self._parent_ownership

    @parent_ownership.setter
    def parent_ownership(self, parent_ownership):
        """Sets the parent_ownership of this OrganizationEntityCards.


        :param parent_ownership: The parent_ownership of this OrganizationEntityCards.  # noqa: E501
        :type: list[Ownership]
        """

        self._parent_ownership = parent_ownership

    @property
    def participated_funding_rounds(self):
        """Gets the participated_funding_rounds of this OrganizationEntityCards.  # noqa: E501


        :return: The participated_funding_rounds of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[FundingRound]
        """
        return self._participated_funding_rounds

    @participated_funding_rounds.setter
    def participated_funding_rounds(self, participated_funding_rounds):
        """Sets the participated_funding_rounds of this OrganizationEntityCards.


        :param participated_funding_rounds: The participated_funding_rounds of this OrganizationEntityCards.  # noqa: E501
        :type: list[FundingRound]
        """

        self._participated_funding_rounds = participated_funding_rounds

    @property
    def participated_funds(self):
        """Gets the participated_funds of this OrganizationEntityCards.  # noqa: E501


        :return: The participated_funds of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Fund]
        """
        return self._participated_funds

    @participated_funds.setter
    def participated_funds(self, participated_funds):
        """Sets the participated_funds of this OrganizationEntityCards.


        :param participated_funds: The participated_funds of this OrganizationEntityCards.  # noqa: E501
        :type: list[Fund]
        """

        self._participated_funds = participated_funds

    @property
    def participated_investments(self):
        """Gets the participated_investments of this OrganizationEntityCards.  # noqa: E501


        :return: The participated_investments of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Investment]
        """
        return self._participated_investments

    @participated_investments.setter
    def participated_investments(self, participated_investments):
        """Sets the participated_investments of this OrganizationEntityCards.


        :param participated_investments: The participated_investments of this OrganizationEntityCards.  # noqa: E501
        :type: list[Investment]
        """

        self._participated_investments = participated_investments

    @property
    def press_references(self):
        """Gets the press_references of this OrganizationEntityCards.  # noqa: E501


        :return: The press_references of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[PressReference]
        """
        return self._press_references

    @press_references.setter
    def press_references(self, press_references):
        """Sets the press_references of this OrganizationEntityCards.


        :param press_references: The press_references of this OrganizationEntityCards.  # noqa: E501
        :type: list[PressReference]
        """

        self._press_references = press_references

    @property
    def raised_funding_rounds(self):
        """Gets the raised_funding_rounds of this OrganizationEntityCards.  # noqa: E501


        :return: The raised_funding_rounds of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[FundingRound]
        """
        return self._raised_funding_rounds

    @raised_funding_rounds.setter
    def raised_funding_rounds(self, raised_funding_rounds):
        """Sets the raised_funding_rounds of this OrganizationEntityCards.


        :param raised_funding_rounds: The raised_funding_rounds of this OrganizationEntityCards.  # noqa: E501
        :type: list[FundingRound]
        """

        self._raised_funding_rounds = raised_funding_rounds

    @property
    def raised_funds(self):
        """Gets the raised_funds of this OrganizationEntityCards.  # noqa: E501


        :return: The raised_funds of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Fund]
        """
        return self._raised_funds

    @raised_funds.setter
    def raised_funds(self, raised_funds):
        """Sets the raised_funds of this OrganizationEntityCards.


        :param raised_funds: The raised_funds of this OrganizationEntityCards.  # noqa: E501
        :type: list[Fund]
        """

        self._raised_funds = raised_funds

    @property
    def raised_investments(self):
        """Gets the raised_investments of this OrganizationEntityCards.  # noqa: E501


        :return: The raised_investments of this OrganizationEntityCards.  # noqa: E501
        :rtype: list[Investment]
        """
        return self._raised_investments

    @raised_investments.setter
    def raised_investments(self, raised_investments):
        """Sets the raised_investments of this OrganizationEntityCards.


        :param raised_investments: The raised_investments of this OrganizationEntityCards.  # noqa: E501
        :type: list[Investment]
        """

        self._raised_investments = raised_investments

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
        if issubclass(OrganizationEntityCards, dict):
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
        if not isinstance(other, OrganizationEntityCards):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
