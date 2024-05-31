# Address

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | Country Code\\ Field Type: text_exact\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes  | [optional] 
**created_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**entity_def_id** | **str** | Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * address - Address  | [optional] 
**headquartered_organization_identifier** | **AllOfAddressHeadquarteredOrganizationIdentifier** | Identifier of the organization that&#x27;s headquartered on this address\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | [optional] 
**identifier** | **AllOfAddressIdentifier** | Descriptive name of the Address (e.g. Headquarters, London Office)\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | 
**location_identifiers** | [**list[LocationIdentifier]**](LocationIdentifier.md) | What city the address is located in (e.g. San Francisco, London, Kiev).\\ Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**name** | **str** | Descriptive name of the Address (e.g. Headquarters, London Office)\\ Field Type: text_blob\\ Searchable: No  | [optional] 
**postal_code** | **str** | The postal code of the address\\ Field Type: text_blob\\ Searchable: No  | [optional] 
**region_code** | **str** | Region Code\\ Field Type: text_exact\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes  | [optional] 
**street_1** | **str** | The street address of the location\\ Field Type: text_blob\\ Searchable: No  | [optional] 
**street_2** | **str** | The street address of the location\\ Field Type: text_blob\\ Searchable: No  | [optional] 
**updated_at** | **datetime** | Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**uuid** | **str** | Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

