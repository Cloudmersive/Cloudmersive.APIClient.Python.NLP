# coding: utf-8

"""
    nlpapi

    The powerful Natural Language Processing APIs let you perform part of speech tagging, entity identification, sentence parsing, and much more to help you understand the meaning of unstructured text.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudmersive_nlp_api_client.api_client import ApiClient


class SpellCheckApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def spell_check_check_json(self, value, **kwargs):  # noqa: E501
        """Spell check word  # noqa: E501

        Spell check a word as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.spell_check_check_json(value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str value: Input sentence (required)
        :return: CheckJsonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.spell_check_check_json_with_http_info(value, **kwargs)  # noqa: E501
        else:
            (data) = self.spell_check_check_json_with_http_info(value, **kwargs)  # noqa: E501
            return data

    def spell_check_check_json_with_http_info(self, value, **kwargs):  # noqa: E501
        """Spell check word  # noqa: E501

        Spell check a word as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.spell_check_check_json_with_http_info(value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str value: Input sentence (required)
        :return: CheckJsonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['value']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spell_check_check_json" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'value' is set
        if ('value' not in params or
                params['value'] is None):
            raise ValueError("Missing the required parameter `value` when calling `spell_check_check_json`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'value' in params:
            body_params = params['value']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/nlp/spellcheck/check/word/json', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CheckJsonResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def spell_check_check_sentence_json(self, value, **kwargs):  # noqa: E501
        """Check if sentence is spelled correctly  # noqa: E501

        Checks whether the sentence is spelled correctly and returns the result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.spell_check_check_sentence_json(value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str value: Input sentence (required)
        :return: CheckSentenceJsonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.spell_check_check_sentence_json_with_http_info(value, **kwargs)  # noqa: E501
        else:
            (data) = self.spell_check_check_sentence_json_with_http_info(value, **kwargs)  # noqa: E501
            return data

    def spell_check_check_sentence_json_with_http_info(self, value, **kwargs):  # noqa: E501
        """Check if sentence is spelled correctly  # noqa: E501

        Checks whether the sentence is spelled correctly and returns the result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.spell_check_check_sentence_json_with_http_info(value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str value: Input sentence (required)
        :return: CheckSentenceJsonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['value']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spell_check_check_sentence_json" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'value' is set
        if ('value' not in params or
                params['value'] is None):
            raise ValueError("Missing the required parameter `value` when calling `spell_check_check_sentence_json`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'value' in params:
            body_params = params['value']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/nlp/spellcheck/check/sentence/json', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CheckSentenceJsonResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def spell_check_check_sentence_string(self, value, **kwargs):  # noqa: E501
        """Spell check a sentence  # noqa: E501

        Check if a sentence is spelled correctly  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.spell_check_check_sentence_string(value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str value: Input sentence word (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.spell_check_check_sentence_string_with_http_info(value, **kwargs)  # noqa: E501
        else:
            (data) = self.spell_check_check_sentence_string_with_http_info(value, **kwargs)  # noqa: E501
            return data

    def spell_check_check_sentence_string_with_http_info(self, value, **kwargs):  # noqa: E501
        """Spell check a sentence  # noqa: E501

        Check if a sentence is spelled correctly  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.spell_check_check_sentence_string_with_http_info(value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str value: Input sentence word (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['value']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spell_check_check_sentence_string" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'value' is set
        if ('value' not in params or
                params['value'] is None):
            raise ValueError("Missing the required parameter `value` when calling `spell_check_check_sentence_string`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'value' in params:
            body_params = params['value']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/nlp/spellcheck/check/sentence/string', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def spell_check_correct(self, value, **kwargs):  # noqa: E501
        """Find spelling corrections  # noqa: E501

        Find the spelling corrections for a word  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.spell_check_correct(value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str value: Input word (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.spell_check_correct_with_http_info(value, **kwargs)  # noqa: E501
        else:
            (data) = self.spell_check_correct_with_http_info(value, **kwargs)  # noqa: E501
            return data

    def spell_check_correct_with_http_info(self, value, **kwargs):  # noqa: E501
        """Find spelling corrections  # noqa: E501

        Find the spelling corrections for a word  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.spell_check_correct_with_http_info(value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str value: Input word (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['value']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spell_check_correct" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'value' is set
        if ('value' not in params or
                params['value'] is None):
            raise ValueError("Missing the required parameter `value` when calling `spell_check_correct`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'value' in params:
            body_params = params['value']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/nlp/spellcheck/correct/word/string', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def spell_check_correct_json(self, value, **kwargs):  # noqa: E501
        """Find spelling corrections  # noqa: E501

        Find spelling correction suggestions and return result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.spell_check_correct_json(value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str value: Input string (required)
        :return: CorrectJsonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.spell_check_correct_json_with_http_info(value, **kwargs)  # noqa: E501
        else:
            (data) = self.spell_check_correct_json_with_http_info(value, **kwargs)  # noqa: E501
            return data

    def spell_check_correct_json_with_http_info(self, value, **kwargs):  # noqa: E501
        """Find spelling corrections  # noqa: E501

        Find spelling correction suggestions and return result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.spell_check_correct_json_with_http_info(value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str value: Input string (required)
        :return: CorrectJsonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['value']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spell_check_correct_json" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'value' is set
        if ('value' not in params or
                params['value'] is None):
            raise ValueError("Missing the required parameter `value` when calling `spell_check_correct_json`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'value' in params:
            body_params = params['value']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/nlp/spellcheck/correct/word/json', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CorrectJsonResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def spell_check_post(self, value, **kwargs):  # noqa: E501
        """Spell check a word  # noqa: E501

        Check if a word is spelled correctly  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.spell_check_post(value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str value: Input string word (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.spell_check_post_with_http_info(value, **kwargs)  # noqa: E501
        else:
            (data) = self.spell_check_post_with_http_info(value, **kwargs)  # noqa: E501
            return data

    def spell_check_post_with_http_info(self, value, **kwargs):  # noqa: E501
        """Spell check a word  # noqa: E501

        Check if a word is spelled correctly  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.spell_check_post_with_http_info(value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str value: Input string word (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['value']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spell_check_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'value' is set
        if ('value' not in params or
                params['value'] is None):
            raise ValueError("Missing the required parameter `value` when calling `spell_check_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'value' in params:
            body_params = params['value']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/nlp/spellcheck/check/word/string', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
