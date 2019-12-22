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


class PosTaggerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pos_tagger_tag_adjectives(self, request, **kwargs):  # noqa: E501
        """Part-of-speech tag a string, filter to adjectives  # noqa: E501

        Part-of-speech (POS) tag a string, find the adjectives, and return result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pos_tagger_tag_adjectives(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PosRequest request: Input string (required)
        :return: PosResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pos_tagger_tag_adjectives_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.pos_tagger_tag_adjectives_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def pos_tagger_tag_adjectives_with_http_info(self, request, **kwargs):  # noqa: E501
        """Part-of-speech tag a string, filter to adjectives  # noqa: E501

        Part-of-speech (POS) tag a string, find the adjectives, and return result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pos_tagger_tag_adjectives_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PosRequest request: Input string (required)
        :return: PosResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pos_tagger_tag_adjectives" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `pos_tagger_tag_adjectives`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/nlp-v2/pos/tag/adjectives', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PosResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pos_tagger_tag_adverbs(self, request, **kwargs):  # noqa: E501
        """Part-of-speech tag a string, filter to adverbs  # noqa: E501

        Part-of-speech (POS) tag a string, find the adverbs, and return result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pos_tagger_tag_adverbs(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PosRequest request: Input string (required)
        :return: PosResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pos_tagger_tag_adverbs_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.pos_tagger_tag_adverbs_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def pos_tagger_tag_adverbs_with_http_info(self, request, **kwargs):  # noqa: E501
        """Part-of-speech tag a string, filter to adverbs  # noqa: E501

        Part-of-speech (POS) tag a string, find the adverbs, and return result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pos_tagger_tag_adverbs_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PosRequest request: Input string (required)
        :return: PosResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pos_tagger_tag_adverbs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `pos_tagger_tag_adverbs`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/nlp-v2/pos/tag/adverbs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PosResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pos_tagger_tag_nouns(self, request, **kwargs):  # noqa: E501
        """Part-of-speech tag a string, filter to nouns  # noqa: E501

        Part-of-speech (POS) tag a string, find the nouns, and return result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pos_tagger_tag_nouns(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PosRequest request: Input string (required)
        :return: PosResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pos_tagger_tag_nouns_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.pos_tagger_tag_nouns_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def pos_tagger_tag_nouns_with_http_info(self, request, **kwargs):  # noqa: E501
        """Part-of-speech tag a string, filter to nouns  # noqa: E501

        Part-of-speech (POS) tag a string, find the nouns, and return result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pos_tagger_tag_nouns_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PosRequest request: Input string (required)
        :return: PosResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pos_tagger_tag_nouns" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `pos_tagger_tag_nouns`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/nlp-v2/pos/tag/nouns', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PosResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pos_tagger_tag_pronouns(self, request, **kwargs):  # noqa: E501
        """Part-of-speech tag a string, filter to pronouns  # noqa: E501

        Part-of-speech (POS) tag a string, find the pronouns, and return result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pos_tagger_tag_pronouns(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PosRequest request: Input string (required)
        :return: PosResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pos_tagger_tag_pronouns_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.pos_tagger_tag_pronouns_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def pos_tagger_tag_pronouns_with_http_info(self, request, **kwargs):  # noqa: E501
        """Part-of-speech tag a string, filter to pronouns  # noqa: E501

        Part-of-speech (POS) tag a string, find the pronouns, and return result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pos_tagger_tag_pronouns_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PosRequest request: Input string (required)
        :return: PosResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pos_tagger_tag_pronouns" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `pos_tagger_tag_pronouns`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/nlp-v2/pos/tag/pronouns', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PosResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pos_tagger_tag_sentence(self, request, **kwargs):  # noqa: E501
        """Part-of-speech tag a string  # noqa: E501

        Part-of-speech (POS) tag a string and return result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pos_tagger_tag_sentence(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PosRequest request: Input string (required)
        :return: PosResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pos_tagger_tag_sentence_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.pos_tagger_tag_sentence_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def pos_tagger_tag_sentence_with_http_info(self, request, **kwargs):  # noqa: E501
        """Part-of-speech tag a string  # noqa: E501

        Part-of-speech (POS) tag a string and return result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pos_tagger_tag_sentence_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PosRequest request: Input string (required)
        :return: PosResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pos_tagger_tag_sentence" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `pos_tagger_tag_sentence`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/nlp-v2/pos/tag/sentence', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PosResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pos_tagger_tag_verbs(self, request, **kwargs):  # noqa: E501
        """Part-of-speech tag a string, filter to verbs  # noqa: E501

        Part-of-speech (POS) tag a string, find the verbs, and return result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pos_tagger_tag_verbs(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PosRequest request: Input string (required)
        :return: PosResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pos_tagger_tag_verbs_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.pos_tagger_tag_verbs_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def pos_tagger_tag_verbs_with_http_info(self, request, **kwargs):  # noqa: E501
        """Part-of-speech tag a string, filter to verbs  # noqa: E501

        Part-of-speech (POS) tag a string, find the verbs, and return result as JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pos_tagger_tag_verbs_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PosRequest request: Input string (required)
        :return: PosResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pos_tagger_tag_verbs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `pos_tagger_tag_verbs`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/nlp-v2/pos/tag/verbs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PosResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)