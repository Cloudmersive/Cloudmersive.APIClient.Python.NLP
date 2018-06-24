# cloudmersive_nlp_api_client.ExtractEntitiesStringApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extract_entities_string_post**](ExtractEntitiesStringApi.md#extract_entities_string_post) | **POST** /nlp/ExtractEntitiesString | Extract entities from string


# **extract_entities_string_post**
> str extract_entities_string_post(value)

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
api_instance = cloudmersive_nlp_api_client.ExtractEntitiesStringApi(cloudmersive_nlp_api_client.ApiClient(configuration))
value = 'value_example' # str | Input string

try:
    # Extract entities from string
    api_response = api_instance.extract_entities_string_post(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractEntitiesStringApi->extract_entities_string_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| Input string | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

