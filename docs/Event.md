# Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**list[EntityIdentifier]**](EntityIdentifier.md) | Descriptive keyword for a Company (e.g. SaaS, Android, Cloud Computing, Medical Device)\\ Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**category_groups** | [**list[EntityIdentifier]**](EntityIdentifier.md) | Superset of Industries (e.g. Software, Mobile, Health Care)\\ Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**created_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**description** | **str** | Text from Event&#x27;s description\\ Field Type: text_long\\ Searchable: Yes\\ Search Operators: blank, contains, not_contains  | [optional] 
**ends_on** | **date** | End date of the Event\\ Field Type: date\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**entity_def_id** | **str** | Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * event - Event  | [optional] 
**event_type** | **list[str]** | Type of Event (e.g. hackathon, meetup, conference)\\ Field Type: enum_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**event_url** | **AllOfEventEventUrl** | Link to main Event page\\ Field Type: link\\ Searchable: No  | [optional] 
**identifier** | **AllOfEventIdentifier** | Name of the Event\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | 
**image_id** | **str** | The profile image of the event on Crunchbase\\ Field Type: image_id\\ Searchable: No  | [optional] 
**image_url** | **str** | The cloudinary url of the profile image\\ Field Type: text_blob\\ Searchable: No  | [optional] 
**location_group_identifiers** | [**list[EntityIdentifier]**](EntityIdentifier.md) | Regions of the Event (e.g. San Francisco Bay Area, Silicon Valley)\\ Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**location_identifiers** | [**list[LocationIdentifier]**](LocationIdentifier.md) | Location of the Event (e.g. Japan, San Francisco, Europe, Asia)\\ Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**name** | **str** | Event Name\\ Field Type: text_blob\\ Searchable: No  | [optional] 
**num_contestants** | **float** | Total number of Contestants at the Event\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_exhibitors** | **float** | Total number of Exhibitors at the Event\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_organizers** | **float** | Total number of Organizers at the Event\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_speakers** | **float** | Total number of Speakers at the Event\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**num_sponsors** | **float** | Total number of Sponsors for the Event\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**organizer_identifiers** | [**list[EntityIdentifier]**](EntityIdentifier.md) | The organizer of the Event\\ Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**permalink** | **str** | Field Type: permalink\\ Searchable: No  | [optional] 
**permalink_aliases** | **list[str]** | These are the alternative aliases to the primary permalink of the Organization\\ Field Type: text_exact_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**rank_event** | **float** | Algorithmic rank assigned to the top 100,000 most active Events\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**registration_url** | **AllOfEventRegistrationUrl** | Link to the Event registration page\\ Field Type: link\\ Searchable: No  | [optional] 
**short_description** | **str** | A short description of the Event\\ Field Type: text_long\\ Searchable: Yes\\ Search Operators: blank, contains, not_contains  | [optional] 
**starts_on** | **date** | Start date of the Event\\ Field Type: date\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**updated_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**uuid** | **str** | Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes  | [optional] 
**venue_name** | **str** | Name of the Event venue\\ Field Type: text_short\\ Searchable: Yes\\ Search Operators: blank, contains, eq, not_contains, not_eq, starts  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

