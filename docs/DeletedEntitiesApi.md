# swagger_client.DeletedEntitiesApi

All URIs are relative to *https://api.crunchbase.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleted_entities_collection_id_get**](DeletedEntitiesApi.md#deleted_entities_collection_id_get) | **GET** /deleted_entities/{collection_id} | Retrieve deleted entities for a collection id
[**deleted_entities_get**](DeletedEntitiesApi.md#deleted_entities_get) | **GET** /deleted_entities | Retrieve deleted entities

# **deleted_entities_collection_id_get**
> DeletedEntitiesResult deleted_entities_collection_id_get(collection_id, before_id=before_id, after_id=after_id, limit=limit, deleted_at_order=deleted_at_order)

Retrieve deleted entities for a collection id

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
api_instance = swagger_client.DeletedEntitiesApi(swagger_client.ApiClient(configuration))
collection_id = 'collection_id_example' # str | Filter by collection id. E.g. organizations, people, funding_rounds, acquisitions, investments, events, press_references, funds, event_appearances, ipos, ownerships, categories, category_groups, locations, jobs 
before_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Used to paginate search results to the previous page. before_id should be the uuid of the first item in the current page. May not be provided simultaneously with after_id.  (optional)
after_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Used to paginate search results to the next page. after_id should be the uuid of the last item in the current page. May not be provided simultaneously with before_id.  (optional)
limit = 56 # int | Number of rows to return. Default is 100, min is 1, max is 2000. (optional)
deleted_at_order = 'deleted_at_order_example' # str | Direction of sorting by deleted_at property (optional)

try:
    # Retrieve deleted entities for a collection id
    api_response = api_instance.deleted_entities_collection_id_get(collection_id, before_id=before_id, after_id=after_id, limit=limit, deleted_at_order=deleted_at_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletedEntitiesApi->deleted_entities_collection_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Filter by collection id. E.g. organizations, people, funding_rounds, acquisitions, investments, events, press_references, funds, event_appearances, ipos, ownerships, categories, category_groups, locations, jobs  | 
 **before_id** | [**str**](.md)| Used to paginate search results to the previous page. before_id should be the uuid of the first item in the current page. May not be provided simultaneously with after_id.  | [optional] 
 **after_id** | [**str**](.md)| Used to paginate search results to the next page. after_id should be the uuid of the last item in the current page. May not be provided simultaneously with before_id.  | [optional] 
 **limit** | **int**| Number of rows to return. Default is 100, min is 1, max is 2000. | [optional] 
 **deleted_at_order** | **str**| Direction of sorting by deleted_at property | [optional] 

### Return type

[**DeletedEntitiesResult**](DeletedEntitiesResult.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleted_entities_get**
> DeletedEntitiesResult deleted_entities_get(collection_ids=collection_ids, before_id=before_id, after_id=after_id, limit=limit, deleted_at_order=deleted_at_order)

Retrieve deleted entities

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
api_instance = swagger_client.DeletedEntitiesApi(swagger_client.ApiClient(configuration))
collection_ids = 'collection_ids_example' # str | Filter by collection id(s). Comma separated list of collection ids.\\ E.g. organizations, people, funding_rounds, acquisitions, investments, events, press_references, funds, event_appearances, ipos, ownerships, categories, category_groups, locations, jobs  (optional)
before_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Used to paginate search results to the previous page. before_id should be the uuid of the first item in the current page. May not be provided simultaneously with after_id.  (optional)
after_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Used to paginate search results to the next page. after_id should be the uuid of the last item in the current page. May not be provided simultaneously with before_id.  (optional)
limit = 56 # int | Number of rows to return. Default is 100, min is 1, max is 2000. (optional)
deleted_at_order = 'deleted_at_order_example' # str | Direction of sorting by deleted_at property (optional)

try:
    # Retrieve deleted entities
    api_response = api_instance.deleted_entities_get(collection_ids=collection_ids, before_id=before_id, after_id=after_id, limit=limit, deleted_at_order=deleted_at_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletedEntitiesApi->deleted_entities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_ids** | **str**| Filter by collection id(s). Comma separated list of collection ids.\\ E.g. organizations, people, funding_rounds, acquisitions, investments, events, press_references, funds, event_appearances, ipos, ownerships, categories, category_groups, locations, jobs  | [optional] 
 **before_id** | [**str**](.md)| Used to paginate search results to the previous page. before_id should be the uuid of the first item in the current page. May not be provided simultaneously with after_id.  | [optional] 
 **after_id** | [**str**](.md)| Used to paginate search results to the next page. after_id should be the uuid of the last item in the current page. May not be provided simultaneously with before_id.  | [optional] 
 **limit** | **int**| Number of rows to return. Default is 100, min is 1, max is 2000. | [optional] 
 **deleted_at_order** | **str**| Direction of sorting by deleted_at property | [optional] 

### Return type

[**DeletedEntitiesResult**](DeletedEntitiesResult.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

