# cloudmersive_nlp_api_client.SegmentationApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**segmentation_get_sentences**](SegmentationApi.md#segmentation_get_sentences) | **POST** /nlp-v2/segmentation/sentences | Extract sentences from string
[**segmentation_get_words**](SegmentationApi.md#segmentation_get_words) | **POST** /nlp-v2/segmentation/words | Get words in input string


# **segmentation_get_sentences**
> SentenceSegmentationResponse segmentation_get_sentences(input)

Extract sentences from string

Segment an input string into separate sentences, output result as a string.

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
api_instance = cloudmersive_nlp_api_client.SegmentationApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = cloudmersive_nlp_api_client.SentenceSegmentationRequest() # SentenceSegmentationRequest | Input string

try:
    # Extract sentences from string
    api_response = api_instance.segmentation_get_sentences(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentationApi->segmentation_get_sentences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**SentenceSegmentationRequest**](SentenceSegmentationRequest.md)| Input string | 

### Return type

[**SentenceSegmentationResponse**](SentenceSegmentationResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segmentation_get_words**
> GetWordsResponse segmentation_get_words(input)

Get words in input string

Get the component words in an input string

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
api_instance = cloudmersive_nlp_api_client.SegmentationApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = cloudmersive_nlp_api_client.GetWordsRequest() # GetWordsRequest | String to process

try:
    # Get words in input string
    api_response = api_instance.segmentation_get_words(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentationApi->segmentation_get_words: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**GetWordsRequest**](GetWordsRequest.md)| String to process | 

### Return type

[**GetWordsResponse**](GetWordsResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

