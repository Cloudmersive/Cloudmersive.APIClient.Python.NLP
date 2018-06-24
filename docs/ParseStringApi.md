# cloudmersive_nlp_api_client.ParseStringApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parse_string_post**](ParseStringApi.md#parse_string_post) | **POST** /nlp/ParseString | Parse string to syntax tree


# **parse_string_post**
> str parse_string_post(input)

Parse string to syntax tree

Parses the input string into a Penn Treebank syntax tree

### Example
```python
from __future__ import print_function
import time
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.ParseStringApi()
input = 'input_example' # str | Input string

try:
    # Parse string to syntax tree
    api_response = api_instance.parse_string_post(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParseStringApi->parse_string_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | **str**| Input string | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

