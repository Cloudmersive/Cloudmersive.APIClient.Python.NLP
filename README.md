# cloudmersive_nlp_api_client
The powerful Natural Language Processing APIs let you perform part of speech tagging, entity identification, sentence parsing, and much more to help you understand the meaning of unstructured text.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.1.5
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
cloudmersive_nlp_api_client.configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# cloudmersive_nlp_api_client.configuration.api_key_prefix['Apikey'] = 'Bearer'
# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.ExtractEntitiesStringApi()
value = 'value_example' # str | Input string

try:
    # Extract entities from string
    api_response = api_instance.extract_entities_string_post(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractEntitiesStringApi->extract_entities_string_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ExtractEntitiesStringApi* | [**extract_entities_string_post**](docs/ExtractEntitiesStringApi.md#extract_entities_string_post) | **POST** /nlp/ExtractEntitiesString | Extract entities from string
*LanguageDetectionApi* | [**language_detection_post**](docs/LanguageDetectionApi.md#language_detection_post) | **POST** /nlp/language/detect | Detect language of text
*ParseStringApi* | [**parse_string_post**](docs/ParseStringApi.md#parse_string_post) | **POST** /nlp/ParseString | Parse string to syntax tree
*PosTaggerJsonApi* | [**pos_tagger_json_post**](docs/PosTaggerJsonApi.md#pos_tagger_json_post) | **POST** /nlp/PosTaggerJson | Part-of-speech tag a string
*PosTaggerStringApi* | [**pos_tagger_string_post**](docs/PosTaggerStringApi.md#pos_tagger_string_post) | **POST** /nlp/PosTaggerString | Part-of-speech tag a string
*SentencesApi* | [**sentences_post**](docs/SentencesApi.md#sentences_post) | **POST** /nlp/get/sentences/string | Extract sentences from string
*SpellCheckApi* | [**spell_check_check_json**](docs/SpellCheckApi.md#spell_check_check_json) | **POST** /nlp/spellcheck/check/word/json | Spell check word
*SpellCheckApi* | [**spell_check_check_sentence_json**](docs/SpellCheckApi.md#spell_check_check_sentence_json) | **POST** /nlp/spellcheck/check/sentence/json | Check if sentence is spelled correctly
*SpellCheckApi* | [**spell_check_check_sentence_string**](docs/SpellCheckApi.md#spell_check_check_sentence_string) | **POST** /nlp/spellcheck/check/sentence/string | Spell check a sentence
*SpellCheckApi* | [**spell_check_correct**](docs/SpellCheckApi.md#spell_check_correct) | **POST** /nlp/spellcheck/correct/word/string | Find spelling corrections
*SpellCheckApi* | [**spell_check_correct_json**](docs/SpellCheckApi.md#spell_check_correct_json) | **POST** /nlp/spellcheck/correct/word/json | Find spelling corrections
*SpellCheckApi* | [**spell_check_post**](docs/SpellCheckApi.md#spell_check_post) | **POST** /nlp/spellcheck/check/word/string | Spell check a word
*WordsApi* | [**words_adjectives**](docs/WordsApi.md#words_adjectives) | **POST** /nlp/get/words/adjectives/string | Get adjectives in string
*WordsApi* | [**words_adverbs**](docs/WordsApi.md#words_adverbs) | **POST** /nlp/get/words/adverbs/string | Get adverbs in input string
*WordsApi* | [**words_get_words_json**](docs/WordsApi.md#words_get_words_json) | **POST** /nlp/get/words/json | Get words in input string (JSON)
*WordsApi* | [**words_get_words_string**](docs/WordsApi.md#words_get_words_string) | **POST** /nlp/get/words/string | Get words from string
*WordsApi* | [**words_nouns**](docs/WordsApi.md#words_nouns) | **POST** /nlp/get/words/nouns/string | Get nouns in string
*WordsApi* | [**words_post**](docs/WordsApi.md#words_post) | **POST** /nlp/get/words/verbs/string | Get the verbs in a string
*WordsApi* | [**words_pronouns**](docs/WordsApi.md#words_pronouns) | **POST** /nlp/get/words/pronouns/string | Returns all pronounts in string
*WordsApi* | [**words_proper_nouns**](docs/WordsApi.md#words_proper_nouns) | **POST** /nlp/get/words/properNouns/string | Get proper nouns in a string


## Documentation For Models

 - [CheckJsonResponse](docs/CheckJsonResponse.md)
 - [CheckSentenceJsonResponse](docs/CheckSentenceJsonResponse.md)
 - [CorrectJsonResponse](docs/CorrectJsonResponse.md)
 - [CorrectWordInSentenceJsonResponse](docs/CorrectWordInSentenceJsonResponse.md)
 - [GetWordsJsonResponse](docs/GetWordsJsonResponse.md)
 - [LanguageDetectionResponse](docs/LanguageDetectionResponse.md)
 - [PosRequest](docs/PosRequest.md)
 - [PosResponse](docs/PosResponse.md)
 - [PosSentence](docs/PosSentence.md)
 - [PosTaggedWord](docs/PosTaggedWord.md)
 - [WordPosition](docs/WordPosition.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author


