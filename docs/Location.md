# Location

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | Short alphabetic or numeric geographical codes that represent countries (e.g. TWN, USA, ZAF)\\ Field Type: text_blob\\ Searchable: No  | [optional] 
**country_code_ext** | **str** | Field Type: text_blob\\ Searchable: No  | [optional] 
**created_at** | **datetime** | Created At\\ Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**entity_def_id** | **str** | Field Type: enum\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes\\ Possible values are:  * location - Location  | [optional] 
**facet_ids** | **list[str]** | Type of location (e.g. City, Continent, Regional Area)\\ Field Type: enum_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**groups** | [**list[LocationIdentifier]**](LocationIdentifier.md) | Regional areas this location belongs to (e.g. San Francisco Bay Area, Silicon Valley)\\ Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**identifier** | **AllOfLocationIdentifier** | Short location name (e.g. Japan, San Francisco, Europe)\\ Field Type: identifier\\ Searchable: Yes\\ Search Operators: blank, contains, eq, includes, not_contains, not_eq, not_includes, starts  | 
**locations** | [**list[LocationIdentifier]**](LocationIdentifier.md) | Full location name (e.g. Denver, Colorado, United States, North America)\\ Field Type: identifier_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**name** | **str** | Field Type: text_blob\\ Searchable: No  | [optional] 
**permalink** | **str** | Field Type: permalink\\ Searchable: No  | [optional] 
**permalink_aliases** | **list[str]** | These are the alternative aliases to the primary permalink of the Organization\\ Field Type: text_exact_multi\\ Searchable: Yes\\ Search Operators: blank, includes, includes_all, not_includes, not_includes_all  | [optional] 
**region_code** | **str** | Region code used to define location\\ Field Type: text_blob\\ Searchable: No  | [optional] 
**short_description** | **str** | Description\\ Field Type: text_long\\ Searchable: Yes\\ Search Operators: blank, contains, not_contains  | [optional] 
**updated_at** | **datetime** | Updated At\\ Field Type: datetime\\ Searchable: Yes\\ Search Operators: between, blank, eq, gte, lte  | [optional] 
**uuid** | **str** | Field Type: uuid\\ Searchable: Yes\\ Search Operators: blank, eq, includes, not_eq, not_includes  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

