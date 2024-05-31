# EntitySearch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_ids** | **list[str]** | Fields to include as columns in the search result entities - array of field_id strings | 
**query** | [**list[Predicate]**](Predicate.md) | Search query to perform on the designated entity | 
**order** | [**list[Order]**](Order.md) | Order in which the search results should be returned | [optional] 
**limit** | **int** | Number of rows to return. Default is 100, min is 1, max is 2000. | [optional] 
**before_id** | **str** | Used to paginate search results to the previous page. before_id should be the uuid of the first item in the current page. May not be provided simultaneously with after_id. | [optional] 
**after_id** | **str** | Used to paginate search results to the next page. after_id should be the uuid of the last item in the current page. May not be provided simultaneously with before_id. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

