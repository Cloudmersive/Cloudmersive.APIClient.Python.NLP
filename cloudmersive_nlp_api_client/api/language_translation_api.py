# coding: utf-8

"""
    nlpapiv2

    The powerful Natural Language Processing APIs (v2) let you perform part of speech tagging, entity identification, sentence parsing, and much more to help you understand the meaning of unstructured text.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudmersive_nlp_api_client.api_client import ApiClient


class LanguageTranslationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def language_translation_translate_deu_to_eng(self, input, **kwargs):  # noqa: E501
        """Translate German to English text with Deep Learning AI  # noqa: E501

        Automatically translates input text in German to output text in English using advanced Deep Learning and Neural NLP.  Consumes 1-2 API calls per input sentence.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.language_translation_translate_deu_to_eng(input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LanguageTranslationRequest input: Input translation request (required)
        :return: LanguageTranslationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.language_translation_translate_deu_to_eng_with_http_info(input, **kwargs)  # noqa: E501
        else:
            (data) = self.language_translation_translate_deu_to_eng_with_http_info(input, **kwargs)  # noqa: E501
            return data

    def language_translation_translate_deu_to_eng_with_http_info(self, input, **kwargs):  # noqa: E501
        """Translate German to English text with Deep Learning AI  # noqa: E501

        Automatically translates input text in German to output text in English using advanced Deep Learning and Neural NLP.  Consumes 1-2 API calls per input sentence.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.language_translation_translate_deu_to_eng_with_http_info(input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LanguageTranslationRequest input: Input translation request (required)
        :return: LanguageTranslationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['input']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method language_translation_translate_deu_to_eng" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input' is set
        if ('input' not in params or
                params['input'] is None):
            raise ValueError("Missing the required parameter `input` when calling `language_translation_translate_deu_to_eng`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input' in params:
            body_params = params['input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/nlp-v2/translate/language/deu/to/eng', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LanguageTranslationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def language_translation_translate_eng_to_deu(self, input, **kwargs):  # noqa: E501
        """Translate English to German text with Deep Learning AI  # noqa: E501

        Automatically translates input text in English to output text in German using advanced Deep Learning and Neural NLP.  Consumes 1-2 API calls per input sentence.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.language_translation_translate_eng_to_deu(input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LanguageTranslationRequest input: Input translation request (required)
        :return: LanguageTranslationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.language_translation_translate_eng_to_deu_with_http_info(input, **kwargs)  # noqa: E501
        else:
            (data) = self.language_translation_translate_eng_to_deu_with_http_info(input, **kwargs)  # noqa: E501
            return data

    def language_translation_translate_eng_to_deu_with_http_info(self, input, **kwargs):  # noqa: E501
        """Translate English to German text with Deep Learning AI  # noqa: E501

        Automatically translates input text in English to output text in German using advanced Deep Learning and Neural NLP.  Consumes 1-2 API calls per input sentence.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.language_translation_translate_eng_to_deu_with_http_info(input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LanguageTranslationRequest input: Input translation request (required)
        :return: LanguageTranslationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['input']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method language_translation_translate_eng_to_deu" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input' is set
        if ('input' not in params or
                params['input'] is None):
            raise ValueError("Missing the required parameter `input` when calling `language_translation_translate_eng_to_deu`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input' in params:
            body_params = params['input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/nlp-v2/translate/language/eng/to/deu', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LanguageTranslationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
