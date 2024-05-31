# Fund

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announced_on** | **date** | Date when a fund raised is announced\\ Field Type: date\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**created_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**entity_def_id** | **str** | Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * fund - Fund  | [optional] 
**identifier** | **AllOfFundIdentifier** | Name of the Fund\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | 
**image_id** | **str** | Field Type: image_id\\ Searchable: No  | [optional] 
**investor_identifiers** | [**list[EntityIdentifier]**](EntityIdentifier.md) | Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**money_raised** | **AllOfFundMoneyRaised** | Amount raised by the Fund\\ Field Type: money\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**name** | **str** | Name of the Fund\\ Field Type: text_blob\\ Searchable: No  | [optional] 
**num_investors** | **float** | Total number of investment firms and individual investors\\ Field Type: integer\\ Searchable: Yes\\ Search Operators: between, blank, eq, gt, gte, lt, lte, not_eq  | [optional] 
**owner_identifier** | **AllOfFundOwnerIdentifier** | Name of the fund owner\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | [optional] 
**permalink** | **str** | Field Type: permalink\\ Searchable: No  | [optional] 
**short_description** | **str** | A short description of the Fund\\ Field Type: text_long\\ Searchable: Yes\\ Search Operators: blank, contains, not_contains  | [optional] 
**started_on** | **AllOfFundStartedOn** | Date when Fund Owner started invested the Fund\\ Field Type: date_precision\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**updated_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**uuid** | **str** | Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

