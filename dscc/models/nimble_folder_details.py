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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dscc.models.associated_links_inner import AssociatedLinksInner
from dscc.models.nimble_common_resource_attributes import NimbleCommonResourceAttributes
from dscc.models.nimble_volume_summary import NimbleVolumeSummary
from typing import Optional, Set
from typing_extensions import Self

class NimbleFolderDetails(BaseModel):
    """
    NimbleFolderDetails
    """ # noqa: E501
    access_protocol: Optional[StrictStr] = Field(default=None, description="Access protocol of the folder. This attribute is used by the VASA Provider to determine the access protocol of the bind request. If not specified in the creation request, it will be the access protocol supported by the group. If the group supports multiple protocols, the default will be Fibre Channel. This field is meaningful only to VVol folder. Possible values: 'iscsi', 'fc'.")
    agent_type: Optional[StrictStr] = Field(default=None, description="External management agent type. Possible values: 'none', 'smis', 'vvol', 'openstack'.")
    app_uuid: Optional[StrictStr] = Field(default=None, description="Application identifier of the folder.")
    appserver_id: Optional[StrictStr] = Field(default=None, description="Identifier of the application server associated with the folder.")
    appserver_name: Optional[StrictStr] = Field(default=None, description="Name of the application server associated with the folder.")
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details")
    capacity_bytes: Optional[StrictInt] = Field(default=None, description="Capacity of the folder in bytes. If the folder's size has a usage limit, capacity_bytes will be the folder's usage limit. If the folder's size does not have a usage limit, capacity_bytes will be the pool's capacity. This field is meaningful only when the usage_valid attribute is true.")
    common_resource_attributes: Optional[NimbleCommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    compressed_snap_usage_bytes: Optional[StrictInt] = Field(default=None, description="Compressed usage of snapshots in the folder. This field is meaningful only when the usage_valid attribute is true.")
    compressed_vol_usage_bytes: Optional[StrictInt] = Field(default=None, description="Compressed usage of volumes in the folder. This field is meaningful only when the usage_valid attribute is true.")
    compression_ratio: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Compression savings for the folder expressed as ratio. This field is meaningful only when the usage_valid attribute is true.")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    creation_time: Optional[StrictInt] = Field(default=None, description="Time when this folder was created.")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    description: Optional[StrictStr] = Field(default=None, description="Text description of folder.")
    folset_id: Optional[StrictStr] = Field(default=None, description="Identifier of the folder set associated with the folder. Only VVol folder can be associated with the folder set. The folder and the containing folder set must be associated with the same application server.")
    folset_name: Optional[StrictStr] = Field(default=None, description="Name of the folder set associated with the folder. Only VVol folder can be associated with the folder set. The folder and the containing folder set must be associated with the same application server.")
    fqn: Optional[StrictStr] = Field(default=None, description="Fully qualified name of folder in the pool.")
    free_space_bytes: Optional[StrictInt] = Field(default=None, description="Free space in the folder in bytes. If the folder has a usage limit, free_space_bytes will be the folder's free space (the folder's usage limit minus the folder's space usage). If the folder does not have a usage limit, free_space_bytes will be the pool's free space. This field is meaningful only when the usage_valid attribute is true.")
    full_name: Optional[StrictStr] = Field(default=None, description="Fully qualified name of folder in the group.")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    inherited_vol_perfpol_id: Optional[StrictStr] = Field(default=None, description="Identifier of the default performance policy for a newly created volume.")
    inherited_vol_perfpol_name: Optional[StrictStr] = Field(default=None, description="Name of the default performance policy for a newly created volume.")
    last_modified: Optional[StrictInt] = Field(default=None, description="Identifier of the default performance policy for a newly created volume.")
    limit_bytes: Optional[StrictInt] = Field(default=None, description="Folder limit size in bytes. By default, a folder (except SMIS and VVol types) does not have a limit. If limit_bytes is not specified when a folder is created, or if limit_bytes is set to the largest possible 64-bit signed integer (9223372036854775807), then the folder has no limit. Otherwise, a limit smaller than the capacity of the pool can be set. On output, if the folder has a limit, the limit_bytes_specified attribute will be true and limit_bytes will be the limit. If the folder does not have a limit, the limit_bytes_specified attribute will be false and limit_bytes will be interpreted based on the value of the usage_valid attribute. If the usage_valid attribute is true, limits_byte will be the capacity of the pool. Otherwise, limits_bytes is not meaningful and can be null. SMIS and VVol folders require a size limit. This attribute is superseded by limit_size_bytes.")
    limit_bytes_specified: Optional[StrictBool] = Field(default=None, description="Indicates whether the folder has a limit.")
    limit_iops: Optional[StrictInt] = Field(default=None, description="IOPS limit for this folder. If limit_iops is not specified when a folder is created, or if limit_iops is set to -1, then the folder has no IOPS limit. IOPS limit should be in range [256, 4294967294] or -1 for unlimited.")
    limit_mbps: Optional[StrictInt] = Field(default=None, description="Throughput limit for this folder in MB/s. If limit_mbps is not specified when a folder is created, or if limit_mbps is set to -1, then the folder has no throughput limit. MBPS limit should be in range [1, 4294967294] or -1 for unlimited.")
    limit_size_bytes: Optional[StrictInt] = Field(default=None, description="Folder size limit in bytes. If limit_size_bytes is not specified when a folder is created, or if limit_size_bytes is set to -1, then the folder has no limit. Otherwise, a limit smaller than the capacity of the pool can be set. Folders with an agent_type of 'smis' or 'vvol' must have a size limit.")
    num_snapcolls: Optional[StrictInt] = Field(default=None, description="Number of snapshot collections inside the folder. This attribute is deprecated and has no meaningful value.")
    num_snaps: Optional[StrictInt] = Field(default=None, description="Number of snapshots inside the folder. This attribute is deprecated and has no meaningful value.")
    overdraft_limit_pct: Optional[StrictInt] = Field(default=None, description="Amount of space to consider as overdraft range for this folder as a percentage of folder used limit. Valid values are from 0% - 200%. This is the limit above the folder usage limit beyond which enforcement action(volume offline/non-writable) is issued.")
    provisioned_bytes: Optional[StrictInt] = Field(default=None, description="Sum of provisioned size of volumes in the folder.")
    provisioned_limit_size_bytes: Optional[StrictInt] = Field(default=None, description="Limit on the provisioned size of volumes in a folder. If provisioned_limit_size_bytes is not specified when a folder is created, or if provisioned_limit_size_bytes is set to -1, then the folder has no provisioned size limit.")
    resource_uri: Optional[StrictStr] = Field(default=None, description="Link to the object URI", alias="resourceUri")
    search_name: Optional[StrictStr] = Field(default=None, description="Name of folder used for object search.")
    snap_compression_ratio: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Identifier of the default performance policy for a newly created volume.")
    tenant_id: Optional[StrictStr] = Field(default=None, description="Tenant ID of the folder. This is used to determine what tenant context the folder belongs to.")
    type: Optional[StrictStr] = Field(default=None, description="type")
    uncompressed_snap_usage_bytes: Optional[StrictInt] = Field(default=None, description="Uncompressed usage of snapshots in the folder. This field is meaningful only when the usage_valid attribute is true.")
    uncompressed_vol_usage_bytes: Optional[StrictInt] = Field(default=None, description="Uncompressed usage of volumes in the folder. This field is meaningful only when the usage_valid attribute is true.")
    unused_reserve_bytes: Optional[StrictInt] = Field(default=None, description="Unused reserve of volumes in the folder in bytes. This field is meaningful only when the usage_valid attribute is true.")
    unused_snap_reserve_bytes: Optional[StrictInt] = Field(default=None, description="Unused reserve of snapshots of volumes in the folder in bytes. This field is meaningful only when the usage_valid attribute is true.")
    usage_bytes: Optional[StrictInt] = Field(default=None, description="Sum of mapped usage and snapshot uncompressed usage of volumes in the folder.")
    usage_valid: Optional[StrictBool] = Field(default=None, description="Indicate whether the space usage attributes of folder are valid.")
    vol_compression_ratio: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Compression ratio of volumes in the folder. This field is meaningful only when the usage_valid attribute is true.")
    volume_list: Optional[List[Optional[NimbleVolumeSummary]]] = Field(default=None, description="List of volumes contained by the folder.")
    volume_mapped_bytes: Optional[StrictInt] = Field(default=None, description="Sum of mapped usage of volumes in the folder.")
    __properties: ClassVar[List[str]] = ["access_protocol", "agent_type", "app_uuid", "appserver_id", "appserver_name", "associated_links", "capacity_bytes", "commonResourceAttributes", "compressed_snap_usage_bytes", "compressed_vol_usage_bytes", "compression_ratio", "consoleUri", "creation_time", "customerId", "description", "folset_id", "folset_name", "fqn", "free_space_bytes", "full_name", "generation", "inherited_vol_perfpol_id", "inherited_vol_perfpol_name", "last_modified", "limit_bytes", "limit_bytes_specified", "limit_iops", "limit_mbps", "limit_size_bytes", "num_snapcolls", "num_snaps", "overdraft_limit_pct", "provisioned_bytes", "provisioned_limit_size_bytes", "resourceUri", "search_name", "snap_compression_ratio", "tenant_id", "type", "uncompressed_snap_usage_bytes", "uncompressed_vol_usage_bytes", "unused_reserve_bytes", "unused_snap_reserve_bytes", "usage_bytes", "usage_valid", "vol_compression_ratio", "volume_list", "volume_mapped_bytes"]

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
        """Create an instance of NimbleFolderDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in volume_list (list)
        _items = []
        if self.volume_list:
            for _item in self.volume_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volume_list'] = _items
        # set to None if access_protocol (nullable) is None
        # and model_fields_set contains the field
        if self.access_protocol is None and "access_protocol" in self.model_fields_set:
            _dict['access_protocol'] = None

        # set to None if agent_type (nullable) is None
        # and model_fields_set contains the field
        if self.agent_type is None and "agent_type" in self.model_fields_set:
            _dict['agent_type'] = None

        # set to None if app_uuid (nullable) is None
        # and model_fields_set contains the field
        if self.app_uuid is None and "app_uuid" in self.model_fields_set:
            _dict['app_uuid'] = None

        # set to None if appserver_id (nullable) is None
        # and model_fields_set contains the field
        if self.appserver_id is None and "appserver_id" in self.model_fields_set:
            _dict['appserver_id'] = None

        # set to None if appserver_name (nullable) is None
        # and model_fields_set contains the field
        if self.appserver_name is None and "appserver_name" in self.model_fields_set:
            _dict['appserver_name'] = None

        # set to None if capacity_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.capacity_bytes is None and "capacity_bytes" in self.model_fields_set:
            _dict['capacity_bytes'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if compressed_snap_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.compressed_snap_usage_bytes is None and "compressed_snap_usage_bytes" in self.model_fields_set:
            _dict['compressed_snap_usage_bytes'] = None

        # set to None if compressed_vol_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.compressed_vol_usage_bytes is None and "compressed_vol_usage_bytes" in self.model_fields_set:
            _dict['compressed_vol_usage_bytes'] = None

        # set to None if compression_ratio (nullable) is None
        # and model_fields_set contains the field
        if self.compression_ratio is None and "compression_ratio" in self.model_fields_set:
            _dict['compression_ratio'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if creation_time (nullable) is None
        # and model_fields_set contains the field
        if self.creation_time is None and "creation_time" in self.model_fields_set:
            _dict['creation_time'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if folset_id (nullable) is None
        # and model_fields_set contains the field
        if self.folset_id is None and "folset_id" in self.model_fields_set:
            _dict['folset_id'] = None

        # set to None if folset_name (nullable) is None
        # and model_fields_set contains the field
        if self.folset_name is None and "folset_name" in self.model_fields_set:
            _dict['folset_name'] = None

        # set to None if fqn (nullable) is None
        # and model_fields_set contains the field
        if self.fqn is None and "fqn" in self.model_fields_set:
            _dict['fqn'] = None

        # set to None if free_space_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.free_space_bytes is None and "free_space_bytes" in self.model_fields_set:
            _dict['free_space_bytes'] = None

        # set to None if full_name (nullable) is None
        # and model_fields_set contains the field
        if self.full_name is None and "full_name" in self.model_fields_set:
            _dict['full_name'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if inherited_vol_perfpol_id (nullable) is None
        # and model_fields_set contains the field
        if self.inherited_vol_perfpol_id is None and "inherited_vol_perfpol_id" in self.model_fields_set:
            _dict['inherited_vol_perfpol_id'] = None

        # set to None if inherited_vol_perfpol_name (nullable) is None
        # and model_fields_set contains the field
        if self.inherited_vol_perfpol_name is None and "inherited_vol_perfpol_name" in self.model_fields_set:
            _dict['inherited_vol_perfpol_name'] = None

        # set to None if last_modified (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified is None and "last_modified" in self.model_fields_set:
            _dict['last_modified'] = None

        # set to None if limit_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.limit_bytes is None and "limit_bytes" in self.model_fields_set:
            _dict['limit_bytes'] = None

        # set to None if limit_bytes_specified (nullable) is None
        # and model_fields_set contains the field
        if self.limit_bytes_specified is None and "limit_bytes_specified" in self.model_fields_set:
            _dict['limit_bytes_specified'] = None

        # set to None if limit_iops (nullable) is None
        # and model_fields_set contains the field
        if self.limit_iops is None and "limit_iops" in self.model_fields_set:
            _dict['limit_iops'] = None

        # set to None if limit_mbps (nullable) is None
        # and model_fields_set contains the field
        if self.limit_mbps is None and "limit_mbps" in self.model_fields_set:
            _dict['limit_mbps'] = None

        # set to None if limit_size_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.limit_size_bytes is None and "limit_size_bytes" in self.model_fields_set:
            _dict['limit_size_bytes'] = None

        # set to None if num_snapcolls (nullable) is None
        # and model_fields_set contains the field
        if self.num_snapcolls is None and "num_snapcolls" in self.model_fields_set:
            _dict['num_snapcolls'] = None

        # set to None if num_snaps (nullable) is None
        # and model_fields_set contains the field
        if self.num_snaps is None and "num_snaps" in self.model_fields_set:
            _dict['num_snaps'] = None

        # set to None if overdraft_limit_pct (nullable) is None
        # and model_fields_set contains the field
        if self.overdraft_limit_pct is None and "overdraft_limit_pct" in self.model_fields_set:
            _dict['overdraft_limit_pct'] = None

        # set to None if provisioned_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.provisioned_bytes is None and "provisioned_bytes" in self.model_fields_set:
            _dict['provisioned_bytes'] = None

        # set to None if provisioned_limit_size_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.provisioned_limit_size_bytes is None and "provisioned_limit_size_bytes" in self.model_fields_set:
            _dict['provisioned_limit_size_bytes'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if search_name (nullable) is None
        # and model_fields_set contains the field
        if self.search_name is None and "search_name" in self.model_fields_set:
            _dict['search_name'] = None

        # set to None if snap_compression_ratio (nullable) is None
        # and model_fields_set contains the field
        if self.snap_compression_ratio is None and "snap_compression_ratio" in self.model_fields_set:
            _dict['snap_compression_ratio'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenant_id'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if uncompressed_snap_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.uncompressed_snap_usage_bytes is None and "uncompressed_snap_usage_bytes" in self.model_fields_set:
            _dict['uncompressed_snap_usage_bytes'] = None

        # set to None if uncompressed_vol_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.uncompressed_vol_usage_bytes is None and "uncompressed_vol_usage_bytes" in self.model_fields_set:
            _dict['uncompressed_vol_usage_bytes'] = None

        # set to None if unused_reserve_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.unused_reserve_bytes is None and "unused_reserve_bytes" in self.model_fields_set:
            _dict['unused_reserve_bytes'] = None

        # set to None if unused_snap_reserve_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.unused_snap_reserve_bytes is None and "unused_snap_reserve_bytes" in self.model_fields_set:
            _dict['unused_snap_reserve_bytes'] = None

        # set to None if usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.usage_bytes is None and "usage_bytes" in self.model_fields_set:
            _dict['usage_bytes'] = None

        # set to None if usage_valid (nullable) is None
        # and model_fields_set contains the field
        if self.usage_valid is None and "usage_valid" in self.model_fields_set:
            _dict['usage_valid'] = None

        # set to None if vol_compression_ratio (nullable) is None
        # and model_fields_set contains the field
        if self.vol_compression_ratio is None and "vol_compression_ratio" in self.model_fields_set:
            _dict['vol_compression_ratio'] = None

        # set to None if volume_list (nullable) is None
        # and model_fields_set contains the field
        if self.volume_list is None and "volume_list" in self.model_fields_set:
            _dict['volume_list'] = None

        # set to None if volume_mapped_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.volume_mapped_bytes is None and "volume_mapped_bytes" in self.model_fields_set:
            _dict['volume_mapped_bytes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleFolderDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access_protocol": obj.get("access_protocol"),
            "agent_type": obj.get("agent_type"),
            "app_uuid": obj.get("app_uuid"),
            "appserver_id": obj.get("appserver_id"),
            "appserver_name": obj.get("appserver_name"),
            "associated_links": [AssociatedLinksInner.from_dict(_item) for _item in obj["associated_links"]] if obj.get("associated_links") is not None else None,
            "capacity_bytes": obj.get("capacity_bytes"),
            "commonResourceAttributes": NimbleCommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "compressed_snap_usage_bytes": obj.get("compressed_snap_usage_bytes"),
            "compressed_vol_usage_bytes": obj.get("compressed_vol_usage_bytes"),
            "compression_ratio": obj.get("compression_ratio"),
            "consoleUri": obj.get("consoleUri"),
            "creation_time": obj.get("creation_time"),
            "customerId": obj.get("customerId"),
            "description": obj.get("description"),
            "folset_id": obj.get("folset_id"),
            "folset_name": obj.get("folset_name"),
            "fqn": obj.get("fqn"),
            "free_space_bytes": obj.get("free_space_bytes"),
            "full_name": obj.get("full_name"),
            "generation": obj.get("generation"),
            "inherited_vol_perfpol_id": obj.get("inherited_vol_perfpol_id"),
            "inherited_vol_perfpol_name": obj.get("inherited_vol_perfpol_name"),
            "last_modified": obj.get("last_modified"),
            "limit_bytes": obj.get("limit_bytes"),
            "limit_bytes_specified": obj.get("limit_bytes_specified"),
            "limit_iops": obj.get("limit_iops"),
            "limit_mbps": obj.get("limit_mbps"),
            "limit_size_bytes": obj.get("limit_size_bytes"),
            "num_snapcolls": obj.get("num_snapcolls"),
            "num_snaps": obj.get("num_snaps"),
            "overdraft_limit_pct": obj.get("overdraft_limit_pct"),
            "provisioned_bytes": obj.get("provisioned_bytes"),
            "provisioned_limit_size_bytes": obj.get("provisioned_limit_size_bytes"),
            "resourceUri": obj.get("resourceUri"),
            "search_name": obj.get("search_name"),
            "snap_compression_ratio": obj.get("snap_compression_ratio"),
            "tenant_id": obj.get("tenant_id"),
            "type": obj.get("type"),
            "uncompressed_snap_usage_bytes": obj.get("uncompressed_snap_usage_bytes"),
            "uncompressed_vol_usage_bytes": obj.get("uncompressed_vol_usage_bytes"),
            "unused_reserve_bytes": obj.get("unused_reserve_bytes"),
            "unused_snap_reserve_bytes": obj.get("unused_snap_reserve_bytes"),
            "usage_bytes": obj.get("usage_bytes"),
            "usage_valid": obj.get("usage_valid"),
            "vol_compression_ratio": obj.get("vol_compression_ratio"),
            "volume_list": [NimbleVolumeSummary.from_dict(_item) for _item in obj["volume_list"]] if obj.get("volume_list") is not None else None,
            "volume_mapped_bytes": obj.get("volume_mapped_bytes")
        })
        return _obj


