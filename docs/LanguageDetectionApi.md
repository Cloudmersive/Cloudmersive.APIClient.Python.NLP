# cloudmersive_nlp_api_client.LanguageDetectionApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**language_detection_post**](LanguageDetectionApi.md#language_detection_post) | **POST** /nlp/language/detect | Detect language of text


# **language_detection_post**
> LanguageDetectionResponse language_detection_post(text_to_detect)

Detect language of text

Automatically determine which language a text string is written in.  Supports Danish (DAN), German (DEU), English (ENG), French (FRA), Italian (ITA), Japanese (JPN), Korean (KOR), Dutch (NLD), Norwegian (NOR), Portuguese (POR), Russian (RUS), Spanish (SPA), Swedish (SWE), Chinese (ZHO).

### Example
```python
from __future__ import print_function
import time
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.LanguageDetectionApi()
text_to_detect = 'text_to_detect_example' # str | Text to detect language of

try:
    # Detect language of text
    api_response = api_instance.language_detection_post(text_to_detect)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageDetectionApi->language_detection_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_to_detect** | **str**| Text to detect language of | 

### Return type

[**LanguageDetectionResponse**](LanguageDetectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

