# swagger_client.AutocompleteApi

All URIs are relative to *https://api.crunchbase.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocompletes_get**](AutocompleteApi.md#autocompletes_get) | **GET** /autocompletes | Suggests matching Identifier entities based on the query and entity_def_ids provided.

# **autocompletes_get**
> AutocompleteResult autocompletes_get(query, collection_ids=collection_ids, limit=limit)

Suggests matching Identifier entities based on the query and entity_def_ids provided.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuthHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-cb-user-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-cb-user-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AutocompleteApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | Value to perform the autocomplete search with.
collection_ids = 'collection_ids_example' # str | A comma separated list of collection ids to search against. Leaving this blank means it will search across all identifiers. Entity defs can be constrained to specific facets by providing them as facet collections. Relationship collections will resolve to their underlying entity def. \\ Collection ids are: organizations, people, funding_rounds, acquisitions, investments, events, press_references, funds, event_appearances, ipos, ownerships, categories, category_groups, locations, jobs  (optional)
limit = 56 # int | Number of results to retrieve; default = 10, max = 25 (optional)

try:
    # Suggests matching Identifier entities based on the query and entity_def_ids provided.
    api_response = api_instance.autocompletes_get(query, collection_ids=collection_ids, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutocompleteApi->autocompletes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Value to perform the autocomplete search with. | 
 **collection_ids** | **str**| A comma separated list of collection ids to search against. Leaving this blank means it will search across all identifiers. Entity defs can be constrained to specific facets by providing them as facet collections. Relationship collections will resolve to their underlying entity def. \\ Collection ids are: organizations, people, funding_rounds, acquisitions, investments, events, press_references, funds, event_appearances, ipos, ownerships, categories, category_groups, locations, jobs  | [optional] 
 **limit** | **int**| Number of results to retrieve; default &#x3D; 10, max &#x3D; 25 | [optional] 

### Return type

[**AutocompleteResult**](AutocompleteResult.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

