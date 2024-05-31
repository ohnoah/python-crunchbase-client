# Ownership

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**entity_def_id** | **str** | Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * ownership - Ownership  | [optional] 
**identifier** | **AllOfOwnershipIdentifier** | Short description of the ownership (e.g. Google owns YouTube)\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | 
**name** | **str** | Field Type: text_blob\\ Searchable: No  | [optional] 
**ownee_identifier** | **AllOfOwnershipOwneeIdentifier** | Name of the sub-organization that is related to a parent organization\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | [optional] 
**owner_identifier** | **AllOfOwnershipOwnerIdentifier** | Name of the organization that has sub-organizations\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | [optional] 
**ownership_type** | **str** | This is the relationship defining how a sub-organization is related to a parent organization\\ Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * affiliated_company - Affiliated Company  * division - Division  * investment_arm - Investment Arm  * joint_venture - Joint Venture  * subsidiary - Subsidiary  | [optional] 
**permalink** | **str** | Field Type: permalink\\ Searchable: No  | [optional] 
**updated_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**uuid** | **str** | Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

