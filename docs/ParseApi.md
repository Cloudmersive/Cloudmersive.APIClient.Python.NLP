# cloudmersive_nlp_api_client.ParseApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parse_parse_string**](ParseApi.md#parse_parse_string) | **POST** /nlp-v2/parse/tree | Parse string to syntax tree


# **parse_parse_string**
> ParseResponse parse_parse_string(input)

Parse string to syntax tree

Parses the input string into a Penn Treebank syntax tree

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
api_instance = cloudmersive_nlp_api_client.ParseApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = cloudmersive_nlp_api_client.ParseRequest() # ParseRequest | Input string

try:
    # Parse string to syntax tree
    api_response = api_instance.parse_parse_string(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParseApi->parse_parse_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ParseRequest**](ParseRequest.md)| Input string | 

### Return type

[**ParseResponse**](ParseResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

