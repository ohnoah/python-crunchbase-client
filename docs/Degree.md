# Degree

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_on** | **AllOfDegreeCompletedOn** | Date when the degree is completed\\ Field Type: date_precision\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**created_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**entity_def_id** | **str** | Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * degree - Degree  | [optional] 
**identifier** | **AllOfDegreeIdentifier** | Name of the Degree\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | 
**name** | **str** | Field Type: text_blob\\ Searchable: No  | [optional] 
**person_identifier** | **AllOfDegreePersonIdentifier** | The Person that received the Degree\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | [optional] 
**school_identifier** | **AllOfDegreeSchoolIdentifier** | The School that awarded the Degree\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | [optional] 
**started_on** | **AllOfDegreeStartedOn** | Date when the degree is started\\ Field Type: date_precision\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**subject** | **str** | The subject or major that the person focused his/her degree on\\ Field Type: text_short\\ Searchable: Yes\\ Search Operators: blank, contains, eq, not_contains, not_eq, starts  | [optional] 
**type_name** | **str** | The type of degree that the person received\\ Field Type: text_short\\ Searchable: Yes\\ Search Operators: blank, contains, eq, not_contains, not_eq, starts  | [optional] 
**updated_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**uuid** | **str** | Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

