# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dscc.models.associated_links_inner import AssociatedLinksInner
from dscc.models.nimble_common_resource_attributes import NimbleCommonResourceAttributes
from dscc.models.replication_throttle import ReplicationThrottle
from dscc.models.replication_volume_collection_summary import ReplicationVolumeCollectionSummary
from typing import Optional, Set
from typing_extensions import Self

class NimbleReplicationPartnerCommon(BaseModel):
    """
    NimbleReplicationPartnerCommon
    """ # noqa: E501
    alias: Optional[StrictStr] = Field(default=None, description="String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen.")
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details")
    common_resource_attributes: Optional[NimbleCommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    control_port: Optional[StrictInt] = Field(default=None, description="Port number of partner control interface. Value -1 for an invalid port or a positive integer value up to 65535 representing the TCP/IP port.")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    data_port: Optional[StrictInt] = Field(default=None, description="Port number of partner data interface. Value -1 for an invalid port or a positive integer value up to 65535 representing the TCP/IP port.")
    description: Optional[StrictStr] = Field(default=None, description="Description of replication partner. String of up to 255 printable ASCII characters.")
    full_name: Optional[StrictStr] = Field(default=None, description="Fully qualified name of replication partner. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    last_keepalive_error: Optional[StrictStr] = Field(default=None, description="Most recent error while attempting to ping the partner. Plain string.")
    last_modified: Optional[StrictInt] = Field(default=None, description="Time when this replication partner was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970.")
    last_sync_error: Optional[StrictStr] = Field(default=None, description="Most recent error seen while attempting to sync objects to the partner. Plain string.")
    match_folder: Optional[StrictBool] = Field(default=None, description="Indicates whether to match the upstream volumes folder on the downstream. Possible values: true, false")
    partner_group_uid: Optional[StrictInt] = Field(default=None, description="Replication partner group uid. Unsigned 64-bit integer.")
    port_range_start: Optional[StrictInt] = Field(default=None, description="Positive integer value up to 65535 representing TCP/IP port. Example: 1234.")
    proxy_hostname: Optional[StrictStr] = Field(default=None, description="String of up to 64 alphanumeric characters, - and . and : are allowed after first character. Example: 'myobject-5'")
    proxy_user: Optional[StrictStr] = Field(default=None, description="HTTP proxy server username, string up to 255 characters, special characters ([, ], `, ;, ampersand, tab, space, newline) are not allowed.")
    remote_partner_folder_id: Optional[StrictStr] = Field(default=None, description="The folder ID where volumes replicated from remote partner will be created. Replica volumes created as clones ignore this parameter and are always created in the same pool as their parent volume. A 42 digit hexadecimal number.")
    remote_partner_folder_name: Optional[StrictStr] = Field(default=None, description="The folder name where volumes replicated from remote partner will be created. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. Example: 'myobject-5'.")
    remote_partner_id: Optional[StrictStr] = Field(default=None, description="ID of the remote partner.")
    remote_partner_name: Optional[StrictStr] = Field(default=None, description="Name of the remote partner. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. Example: 'myobject-5'.")
    remote_partner_pool_id: Optional[StrictStr] = Field(default=None, description="The pool ID where volumes replicated from remote partner will be created. Replica volumes created as clones ignore this parameter and are always created in the same pool as their parent volume. A 42 digit hexadecimal number.")
    remote_partner_pool_name: Optional[StrictStr] = Field(default=None, description="The pool name where volumes replicated from remote partner will be created. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. Example: 'myobject-5'.")
    remote_partner_subnet_label: Optional[StrictStr] = Field(default=None, description="Label of the subnet used to replicate to remote partner. String of up to 64 alphanumeric characters, - and . and colon are allowed after first character.")
    remote_partner_subnet_type: Optional[StrictStr] = Field(default=None, description="Type of the subnet used to replicate to the remote partner. Possible values are 'invalid', 'unconfigured', 'mgmt', 'data', 'mgmt_data'.")
    remote_partner_system_id: Optional[StrictStr] = Field(default=None, description="ID of the system to which the remote partner belongs.")
    replication_direction: Optional[StrictStr] = Field(default=None, description="Direction of replication configured with this partner. Possible values: none, downstream, upstream, bi_directional")
    search_name: Optional[StrictStr] = Field(default=None, description="Name of replication partner used for object search. Alphanumeric string, up to 64 characters including hyphen, period, colon.")
    status: Optional[StrictStr] = Field(default=None, description="Status of the partner. Failed, Normal, Degraded, Unknown.")
    throttled_bandwidth_current: Optional[StrictInt] = Field(default=None, description="Current bandwidth throttle for this partner, expressed either as megabits per second or as -1 to indicate that there is no throttle. Signed 64-bit integer.")
    throttled_bandwidth_current_kbps: Optional[StrictInt] = Field(default=None, description="Current bandwidth throttle for this partner, expressed either as kilobits per second or as -1 to indicate that there is no throttle. Signed 64-bit integer.")
    throttles: Optional[List[Optional[ReplicationThrottle]]] = Field(default=None, description="Throttles used while replicating from/to this partner. All the throttles for the partner.")
    type: Optional[StrictStr] = Field(default=None, description="type")
    unique_name: Optional[StrictBool] = Field(default=None, description="Possible values: 'true', 'false'.")
    volume_collection_list: Optional[List[Optional[ReplicationVolumeCollectionSummary]]] = Field(default=None, description="List of volume collections that are replicating from/to this partner. List of volume collections.")
    witness: Optional[StrictStr] = Field(default=None, description="Hostname or ip addresses of witness. Comma separated strings of up to 63 characters of hostname and/or ip addresses. Total length cannot exceed 255 characters.")
    __properties: ClassVar[List[str]] = ["alias", "associated_links", "commonResourceAttributes", "control_port", "customerId", "data_port", "description", "full_name", "generation", "last_keepalive_error", "last_modified", "last_sync_error", "match_folder", "partner_group_uid", "port_range_start", "proxy_hostname", "proxy_user", "remote_partner_folder_id", "remote_partner_folder_name", "remote_partner_id", "remote_partner_name", "remote_partner_pool_id", "remote_partner_pool_name", "remote_partner_subnet_label", "remote_partner_subnet_type", "remote_partner_system_id", "replication_direction", "search_name", "status", "throttled_bandwidth_current", "throttled_bandwidth_current_kbps", "throttles", "type", "unique_name", "volume_collection_list", "witness"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of NimbleReplicationPartnerCommon from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in associated_links (list)
        _items = []
        if self.associated_links:
            for _item in self.associated_links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['associated_links'] = _items
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in throttles (list)
        _items = []
        if self.throttles:
            for _item in self.throttles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['throttles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in volume_collection_list (list)
        _items = []
        if self.volume_collection_list:
            for _item in self.volume_collection_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volume_collection_list'] = _items
        # set to None if alias (nullable) is None
        # and model_fields_set contains the field
        if self.alias is None and "alias" in self.model_fields_set:
            _dict['alias'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if control_port (nullable) is None
        # and model_fields_set contains the field
        if self.control_port is None and "control_port" in self.model_fields_set:
            _dict['control_port'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if data_port (nullable) is None
        # and model_fields_set contains the field
        if self.data_port is None and "data_port" in self.model_fields_set:
            _dict['data_port'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if full_name (nullable) is None
        # and model_fields_set contains the field
        if self.full_name is None and "full_name" in self.model_fields_set:
            _dict['full_name'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if last_keepalive_error (nullable) is None
        # and model_fields_set contains the field
        if self.last_keepalive_error is None and "last_keepalive_error" in self.model_fields_set:
            _dict['last_keepalive_error'] = None

        # set to None if last_modified (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified is None and "last_modified" in self.model_fields_set:
            _dict['last_modified'] = None

        # set to None if last_sync_error (nullable) is None
        # and model_fields_set contains the field
        if self.last_sync_error is None and "last_sync_error" in self.model_fields_set:
            _dict['last_sync_error'] = None

        # set to None if match_folder (nullable) is None
        # and model_fields_set contains the field
        if self.match_folder is None and "match_folder" in self.model_fields_set:
            _dict['match_folder'] = None

        # set to None if partner_group_uid (nullable) is None
        # and model_fields_set contains the field
        if self.partner_group_uid is None and "partner_group_uid" in self.model_fields_set:
            _dict['partner_group_uid'] = None

        # set to None if port_range_start (nullable) is None
        # and model_fields_set contains the field
        if self.port_range_start is None and "port_range_start" in self.model_fields_set:
            _dict['port_range_start'] = None

        # set to None if proxy_hostname (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_hostname is None and "proxy_hostname" in self.model_fields_set:
            _dict['proxy_hostname'] = None

        # set to None if proxy_user (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_user is None and "proxy_user" in self.model_fields_set:
            _dict['proxy_user'] = None

        # set to None if remote_partner_folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.remote_partner_folder_id is None and "remote_partner_folder_id" in self.model_fields_set:
            _dict['remote_partner_folder_id'] = None

        # set to None if remote_partner_folder_name (nullable) is None
        # and model_fields_set contains the field
        if self.remote_partner_folder_name is None and "remote_partner_folder_name" in self.model_fields_set:
            _dict['remote_partner_folder_name'] = None

        # set to None if remote_partner_id (nullable) is None
        # and model_fields_set contains the field
        if self.remote_partner_id is None and "remote_partner_id" in self.model_fields_set:
            _dict['remote_partner_id'] = None

        # set to None if remote_partner_name (nullable) is None
        # and model_fields_set contains the field
        if self.remote_partner_name is None and "remote_partner_name" in self.model_fields_set:
            _dict['remote_partner_name'] = None

        # set to None if remote_partner_pool_id (nullable) is None
        # and model_fields_set contains the field
        if self.remote_partner_pool_id is None and "remote_partner_pool_id" in self.model_fields_set:
            _dict['remote_partner_pool_id'] = None

        # set to None if remote_partner_pool_name (nullable) is None
        # and model_fields_set contains the field
        if self.remote_partner_pool_name is None and "remote_partner_pool_name" in self.model_fields_set:
            _dict['remote_partner_pool_name'] = None

        # set to None if remote_partner_subnet_type (nullable) is None
        # and model_fields_set contains the field
        if self.remote_partner_subnet_type is None and "remote_partner_subnet_type" in self.model_fields_set:
            _dict['remote_partner_subnet_type'] = None

        # set to None if remote_partner_system_id (nullable) is None
        # and model_fields_set contains the field
        if self.remote_partner_system_id is None and "remote_partner_system_id" in self.model_fields_set:
            _dict['remote_partner_system_id'] = None

        # set to None if replication_direction (nullable) is None
        # and model_fields_set contains the field
        if self.replication_direction is None and "replication_direction" in self.model_fields_set:
            _dict['replication_direction'] = None

        # set to None if search_name (nullable) is None
        # and model_fields_set contains the field
        if self.search_name is None and "search_name" in self.model_fields_set:
            _dict['search_name'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if throttled_bandwidth_current (nullable) is None
        # and model_fields_set contains the field
        if self.throttled_bandwidth_current is None and "throttled_bandwidth_current" in self.model_fields_set:
            _dict['throttled_bandwidth_current'] = None

        # set to None if throttled_bandwidth_current_kbps (nullable) is None
        # and model_fields_set contains the field
        if self.throttled_bandwidth_current_kbps is None and "throttled_bandwidth_current_kbps" in self.model_fields_set:
            _dict['throttled_bandwidth_current_kbps'] = None

        # set to None if throttles (nullable) is None
        # and model_fields_set contains the field
        if self.throttles is None and "throttles" in self.model_fields_set:
            _dict['throttles'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if volume_collection_list (nullable) is None
        # and model_fields_set contains the field
        if self.volume_collection_list is None and "volume_collection_list" in self.model_fields_set:
            _dict['volume_collection_list'] = None

        # set to None if witness (nullable) is None
        # and model_fields_set contains the field
        if self.witness is None and "witness" in self.model_fields_set:
            _dict['witness'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleReplicationPartnerCommon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alias": obj.get("alias"),
            "associated_links": [AssociatedLinksInner.from_dict(_item) for _item in obj["associated_links"]] if obj.get("associated_links") is not None else None,
            "commonResourceAttributes": NimbleCommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "control_port": obj.get("control_port"),
            "customerId": obj.get("customerId"),
            "data_port": obj.get("data_port"),
            "description": obj.get("description"),
            "full_name": obj.get("full_name"),
            "generation": obj.get("generation"),
            "last_keepalive_error": obj.get("last_keepalive_error"),
            "last_modified": obj.get("last_modified"),
            "last_sync_error": obj.get("last_sync_error"),
            "match_folder": obj.get("match_folder"),
            "partner_group_uid": obj.get("partner_group_uid"),
            "port_range_start": obj.get("port_range_start"),
            "proxy_hostname": obj.get("proxy_hostname"),
            "proxy_user": obj.get("proxy_user"),
            "remote_partner_folder_id": obj.get("remote_partner_folder_id"),
            "remote_partner_folder_name": obj.get("remote_partner_folder_name"),
            "remote_partner_id": obj.get("remote_partner_id"),
            "remote_partner_name": obj.get("remote_partner_name"),
            "remote_partner_pool_id": obj.get("remote_partner_pool_id"),
            "remote_partner_pool_name": obj.get("remote_partner_pool_name"),
            "remote_partner_subnet_label": obj.get("remote_partner_subnet_label"),
            "remote_partner_subnet_type": obj.get("remote_partner_subnet_type"),
            "remote_partner_system_id": obj.get("remote_partner_system_id"),
            "replication_direction": obj.get("replication_direction"),
            "search_name": obj.get("search_name"),
            "status": obj.get("status"),
            "throttled_bandwidth_current": obj.get("throttled_bandwidth_current"),
            "throttled_bandwidth_current_kbps": obj.get("throttled_bandwidth_current_kbps"),
            "throttles": [ReplicationThrottle.from_dict(_item) for _item in obj["throttles"]] if obj.get("throttles") is not None else None,
            "type": obj.get("type"),
            "unique_name": obj.get("unique_name"),
            "volume_collection_list": [ReplicationVolumeCollectionSummary.from_dict(_item) for _item in obj["volume_collection_list"]] if obj.get("volume_collection_list") is not None else None,
            "witness": obj.get("witness")
        })
        return _obj


