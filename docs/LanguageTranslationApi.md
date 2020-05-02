# cloudmersive_nlp_api_client.LanguageTranslationApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**language_translation_translate_deu_to_eng**](LanguageTranslationApi.md#language_translation_translate_deu_to_eng) | **POST** /nlp-v2/translate/language/deu/to/eng | Translate German to English text with Deep Learning AI
[**language_translation_translate_eng_to_deu**](LanguageTranslationApi.md#language_translation_translate_eng_to_deu) | **POST** /nlp-v2/translate/language/eng/to/deu | Translate English to German text with Deep Learning AI


# **language_translation_translate_deu_to_eng**
> LanguageTranslationResponse language_translation_translate_deu_to_eng(input)

Translate German to English text with Deep Learning AI

Automatically translates input text in German to output text in English using advanced Deep Learning and Neural NLP.  Consumes 1-2 API calls per input sentence.

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
api_instance = cloudmersive_nlp_api_client.LanguageTranslationApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = cloudmersive_nlp_api_client.LanguageTranslationRequest() # LanguageTranslationRequest | Input translation request

try:
    # Translate German to English text with Deep Learning AI
    api_response = api_instance.language_translation_translate_deu_to_eng(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageTranslationApi->language_translation_translate_deu_to_eng: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**LanguageTranslationRequest**](LanguageTranslationRequest.md)| Input translation request | 

### Return type

[**LanguageTranslationResponse**](LanguageTranslationResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **language_translation_translate_eng_to_deu**
> LanguageTranslationResponse language_translation_translate_eng_to_deu(input)

Translate English to German text with Deep Learning AI

Automatically translates input text in English to output text in German using advanced Deep Learning and Neural NLP.  Consumes 1-2 API calls per input sentence.

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
api_instance = cloudmersive_nlp_api_client.LanguageTranslationApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = cloudmersive_nlp_api_client.LanguageTranslationRequest() # LanguageTranslationRequest | Input translation request

try:
    # Translate English to German text with Deep Learning AI
    api_response = api_instance.language_translation_translate_eng_to_deu(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageTranslationApi->language_translation_translate_eng_to_deu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**LanguageTranslationRequest**](LanguageTranslationRequest.md)| Input translation request | 

### Return type

[**LanguageTranslationResponse**](LanguageTranslationResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

