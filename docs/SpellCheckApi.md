# cloudmersive_nlp_api_client.SpellCheckApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spell_check_check_json**](SpellCheckApi.md#spell_check_check_json) | **POST** /nlp/spellcheck/check/word/json | Spell check word
[**spell_check_check_sentence_json**](SpellCheckApi.md#spell_check_check_sentence_json) | **POST** /nlp/spellcheck/check/sentence/json | Check if sentence is spelled correctly
[**spell_check_check_sentence_string**](SpellCheckApi.md#spell_check_check_sentence_string) | **POST** /nlp/spellcheck/check/sentence/string | Spell check a sentence
[**spell_check_correct**](SpellCheckApi.md#spell_check_correct) | **POST** /nlp/spellcheck/correct/word/string | Find spelling corrections
[**spell_check_correct_json**](SpellCheckApi.md#spell_check_correct_json) | **POST** /nlp/spellcheck/correct/word/json | Find spelling corrections
[**spell_check_post**](SpellCheckApi.md#spell_check_post) | **POST** /nlp/spellcheck/check/word/string | Spell check a word


# **spell_check_check_json**
> CheckJsonResponse spell_check_check_json(value)

Spell check word

Spell check a word as JSON

### Example
```python
from __future__ import print_function
import time
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.SpellCheckApi()
value = 'value_example' # str | Input sentence

try:
    # Spell check word
    api_response = api_instance.spell_check_check_json(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpellCheckApi->spell_check_check_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| Input sentence | 

### Return type

[**CheckJsonResponse**](CheckJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spell_check_check_sentence_json**
> CheckSentenceJsonResponse spell_check_check_sentence_json(value)

Check if sentence is spelled correctly

Checks whether the sentence is spelled correctly and returns the result as JSON

### Example
```python
from __future__ import print_function
import time
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.SpellCheckApi()
value = 'value_example' # str | Input sentence

try:
    # Check if sentence is spelled correctly
    api_response = api_instance.spell_check_check_sentence_json(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpellCheckApi->spell_check_check_sentence_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| Input sentence | 

### Return type

[**CheckSentenceJsonResponse**](CheckSentenceJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spell_check_check_sentence_string**
> bool spell_check_check_sentence_string(value)

Spell check a sentence

Check if a sentence is spelled correctly

### Example
```python
from __future__ import print_function
import time
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.SpellCheckApi()
value = 'value_example' # str | Input sentence word

try:
    # Spell check a sentence
    api_response = api_instance.spell_check_check_sentence_string(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpellCheckApi->spell_check_check_sentence_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| Input sentence word | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spell_check_correct**
> str spell_check_correct(value)

Find spelling corrections

Find the spelling corrections for a word

### Example
```python
from __future__ import print_function
import time
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.SpellCheckApi()
value = 'value_example' # str | Input word

try:
    # Find spelling corrections
    api_response = api_instance.spell_check_correct(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpellCheckApi->spell_check_correct: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| Input word | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spell_check_correct_json**
> CorrectJsonResponse spell_check_correct_json(value)

Find spelling corrections

Find spelling correction suggestions and return result as JSON

### Example
```python
from __future__ import print_function
import time
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.SpellCheckApi()
value = 'value_example' # str | Input string

try:
    # Find spelling corrections
    api_response = api_instance.spell_check_correct_json(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpellCheckApi->spell_check_correct_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| Input string | 

### Return type

[**CorrectJsonResponse**](CorrectJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spell_check_post**
> bool spell_check_post(value)

Spell check a word

Check if a word is spelled correctly

### Example
```python
from __future__ import print_function
import time
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.SpellCheckApi()
value = 'value_example' # str | Input string word

try:
    # Spell check a word
    api_response = api_instance.spell_check_post(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpellCheckApi->spell_check_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| Input string word | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

