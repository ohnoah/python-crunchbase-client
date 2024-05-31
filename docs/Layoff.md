# Layoff

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Laoyff entity creation date\\ Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**entity_def_id** | **str** | Layoff Signal\\ Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * layoff - layoff  | [optional] 
**identifier** | [**EntityIdentifier**](EntityIdentifier.md) |  | 
**key_event_date** | **date** | Date when the news article was posted\\ Field Type: date\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**organization_identifier** | **AllOfLayoffOrganizationIdentifier** | Organization that had a layoff mentioned\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | [optional] 
**updated_at** | **datetime** | Entity Updating date\\ Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**uuid** | **str** | Entity UUID\\ Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

