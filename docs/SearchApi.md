# swagger_client.SearchApi

All URIs are relative to *https://api.crunchbase.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searches_acquisitions_post**](SearchApi.md#searches_acquisitions_post) | **POST** /searches/acquisitions | Search Acquisition Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_addresses_post**](SearchApi.md#searches_addresses_post) | **POST** /searches/addresses | Search Address Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_categories_post**](SearchApi.md#searches_categories_post) | **POST** /searches/categories | Search Category Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_category_groups_post**](SearchApi.md#searches_category_groups_post) | **POST** /searches/category_groups | Search Category Group Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_degrees_post**](SearchApi.md#searches_degrees_post) | **POST** /searches/degrees | Search Degree Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_event_appearances_post**](SearchApi.md#searches_event_appearances_post) | **POST** /searches/event_appearances | Search Event Appearance Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_events_post**](SearchApi.md#searches_events_post) | **POST** /searches/events | Search Event Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_funding_rounds_post**](SearchApi.md#searches_funding_rounds_post) | **POST** /searches/funding_rounds | Search Funding Round Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_funds_post**](SearchApi.md#searches_funds_post) | **POST** /searches/funds | Search Fund Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_investments_post**](SearchApi.md#searches_investments_post) | **POST** /searches/investments | Search Investment Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_ipos_post**](SearchApi.md#searches_ipos_post) | **POST** /searches/ipos | Search Ipo Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_jobs_post**](SearchApi.md#searches_jobs_post) | **POST** /searches/jobs | Search Job Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_key_employee_changes_post**](SearchApi.md#searches_key_employee_changes_post) | **POST** /searches/key_employee_changes | Search Key Employee Change Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_layoffs_post**](SearchApi.md#searches_layoffs_post) | **POST** /searches/layoffs | Search Layoff Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_locations_post**](SearchApi.md#searches_locations_post) | **POST** /searches/locations | Search Location Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_organizations_post**](SearchApi.md#searches_organizations_post) | **POST** /searches/organizations | Search Organization Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_ownerships_post**](SearchApi.md#searches_ownerships_post) | **POST** /searches/ownerships | Search Ownership Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_people_post**](SearchApi.md#searches_people_post) | **POST** /searches/people | Search Person Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_press_references_post**](SearchApi.md#searches_press_references_post) | **POST** /searches/press_references | Search Press Reference Entities. Can perform more complex filtering based on the query defined in the request body. 
[**searches_principals_post**](SearchApi.md#searches_principals_post) | **POST** /searches/principals | Search Principal Entities. Can perform more complex filtering based on the query defined in the request body. 

# **searches_acquisitions_post**
> AcquisitionSearchResults searches_acquisitions_post(body)

Search Acquisition Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Acquisition Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_acquisitions_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_acquisitions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**AcquisitionSearchResults**](AcquisitionSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_addresses_post**
> AddressSearchResults searches_addresses_post(body)

Search Address Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Address Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_addresses_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_addresses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**AddressSearchResults**](AddressSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_categories_post**
> CategorySearchResults searches_categories_post(body)

Search Category Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Category Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_categories_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_categories_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**CategorySearchResults**](CategorySearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_category_groups_post**
> CategoryGroupSearchResults searches_category_groups_post(body)

Search Category Group Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Category Group Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_category_groups_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_category_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**CategoryGroupSearchResults**](CategoryGroupSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_degrees_post**
> DegreeSearchResults searches_degrees_post(body)

Search Degree Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Degree Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_degrees_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_degrees_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**DegreeSearchResults**](DegreeSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_event_appearances_post**
> EventAppearanceSearchResults searches_event_appearances_post(body)

Search Event Appearance Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Event Appearance Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_event_appearances_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_event_appearances_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**EventAppearanceSearchResults**](EventAppearanceSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_events_post**
> EventSearchResults searches_events_post(body)

Search Event Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Event Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_events_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_events_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**EventSearchResults**](EventSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_funding_rounds_post**
> FundingRoundSearchResults searches_funding_rounds_post(body)

Search Funding Round Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Funding Round Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_funding_rounds_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_funding_rounds_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**FundingRoundSearchResults**](FundingRoundSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_funds_post**
> FundSearchResults searches_funds_post(body)

Search Fund Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Fund Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_funds_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_funds_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**FundSearchResults**](FundSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_investments_post**
> InvestmentSearchResults searches_investments_post(body)

Search Investment Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Investment Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_investments_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_investments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**InvestmentSearchResults**](InvestmentSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_ipos_post**
> IpoSearchResults searches_ipos_post(body)

Search Ipo Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Ipo Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_ipos_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_ipos_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**IpoSearchResults**](IpoSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_jobs_post**
> JobSearchResults searches_jobs_post(body)

Search Job Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Job Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_jobs_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_jobs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**JobSearchResults**](JobSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_key_employee_changes_post**
> KeyEmployeeChangeSearchResults searches_key_employee_changes_post(body)

Search Key Employee Change Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Key Employee Change Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_key_employee_changes_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_key_employee_changes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**KeyEmployeeChangeSearchResults**](KeyEmployeeChangeSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_layoffs_post**
> LayoffSearchResults searches_layoffs_post(body)

Search Layoff Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Layoff Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_layoffs_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_layoffs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**LayoffSearchResults**](LayoffSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_locations_post**
> LocationSearchResults searches_locations_post(body)

Search Location Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Location Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_locations_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_locations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**LocationSearchResults**](LocationSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_organizations_post**
> OrganizationSearchResults searches_organizations_post(body)

Search Organization Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Organization Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_organizations_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_organizations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**OrganizationSearchResults**](OrganizationSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_ownerships_post**
> OwnershipSearchResults searches_ownerships_post(body)

Search Ownership Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Ownership Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_ownerships_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_ownerships_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**OwnershipSearchResults**](OwnershipSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_people_post**
> PersonSearchResults searches_people_post(body)

Search Person Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Person Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_people_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_people_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**PersonSearchResults**](PersonSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_press_references_post**
> PressReferenceSearchResults searches_press_references_post(body)

Search Press Reference Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Press Reference Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_press_references_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_press_references_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**PressReferenceSearchResults**](PressReferenceSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_principals_post**
> PrincipalSearchResults searches_principals_post(body)

Search Principal Entities. Can perform more complex filtering based on the query defined in the request body. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EntitySearch() # EntitySearch | Search Query Parameters

try:
    # Search Principal Entities. Can perform more complex filtering based on the query defined in the request body. 
    api_response = api_instance.searches_principals_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->searches_principals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitySearch**](EntitySearch.md)| Search Query Parameters | 

### Return type

[**PrincipalSearchResults**](PrincipalSearchResults.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

