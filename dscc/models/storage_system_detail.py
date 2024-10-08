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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dscc.models.collection_status import CollectionStatus
from dscc.models.connection_status import ConnectionStatus
from dscc.models.device_type4_associated_links_inner import DeviceType4AssociatedLinksInner
from dscc.models.ips import Ips
from dscc.models.nimble_array_summary import NimbleArraySummary
from typing import Optional, Set
from typing_extensions import Self

class StorageSystemDetail(BaseModel):
    """
    StorageSystemDetail
    """ # noqa: E501
    array_list: Optional[List[Optional[NimbleArraySummary]]] = Field(default=None, description="The list of Nimble arrays part of this system.", alias="arrayList")
    associated_links: Optional[List[DeviceType4AssociatedLinksInner]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    callhome_status: Optional[StrictStr] = Field(default=None, description="Device Call-home connectivity status", alias="callhomeStatus")
    collection_status: Optional[CollectionStatus] = Field(default=None, alias="collectionStatus")
    connection_status: Optional[ConnectionStatus] = Field(default=None, alias="connectionStatus")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    description: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="A brief description of the storage system.")
    fqdn: Optional[StrictStr] = Field(default=None, description="Fully qualified domain name of the system")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    id: Optional[StrictStr] = Field(default=None, description="UUID string uniquely identifying the storage system object.")
    last_connected_time: Optional[StrictInt] = Field(default=None, description="Last time when the system was connected", alias="lastConnectedTime")
    mgmt_ip: Optional[Ips] = Field(default=None, alias="mgmtIp")
    model: Optional[StrictStr] = Field(default=None, description="Model of the storage system")
    name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="A name to identify the storage system.")
    product_family: Optional[StrictStr] = Field(default=None, description="Storage device type", alias="productFamily")
    request_uri: Optional[StrictStr] = Field(default=None, description="requestUri for detailed storage object", alias="requestUri")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed storage object", alias="resourceUri")
    software_version: Optional[StrictStr] = Field(default=None, description="Software version of the storage system", alias="softwareVersion")
    state: Optional[StrictStr] = Field(default=None, description="For deviceType1 State derived from ports, enclosure, disk and node state for deviceType2 state is state reported by deviceType2 array")
    system_wwn: Optional[StrictStr] = Field(default=None, description="WWN of the array", alias="systemWWN")
    tier_type: Optional[StrictStr] = Field(default=None, description="StorageTier.", alias="tierType")
    type: Optional[StrictStr] = Field(default=None, description="type")
    up_since: Optional[StrictInt] = Field(default=None, description="The time that the system has been up since", alias="upSince")
    __properties: ClassVar[List[str]] = ["arrayList", "associatedLinks", "callhomeStatus", "collectionStatus", "connectionStatus", "consoleUri", "customerId", "description", "fqdn", "generation", "id", "lastConnectedTime", "mgmtIp", "model", "name", "productFamily", "requestUri", "resourceUri", "softwareVersion", "state", "systemWWN", "tierType", "type", "upSince"]

    @field_validator('callhome_status')
    def callhome_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ENABLED_NORMAL', 'ENABLED_DEGRADED', 'DISABLED', 'UNKNOWN']):
            raise ValueError("must be one of enum values ('ENABLED_NORMAL', 'ENABLED_DEGRADED', 'DISABLED', 'UNKNOWN')")
        return value

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NORMAL', 'DEGRADED']):
            raise ValueError("must be one of enum values ('NORMAL', 'DEGRADED')")
        return value

    @field_validator('tier_type')
    def tier_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['STORAGE_TIER_9000_NVME', 'STORAGE_TIER_6000_NVME', 'STORAGE_TIER_NIMBLE_HYBRID', 'STORAGE_TIER_NIMBLE_AFA', 'STORAGE_TIER_600_AFA', 'STORAGE_TIER_600_HYBRID', 'STORAGE_TIER_NIMBLE_VSA', 'STORAGE_TIER_MISSION_CRITICAL', 'STORAGE_TIER_BUSINESS_CRITICAL', 'STORAGE_TIER_GENERAL_PURPOSE', 'STORAGE_TIER_5000', 'STORAGE_TIER_10000_NVME', 'STORAGE_TIER_10020_MP', 'STORAGE_TIER_UNKNOWN', 'STORAGE_TIER_VIRTUAL_ARCUS']):
            raise ValueError("must be one of enum values ('STORAGE_TIER_9000_NVME', 'STORAGE_TIER_6000_NVME', 'STORAGE_TIER_NIMBLE_HYBRID', 'STORAGE_TIER_NIMBLE_AFA', 'STORAGE_TIER_600_AFA', 'STORAGE_TIER_600_HYBRID', 'STORAGE_TIER_NIMBLE_VSA', 'STORAGE_TIER_MISSION_CRITICAL', 'STORAGE_TIER_BUSINESS_CRITICAL', 'STORAGE_TIER_GENERAL_PURPOSE', 'STORAGE_TIER_5000', 'STORAGE_TIER_10000_NVME', 'STORAGE_TIER_10020_MP', 'STORAGE_TIER_UNKNOWN', 'STORAGE_TIER_VIRTUAL_ARCUS')")
        return value

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
        """Create an instance of StorageSystemDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in array_list (list)
        _items = []
        if self.array_list:
            for _item in self.array_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['arrayList'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in associated_links (list)
        _items = []
        if self.associated_links:
            for _item in self.associated_links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['associatedLinks'] = _items
        # override the default output from pydantic by calling `to_dict()` of collection_status
        if self.collection_status:
            _dict['collectionStatus'] = self.collection_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mgmt_ip
        if self.mgmt_ip:
            _dict['mgmtIp'] = self.mgmt_ip.to_dict()
        # set to None if array_list (nullable) is None
        # and model_fields_set contains the field
        if self.array_list is None and "array_list" in self.model_fields_set:
            _dict['arrayList'] = None

        # set to None if associated_links (nullable) is None
        # and model_fields_set contains the field
        if self.associated_links is None and "associated_links" in self.model_fields_set:
            _dict['associatedLinks'] = None

        # set to None if collection_status (nullable) is None
        # and model_fields_set contains the field
        if self.collection_status is None and "collection_status" in self.model_fields_set:
            _dict['collectionStatus'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if fqdn (nullable) is None
        # and model_fields_set contains the field
        if self.fqdn is None and "fqdn" in self.model_fields_set:
            _dict['fqdn'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if last_connected_time (nullable) is None
        # and model_fields_set contains the field
        if self.last_connected_time is None and "last_connected_time" in self.model_fields_set:
            _dict['lastConnectedTime'] = None

        # set to None if mgmt_ip (nullable) is None
        # and model_fields_set contains the field
        if self.mgmt_ip is None and "mgmt_ip" in self.model_fields_set:
            _dict['mgmtIp'] = None

        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestUri'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if software_version (nullable) is None
        # and model_fields_set contains the field
        if self.software_version is None and "software_version" in self.model_fields_set:
            _dict['softwareVersion'] = None

        # set to None if system_wwn (nullable) is None
        # and model_fields_set contains the field
        if self.system_wwn is None and "system_wwn" in self.model_fields_set:
            _dict['systemWWN'] = None

        # set to None if tier_type (nullable) is None
        # and model_fields_set contains the field
        if self.tier_type is None and "tier_type" in self.model_fields_set:
            _dict['tierType'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if up_since (nullable) is None
        # and model_fields_set contains the field
        if self.up_since is None and "up_since" in self.model_fields_set:
            _dict['upSince'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StorageSystemDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "arrayList": [NimbleArraySummary.from_dict(_item) for _item in obj["arrayList"]] if obj.get("arrayList") is not None else None,
            "associatedLinks": [DeviceType4AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "callhomeStatus": obj.get("callhomeStatus"),
            "collectionStatus": CollectionStatus.from_dict(obj["collectionStatus"]) if obj.get("collectionStatus") is not None else None,
            "connectionStatus": obj.get("connectionStatus"),
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "description": obj.get("description"),
            "fqdn": obj.get("fqdn"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "lastConnectedTime": obj.get("lastConnectedTime"),
            "mgmtIp": Ips.from_dict(obj["mgmtIp"]) if obj.get("mgmtIp") is not None else None,
            "model": obj.get("model"),
            "name": obj.get("name"),
            "productFamily": obj.get("productFamily"),
            "requestUri": obj.get("requestUri"),
            "resourceUri": obj.get("resourceUri"),
            "softwareVersion": obj.get("softwareVersion"),
            "state": obj.get("state"),
            "systemWWN": obj.get("systemWWN"),
            "tierType": obj.get("tierType"),
            "type": obj.get("type"),
            "upSince": obj.get("upSince")
        })
        return _obj


