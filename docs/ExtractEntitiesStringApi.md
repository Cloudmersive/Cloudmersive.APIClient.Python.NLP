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

# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.ExtractEntitiesStringApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

