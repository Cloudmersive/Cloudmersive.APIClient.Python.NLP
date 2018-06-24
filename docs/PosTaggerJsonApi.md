# cloudmersive_nlp_api_client.PosTaggerJsonApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pos_tagger_json_post**](PosTaggerJsonApi.md#pos_tagger_json_post) | **POST** /nlp/PosTaggerJson | Part-of-speech tag a string


# **pos_tagger_json_post**
> PosResponse pos_tagger_json_post(request)

Part-of-speech tag a string

Part-of-speech (POS) tag a string and return result as JSON

### Example
```python
from __future__ import print_function
import time
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.PosTaggerJsonApi()
request = cloudmersive_nlp_api_client.PosRequest() # PosRequest | Input string

try:
    # Part-of-speech tag a string
    api_response = api_instance.pos_tagger_json_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PosTaggerJsonApi->pos_tagger_json_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PosRequest**](PosRequest.md)| Input string | 

### Return type

[**PosResponse**](PosResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

