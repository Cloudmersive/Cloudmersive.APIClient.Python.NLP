# cloudmersive_nlp_api_client
The powerful Natural Language Processing APIs (v2) let you perform part of speech tagging, entity identification, sentence parsing, and much more to help you understand the meaning of unstructured text.

This Python package provides a native API client for [Cloudmersive NLP](https://www.cloudmersive.com/nlp-api)

- API version: v1
- Package version: 3.0.5
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cloudmersive_nlp_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudmersive_nlp_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = cloudmersive_nlp_api_client.ExtractEntitiesApi(cloudmersive_nlp_api_client.ApiClient(configuration))
value = cloudmersive_nlp_api_client.ExtractEntitiesRequest() # ExtractEntitiesRequest | Input string

try:
    # Extract entities from string
    api_response = api_instance.extract_entities_post(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractEntitiesApi->extract_entities_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ExtractEntitiesApi* | [**extract_entities_post**](docs/ExtractEntitiesApi.md#extract_entities_post) | **POST** /nlp-v2/extract-entities | Extract entities from string
*LanguageDetectionApi* | [**language_detection_get_language**](docs/LanguageDetectionApi.md#language_detection_get_language) | **POST** /nlp-v2/language/detect | Detect language of text
*LanguageTranslationApi* | [**language_translation_translate_deu_to_eng**](docs/LanguageTranslationApi.md#language_translation_translate_deu_to_eng) | **POST** /nlp-v2/translate/language/deu/to/eng | Translate German to English text with Deep Learning AI
*LanguageTranslationApi* | [**language_translation_translate_eng_to_deu**](docs/LanguageTranslationApi.md#language_translation_translate_eng_to_deu) | **POST** /nlp-v2/translate/language/eng/to/deu | Translate English to German text with Deep Learning AI
*LanguageTranslationApi* | [**language_translation_translate_eng_to_rus**](docs/LanguageTranslationApi.md#language_translation_translate_eng_to_rus) | **POST** /nlp-v2/translate/language/eng/to/rus | Translate English to Russian text with Deep Learning AI
*LanguageTranslationApi* | [**language_translation_translate_rus_to_eng**](docs/LanguageTranslationApi.md#language_translation_translate_rus_to_eng) | **POST** /nlp-v2/translate/language/rus/to/eng | Translate Russian to English text with Deep Learning AI
*ParseApi* | [**parse_parse_string**](docs/ParseApi.md#parse_parse_string) | **POST** /nlp-v2/parse/tree | Parse string to syntax tree
*PosTaggerApi* | [**pos_tagger_tag_adjectives**](docs/PosTaggerApi.md#pos_tagger_tag_adjectives) | **POST** /nlp-v2/pos/tag/adjectives | Part-of-speech tag a string, filter to adjectives
*PosTaggerApi* | [**pos_tagger_tag_adverbs**](docs/PosTaggerApi.md#pos_tagger_tag_adverbs) | **POST** /nlp-v2/pos/tag/adverbs | Part-of-speech tag a string, filter to adverbs
*PosTaggerApi* | [**pos_tagger_tag_nouns**](docs/PosTaggerApi.md#pos_tagger_tag_nouns) | **POST** /nlp-v2/pos/tag/nouns | Part-of-speech tag a string, filter to nouns
*PosTaggerApi* | [**pos_tagger_tag_pronouns**](docs/PosTaggerApi.md#pos_tagger_tag_pronouns) | **POST** /nlp-v2/pos/tag/pronouns | Part-of-speech tag a string, filter to pronouns
*PosTaggerApi* | [**pos_tagger_tag_sentence**](docs/PosTaggerApi.md#pos_tagger_tag_sentence) | **POST** /nlp-v2/pos/tag/sentence | Part-of-speech tag a string
*PosTaggerApi* | [**pos_tagger_tag_verbs**](docs/PosTaggerApi.md#pos_tagger_tag_verbs) | **POST** /nlp-v2/pos/tag/verbs | Part-of-speech tag a string, filter to verbs
*RephraseApi* | [**rephrase_translate_deu_to_eng**](docs/RephraseApi.md#rephrase_translate_deu_to_eng) | **POST** /nlp-v2/rephrase/rephrase/eng/by-sentence | Rephrase, paraphrase English text sentence-by-sentence using Deep Learning AI
*SegmentationApi* | [**segmentation_get_sentences**](docs/SegmentationApi.md#segmentation_get_sentences) | **POST** /nlp-v2/segmentation/sentences | Extract sentences from string
*SegmentationApi* | [**segmentation_get_words**](docs/SegmentationApi.md#segmentation_get_words) | **POST** /nlp-v2/segmentation/words | Get words in input string
*SpellcheckApi* | [**spellcheck_check_sentence**](docs/SpellcheckApi.md#spellcheck_check_sentence) | **POST** /nlp-v2/spellcheck/check/sentence | Check if sentence is spelled correctly
*SpellcheckApi* | [**spellcheck_correct_json**](docs/SpellcheckApi.md#spellcheck_correct_json) | **POST** /nlp-v2/spellcheck/check/word | Find spelling corrections


## Documentation For Models

 - [CheckSentenceRequest](docs/CheckSentenceRequest.md)
 - [CheckSentenceResponse](docs/CheckSentenceResponse.md)
 - [CheckWordRequest](docs/CheckWordRequest.md)
 - [CheckWordResponse](docs/CheckWordResponse.md)
 - [CorrectWordInSentence](docs/CorrectWordInSentence.md)
 - [Entity](docs/Entity.md)
 - [ExtractEntitiesRequest](docs/ExtractEntitiesRequest.md)
 - [ExtractEntitiesResponse](docs/ExtractEntitiesResponse.md)
 - [GetWordsRequest](docs/GetWordsRequest.md)
 - [GetWordsResponse](docs/GetWordsResponse.md)
 - [LanguageDetectionRequest](docs/LanguageDetectionRequest.md)
 - [LanguageDetectionResponse](docs/LanguageDetectionResponse.md)
 - [LanguageTranslationRequest](docs/LanguageTranslationRequest.md)
 - [LanguageTranslationResponse](docs/LanguageTranslationResponse.md)
 - [ParseRequest](docs/ParseRequest.md)
 - [ParseResponse](docs/ParseResponse.md)
 - [PosRequest](docs/PosRequest.md)
 - [PosResponse](docs/PosResponse.md)
 - [PosSentence](docs/PosSentence.md)
 - [PosTaggedWord](docs/PosTaggedWord.md)
 - [RephraseRequest](docs/RephraseRequest.md)
 - [RephraseResponse](docs/RephraseResponse.md)
 - [RephrasedSentence](docs/RephrasedSentence.md)
 - [RephrasedSentenceOption](docs/RephrasedSentenceOption.md)
 - [SentenceSegmentationRequest](docs/SentenceSegmentationRequest.md)
 - [SentenceSegmentationResponse](docs/SentenceSegmentationResponse.md)
 - [WordPosition](docs/WordPosition.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



