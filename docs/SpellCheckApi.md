# cloudmersive_nlp_api_client.SpellcheckApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spellcheck_check_sentence**](SpellcheckApi.md#spellcheck_check_sentence) | **POST** /nlp-v2/spellcheck/check/sentence | Check if sentence is spelled correctly
[**spellcheck_correct_json**](SpellcheckApi.md#spellcheck_correct_json) | **POST** /nlp-v2/spellcheck/check/word | Find spelling corrections


# **spellcheck_check_sentence**
> CheckSentenceResponse spellcheck_check_sentence(value)

Check if sentence is spelled correctly

Checks whether the sentence is spelled correctly and returns the result as JSON

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
api_instance = cloudmersive_nlp_api_client.SpellcheckApi(cloudmersive_nlp_api_client.ApiClient(configuration))
value = cloudmersive_nlp_api_client.CheckSentenceRequest() # CheckSentenceRequest | Input sentence

try:
    # Check if sentence is spelled correctly
    api_response = api_instance.spellcheck_check_sentence(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpellcheckApi->spellcheck_check_sentence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | [**CheckSentenceRequest**](CheckSentenceRequest.md)| Input sentence | 

### Return type

[**CheckSentenceResponse**](CheckSentenceResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spellcheck_correct_json**
> CheckWordResponse spellcheck_correct_json(value)

Find spelling corrections

Find spelling correction suggestions and return result as JSON

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
api_instance = cloudmersive_nlp_api_client.SpellcheckApi(cloudmersive_nlp_api_client.ApiClient(configuration))
value = cloudmersive_nlp_api_client.CheckWordRequest() # CheckWordRequest | Input string

try:
    # Find spelling corrections
    api_response = api_instance.spellcheck_correct_json(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpellcheckApi->spellcheck_correct_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | [**CheckWordRequest**](CheckWordRequest.md)| Input string | 

### Return type

[**CheckWordResponse**](CheckWordResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

