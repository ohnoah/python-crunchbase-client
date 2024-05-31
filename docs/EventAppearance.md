# EventAppearance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appearance_type** | **str** | Describe how an Organization or a Person is participating in an Event (e.g. Speaker, Sponsor, etc.)\\ Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * contestant - Contestant  * exhibitor - Exhibitor  * organizer - Organizer  * speaker - Speaker  * sponsor - Sponsor  | [optional] 
**created_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**entity_def_id** | **str** | Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * event_appearance - Event Appearance  | [optional] 
**event_identifier** | **AllOfEventAppearanceEventIdentifier** | Name of the Event\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | [optional] 
**event_location_identifiers** | [**list[LocationIdentifier]**](LocationIdentifier.md) | Location of the Event (e.g. Japan, San Francisco, Europe, Asia)\\ Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**event_starts_on** | **date** | Start date of the Event\\ Field Type: date\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**identifier** | **AllOfEventAppearanceIdentifier** | Name of the Event Appearance\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | 
**name** | **str** | Field Type: text_long\\ Searchable: Yes\\ Search Operators: blank, contains, not_contains  | [optional] 
**participant_identifier** | **AllOfEventAppearanceParticipantIdentifier** | The name of the participant in an Event\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | [optional] 
**permalink** | **str** | Field Type: permalink\\ Searchable: No  | [optional] 
**short_description** | **str** | A short description of how a person or an organization is participant in an Event\\ Field Type: text_long\\ Searchable: Yes\\ Search Operators: blank, contains, not_contains  | [optional] 
**updated_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**uuid** | **str** | Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

