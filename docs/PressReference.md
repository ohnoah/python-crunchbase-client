# PressReference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_entities** | [**list[EntityIdentifier]**](EntityIdentifier.md) | Entities mentioned in the press reference\\ Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**author** | **str** | The author of the press reference\\ Field Type: text_blob\\ Searchable: No  | [optional] 
**created_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**entity_def_id** | **str** | Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * press_reference - Press Reference  | [optional] 
**identifier** | **AllOfPressReferenceIdentifier** | Name of the Article\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | 
**posted_on** | **date** | Date when the press reference is posted\\ Field Type: date\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**publisher** | **str** | The publisher of the press reference\\ Field Type: text_blob\\ Searchable: No  | [optional] 
**thumbnail_url** | **str** | Field Type: text_blob\\ Searchable: No  | [optional] 
**title** | **str** | The title of the press reference\\ Field Type: text_long\\ Searchable: Yes\\ Search Operators: blank, contains, not_contains  | [optional] 
**updated_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**url** | **AllOfPressReferenceUrl** | The URL of the press reference\\ Field Type: link\\ Searchable: No  | [optional] 
**uuid** | **str** | Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

