# cloudmersive_nlp_api_client.PosTaggerStringApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pos_tagger_string_post**](PosTaggerStringApi.md#pos_tagger_string_post) | **POST** /nlp/PosTaggerString | Part-of-speech tag a string


# **pos_tagger_string_post**
> str pos_tagger_string_post(input)

Part-of-speech tag a string

Perform a part-of-speech (POS) tagging on the input string.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.PosTaggerStringApi()
input = 'input_example' # str | Input string

try:
    # Part-of-speech tag a string
    api_response = api_instance.pos_tagger_string_post(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PosTaggerStringApi->pos_tagger_string_post: %s\n" % e)
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

