# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.33.61.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_client.models.global_search_query import GlobalSearchQuery
from openapi_client.models.global_search_result_page import GlobalSearchResultPage

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class GlobalSearchApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def search_global(
        self,
        token: Annotated[Optional[StrictStr], Field(description="Auth token as query parameter (alternative to Authorization header).")] = None,
        act_as_admin: Annotated[Optional[StrictBool], Field(description="Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="How many elements to skip.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=1000, strict=True, ge=0)]], Field(description="How many elements to return.")] = None,
        var_from: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="From which element the page should start.")] = None,
        to: Annotated[Optional[StrictInt], Field(description="At which element the page should end (excluding it).")] = None,
        global_search_query: Optional[GlobalSearchQuery] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> GlobalSearchResultPage:
        """search_global

        Requirements:<br/>- auth-client scopes: \"workspace:read\"

        :param token: Auth token as query parameter (alternative to Authorization header).
        :type token: str
        :param act_as_admin: Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team.
        :type act_as_admin: bool
        :param offset: How many elements to skip.
        :type offset: int
        :param limit: How many elements to return.
        :type limit: int
        :param var_from: From which element the page should start.
        :type var_from: int
        :param to: At which element the page should end (excluding it).
        :type to: int
        :param global_search_query:
        :type global_search_query: GlobalSearchQuery
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._search_global_serialize(
            token=token,
            act_as_admin=act_as_admin,
            offset=offset,
            limit=limit,
            var_from=var_from,
            to=to,
            global_search_query=global_search_query,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GlobalSearchResultPage",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def search_global_with_http_info(
        self,
        token: Annotated[Optional[StrictStr], Field(description="Auth token as query parameter (alternative to Authorization header).")] = None,
        act_as_admin: Annotated[Optional[StrictBool], Field(description="Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="How many elements to skip.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=1000, strict=True, ge=0)]], Field(description="How many elements to return.")] = None,
        var_from: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="From which element the page should start.")] = None,
        to: Annotated[Optional[StrictInt], Field(description="At which element the page should end (excluding it).")] = None,
        global_search_query: Optional[GlobalSearchQuery] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[GlobalSearchResultPage]:
        """search_global

        Requirements:<br/>- auth-client scopes: \"workspace:read\"

        :param token: Auth token as query parameter (alternative to Authorization header).
        :type token: str
        :param act_as_admin: Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team.
        :type act_as_admin: bool
        :param offset: How many elements to skip.
        :type offset: int
        :param limit: How many elements to return.
        :type limit: int
        :param var_from: From which element the page should start.
        :type var_from: int
        :param to: At which element the page should end (excluding it).
        :type to: int
        :param global_search_query:
        :type global_search_query: GlobalSearchQuery
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._search_global_serialize(
            token=token,
            act_as_admin=act_as_admin,
            offset=offset,
            limit=limit,
            var_from=var_from,
            to=to,
            global_search_query=global_search_query,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GlobalSearchResultPage",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def search_global_without_preload_content(
        self,
        token: Annotated[Optional[StrictStr], Field(description="Auth token as query parameter (alternative to Authorization header).")] = None,
        act_as_admin: Annotated[Optional[StrictBool], Field(description="Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="How many elements to skip.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=1000, strict=True, ge=0)]], Field(description="How many elements to return.")] = None,
        var_from: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="From which element the page should start.")] = None,
        to: Annotated[Optional[StrictInt], Field(description="At which element the page should end (excluding it).")] = None,
        global_search_query: Optional[GlobalSearchQuery] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """search_global

        Requirements:<br/>- auth-client scopes: \"workspace:read\"

        :param token: Auth token as query parameter (alternative to Authorization header).
        :type token: str
        :param act_as_admin: Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team.
        :type act_as_admin: bool
        :param offset: How many elements to skip.
        :type offset: int
        :param limit: How many elements to return.
        :type limit: int
        :param var_from: From which element the page should start.
        :type var_from: int
        :param to: At which element the page should end (excluding it).
        :type to: int
        :param global_search_query:
        :type global_search_query: GlobalSearchQuery
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._search_global_serialize(
            token=token,
            act_as_admin=act_as_admin,
            offset=offset,
            limit=limit,
            var_from=var_from,
            to=to,
            global_search_query=global_search_query,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GlobalSearchResultPage",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _search_global_serialize(
        self,
        token,
        act_as_admin,
        offset,
        limit,
        var_from,
        to,
        global_search_query,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if token is not None:
            
            _query_params.append(('token', token))
            
        if act_as_admin is not None:
            
            _query_params.append(('actAsAdmin', act_as_admin))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if var_from is not None:
            
            _query_params.append(('from', var_from))
            
        if to is not None:
            
            _query_params.append(('to', to))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if global_search_query is not None:
            _body_params = global_search_query


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'httpAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/workspaces/global-search',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


