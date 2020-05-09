# cloudmersive_nlp_api_client.RephraseApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rephrase_english_rephrase_sentence_by_sentence**](RephraseApi.md#rephrase_english_rephrase_sentence_by_sentence) | **POST** /nlp-v2/rephrase/rephrase/eng/by-sentence | Rephrase, paraphrase English text sentence-by-sentence using Deep Learning AI


# **rephrase_english_rephrase_sentence_by_sentence**
> RephraseResponse rephrase_english_rephrase_sentence_by_sentence(input)

Rephrase, paraphrase English text sentence-by-sentence using Deep Learning AI

Automatically rephrases or paraphrases input text in English sentence by sentence using advanced Deep Learning and Neural NLP.  Creates multiple reprhasing candidates per input sentence, from 1 to 10 possible rephrasings of the original sentence.  Seeks to preserve original semantic meaning in rephrased output candidates.  Consumes 1-2 API calls per output rephrasing option generated, per sentence.

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
api_instance = cloudmersive_nlp_api_client.RephraseApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = cloudmersive_nlp_api_client.RephraseRequest() # RephraseRequest | Input rephrase request

try:
    # Rephrase, paraphrase English text sentence-by-sentence using Deep Learning AI
    api_response = api_instance.rephrase_english_rephrase_sentence_by_sentence(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RephraseApi->rephrase_english_rephrase_sentence_by_sentence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**RephraseRequest**](RephraseRequest.md)| Input rephrase request | 

### Return type

[**RephraseResponse**](RephraseResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

