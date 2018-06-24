# cloudmersive_nlp_api_client.WordsApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**words_adjectives**](WordsApi.md#words_adjectives) | **POST** /nlp/get/words/adjectives/string | Get adjectives in string
[**words_adverbs**](WordsApi.md#words_adverbs) | **POST** /nlp/get/words/adverbs/string | Get adverbs in input string
[**words_get_words_json**](WordsApi.md#words_get_words_json) | **POST** /nlp/get/words/json | Get words in input string (JSON)
[**words_get_words_string**](WordsApi.md#words_get_words_string) | **POST** /nlp/get/words/string | Get words from string
[**words_nouns**](WordsApi.md#words_nouns) | **POST** /nlp/get/words/nouns/string | Get nouns in string
[**words_post**](WordsApi.md#words_post) | **POST** /nlp/get/words/verbs/string | Get the verbs in a string
[**words_pronouns**](WordsApi.md#words_pronouns) | **POST** /nlp/get/words/pronouns/string | Returns all pronounts in string
[**words_proper_nouns**](WordsApi.md#words_proper_nouns) | **POST** /nlp/get/words/properNouns/string | Get proper nouns in a string


# **words_adjectives**
> str words_adjectives(input)

Get adjectives in string

Retrieves all adjectives in input string

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
api_instance = cloudmersive_nlp_api_client.WordsApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = 'input_example' # str | Input string

try:
    # Get adjectives in string
    api_response = api_instance.words_adjectives(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->words_adjectives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | **str**| Input string | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **words_adverbs**
> str words_adverbs(input)

Get adverbs in input string

Returns all adverb words in the input string

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
api_instance = cloudmersive_nlp_api_client.WordsApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = 'input_example' # str | Input string

try:
    # Get adverbs in input string
    api_response = api_instance.words_adverbs(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->words_adverbs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | **str**| Input string | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **words_get_words_json**
> GetWordsJsonResponse words_get_words_json(input)

Get words in input string (JSON)

Get the component words in an input string, formatted as JSON

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
api_instance = cloudmersive_nlp_api_client.WordsApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = 'input_example' # str | String to process

try:
    # Get words in input string (JSON)
    api_response = api_instance.words_get_words_json(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->words_get_words_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | **str**| String to process | 

### Return type

[**GetWordsJsonResponse**](GetWordsJsonResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **words_get_words_string**
> str words_get_words_string(input)

Get words from string

Segment an input string into its component words

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
api_instance = cloudmersive_nlp_api_client.WordsApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = 'input_example' # str | Input string

try:
    # Get words from string
    api_response = api_instance.words_get_words_string(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->words_get_words_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | **str**| Input string | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **words_nouns**
> str words_nouns(input)

Get nouns in string

Returns all of the nouns in the input string

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
api_instance = cloudmersive_nlp_api_client.WordsApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = 'input_example' # str | Input string

try:
    # Get nouns in string
    api_response = api_instance.words_nouns(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->words_nouns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | **str**| Input string | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **words_post**
> str words_post(input)

Get the verbs in a string

Get all of the verbs in the input string.

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
api_instance = cloudmersive_nlp_api_client.WordsApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = 'input_example' # str | Input string

try:
    # Get the verbs in a string
    api_response = api_instance.words_post(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->words_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | **str**| Input string | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **words_pronouns**
> str words_pronouns(input)

Returns all pronounts in string

Returns all pronouns in the input string

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
api_instance = cloudmersive_nlp_api_client.WordsApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = 'input_example' # str | Input string

try:
    # Returns all pronounts in string
    api_response = api_instance.words_pronouns(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->words_pronouns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | **str**| Input string | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **words_proper_nouns**
> str words_proper_nouns(input)

Get proper nouns in a string

Returns all of the proper nouns in a string.  Proper nouns are named entities such as \"Hilton\".

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
api_instance = cloudmersive_nlp_api_client.WordsApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = 'input_example' # str | Input string

try:
    # Get proper nouns in a string
    api_response = api_instance.words_proper_nouns(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->words_proper_nouns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | **str**| Input string | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

