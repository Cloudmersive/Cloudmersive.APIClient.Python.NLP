# cloudmersive_nlp_api_client.ExtractEntitiesApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extract_entities_post**](ExtractEntitiesApi.md#extract_entities_post) | **POST** /nlp-v2/extract-entities | Extract entities from string


# **extract_entities_post**
> ExtractEntitiesResponse extract_entities_post(value)

Extract entities from string

Extract the named entitites from an input string.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_nlp_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.ExtractEntitiesApi(cloudmersive_nlp_api_client.ApiClient(configuration))
value = cloudmersive_nlp_api_client.ExtractEntitiesRequest() # ExtractEntitiesRequest | Input string

try:
    # Extract entities from string
    api_response = api_instance.extract_entities_post(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractEntitiesApi->extract_entities_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | [**ExtractEntitiesRequest**](ExtractEntitiesRequest.md)| Input string | 

### Return type

[**ExtractEntitiesResponse**](ExtractEntitiesResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

