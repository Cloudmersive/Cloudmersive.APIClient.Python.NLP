# cloudmersive_nlp_api_client.AnalyticsApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analytics_sentiment**](AnalyticsApi.md#analytics_sentiment) | **POST** /nlp-v2/analytics/sentiment | Perform Sentiment Analysis and Classification on Text


# **analytics_sentiment**
> SentimentAnalysisResponse analytics_sentiment(input)

Perform Sentiment Analysis and Classification on Text

Analyze input text using advanced Sentiment Analysis to determine if the input is positive, negative, or neutral.  Supports English language input.  Consumes 1-2 API calls per sentence.

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
api_instance = cloudmersive_nlp_api_client.AnalyticsApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = cloudmersive_nlp_api_client.SentimentAnalysisRequest() # SentimentAnalysisRequest | Input sentiment analysis request

try:
    # Perform Sentiment Analysis and Classification on Text
    api_response = api_instance.analytics_sentiment(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->analytics_sentiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**SentimentAnalysisRequest**](SentimentAnalysisRequest.md)| Input sentiment analysis request | 

### Return type

[**SentimentAnalysisResponse**](SentimentAnalysisResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

