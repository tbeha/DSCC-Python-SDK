# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from dscc.models.nimble_events_list import NimbleEventsList
from dscc.models.nimble_events_with_request_uri import NimbleEventsWithRequestUri

from dscc.api_client import ApiClient, RequestSerialized
from dscc.api_response import ApiResponse
from dscc.rest import RESTResponseType


class AuditEventApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def device_type2_get_events(
        self,
        system_id: Annotated[StrictStr, Field(description="ID of the storage system")],
        limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Number of items to return at a time")] = None,
        offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="The offset of the first item in the collection to return")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="Lucene query to filter Events by Key.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="oData query to sort Event resource by Key.")] = None,
        select: Annotated[Optional[StrictStr], Field(description="Query to select only the required parameters, separated by . if nested")] = None,
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
    ) -> NimbleEventsList:
        """Get all events of Nimble / Alletra 6K

        Get all events of Nimble / Alletra 6K

        :param system_id: ID of the storage system (required)
        :type system_id: str
        :param limit: Number of items to return at a time
        :type limit: int
        :param offset: The offset of the first item in the collection to return
        :type offset: int
        :param filter: Lucene query to filter Events by Key.
        :type filter: str
        :param sort: oData query to sort Event resource by Key.
        :type sort: str
        :param select: Query to select only the required parameters, separated by . if nested
        :type select: str
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

        _param = self._device_type2_get_events_serialize(
            system_id=system_id,
            limit=limit,
            offset=offset,
            filter=filter,
            sort=sort,
            select=select,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NimbleEventsList",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def device_type2_get_events_with_http_info(
        self,
        system_id: Annotated[StrictStr, Field(description="ID of the storage system")],
        limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Number of items to return at a time")] = None,
        offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="The offset of the first item in the collection to return")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="Lucene query to filter Events by Key.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="oData query to sort Event resource by Key.")] = None,
        select: Annotated[Optional[StrictStr], Field(description="Query to select only the required parameters, separated by . if nested")] = None,
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
    ) -> ApiResponse[NimbleEventsList]:
        """Get all events of Nimble / Alletra 6K

        Get all events of Nimble / Alletra 6K

        :param system_id: ID of the storage system (required)
        :type system_id: str
        :param limit: Number of items to return at a time
        :type limit: int
        :param offset: The offset of the first item in the collection to return
        :type offset: int
        :param filter: Lucene query to filter Events by Key.
        :type filter: str
        :param sort: oData query to sort Event resource by Key.
        :type sort: str
        :param select: Query to select only the required parameters, separated by . if nested
        :type select: str
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

        _param = self._device_type2_get_events_serialize(
            system_id=system_id,
            limit=limit,
            offset=offset,
            filter=filter,
            sort=sort,
            select=select,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NimbleEventsList",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def device_type2_get_events_without_preload_content(
        self,
        system_id: Annotated[StrictStr, Field(description="ID of the storage system")],
        limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Number of items to return at a time")] = None,
        offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="The offset of the first item in the collection to return")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="Lucene query to filter Events by Key.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="oData query to sort Event resource by Key.")] = None,
        select: Annotated[Optional[StrictStr], Field(description="Query to select only the required parameters, separated by . if nested")] = None,
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
        """Get all events of Nimble / Alletra 6K

        Get all events of Nimble / Alletra 6K

        :param system_id: ID of the storage system (required)
        :type system_id: str
        :param limit: Number of items to return at a time
        :type limit: int
        :param offset: The offset of the first item in the collection to return
        :type offset: int
        :param filter: Lucene query to filter Events by Key.
        :type filter: str
        :param sort: oData query to sort Event resource by Key.
        :type sort: str
        :param select: Query to select only the required parameters, separated by . if nested
        :type select: str
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

        _param = self._device_type2_get_events_serialize(
            system_id=system_id,
            limit=limit,
            offset=offset,
            filter=filter,
            sort=sort,
            select=select,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NimbleEventsList",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _device_type2_get_events_serialize(
        self,
        system_id,
        limit,
        offset,
        filter,
        sort,
        select,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if system_id is not None:
            _path_params['systemId'] = system_id
        # process the query parameters
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
        if filter is not None:
            
            _query_params.append(('filter', filter))
            
        if sort is not None:
            
            _query_params.append(('sort', sort))
            
        if select is not None:
            
            _query_params.append(('select', select))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'JWTAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/storage-systems/device-type2/{systemId}/events',
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




    @validate_call
    def device_type2_get_events_using_event_id(
        self,
        system_id: Annotated[StrictStr, Field(description="ID of the storage system")],
        event_id: Annotated[StrictStr, Field(description="ID of the Event. A 42 digit hexadecimal number.")],
        select: Annotated[Optional[StrictStr], Field(description="Query to select only the required parameters, separated by . if nested")] = None,
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
    ) -> NimbleEventsWithRequestUri:
        """Get all events of Nimble / Alletra 6K identified by {eventId}

        Get all events of Nimble / Alletra 6K indentified by {eventId}

        :param system_id: ID of the storage system (required)
        :type system_id: str
        :param event_id: ID of the Event. A 42 digit hexadecimal number. (required)
        :type event_id: str
        :param select: Query to select only the required parameters, separated by . if nested
        :type select: str
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

        _param = self._device_type2_get_events_using_event_id_serialize(
            system_id=system_id,
            event_id=event_id,
            select=select,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NimbleEventsWithRequestUri",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def device_type2_get_events_using_event_id_with_http_info(
        self,
        system_id: Annotated[StrictStr, Field(description="ID of the storage system")],
        event_id: Annotated[StrictStr, Field(description="ID of the Event. A 42 digit hexadecimal number.")],
        select: Annotated[Optional[StrictStr], Field(description="Query to select only the required parameters, separated by . if nested")] = None,
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
    ) -> ApiResponse[NimbleEventsWithRequestUri]:
        """Get all events of Nimble / Alletra 6K identified by {eventId}

        Get all events of Nimble / Alletra 6K indentified by {eventId}

        :param system_id: ID of the storage system (required)
        :type system_id: str
        :param event_id: ID of the Event. A 42 digit hexadecimal number. (required)
        :type event_id: str
        :param select: Query to select only the required parameters, separated by . if nested
        :type select: str
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

        _param = self._device_type2_get_events_using_event_id_serialize(
            system_id=system_id,
            event_id=event_id,
            select=select,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NimbleEventsWithRequestUri",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def device_type2_get_events_using_event_id_without_preload_content(
        self,
        system_id: Annotated[StrictStr, Field(description="ID of the storage system")],
        event_id: Annotated[StrictStr, Field(description="ID of the Event. A 42 digit hexadecimal number.")],
        select: Annotated[Optional[StrictStr], Field(description="Query to select only the required parameters, separated by . if nested")] = None,
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
        """Get all events of Nimble / Alletra 6K identified by {eventId}

        Get all events of Nimble / Alletra 6K indentified by {eventId}

        :param system_id: ID of the storage system (required)
        :type system_id: str
        :param event_id: ID of the Event. A 42 digit hexadecimal number. (required)
        :type event_id: str
        :param select: Query to select only the required parameters, separated by . if nested
        :type select: str
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

        _param = self._device_type2_get_events_using_event_id_serialize(
            system_id=system_id,
            event_id=event_id,
            select=select,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NimbleEventsWithRequestUri",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _device_type2_get_events_using_event_id_serialize(
        self,
        system_id,
        event_id,
        select,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if system_id is not None:
            _path_params['systemId'] = system_id
        if event_id is not None:
            _path_params['eventId'] = event_id
        # process the query parameters
        if select is not None:
            
            _query_params.append(('select', select))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'JWTAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/storage-systems/device-type2/{systemId}/events/{eventId}',
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


