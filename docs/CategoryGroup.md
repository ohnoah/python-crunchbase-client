# CategoryGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**list[EntityIdentifier]**](EntityIdentifier.md) | Descriptive keyword for an Organization (e.g. SaaS, Android, Cloud Computing, Medical Device)\\ Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**created_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**entity_def_id** | **str** | Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * category_group - Industry Group  | [optional] 
**identifier** | **AllOfCategoryGroupIdentifier** | Superset of Industries (e.g. Software, Mobile, Health Care)\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | 
**name** | **str** | Descriptive name of the Industry Group\\ Field Type: text_blob\\ Searchable: No  | [optional] 
**updated_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**uuid** | **str** | Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

