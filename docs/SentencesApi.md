# cloudmersive_nlp_api_client.SentencesApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sentences_post**](SentencesApi.md#sentences_post) | **POST** /nlp/get/sentences/string | Extract sentences from string


# **sentences_post**
> str sentences_post(input)

Extract sentences from string

Segment an input string into separate sentences, output result as a string.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.SentencesApi()
input = 'input_example' # str | Input string

try:
    # Extract sentences from string
    api_response = api_instance.sentences_post(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SentencesApi->sentences_post: %s\n" % e)
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

