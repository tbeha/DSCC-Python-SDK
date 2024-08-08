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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dscc.models.admit_time import AdmitTime
from dscc.models.associated_links_inner import AssociatedLinksInner
from dscc.models.disk_capacity import DiskCapacity
from dscc.models.disk_loop import DiskLoop
from dscc.models.disk_position import DiskPosition
from dscc.models.disk_position_now import DiskPositionNow
from dscc.models.error_count import ErrorCount
from dscc.models.manufacturing_single import ManufacturingSingle
from dscc.models.primera_common_resource_attributes import PrimeraCommonResourceAttributes
from dscc.models.state import State
from typing import Optional, Set
from typing_extensions import Self

class DiskDetails(BaseModel):
    """
    DiskDetails
    """ # noqa: E501
    admit_time: Optional[AdmitTime] = Field(default=None, alias="admitTime")
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    capacity: Optional[DiskCapacity] = None
    common_resource_attributes: Optional[PrimeraCommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    consumable_size_mi_b: Optional[StrictInt] = Field(default=None, description="consumable size of disk in MiB", alias="consumableSizeMiB")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    dev_type: Optional[StrictStr] = Field(default=None, description="Type of the disk", alias="devType")
    disk_id: Optional[StrictInt] = Field(default=None, description="id of the disk", alias="diskId")
    displayname: Optional[StrictStr] = Field(default=None, description="Name to be used for display purposes")
    domain: Optional[StrictStr] = Field(default=None, description="Domain that the resource belongs to")
    fw_status: Optional[StrictStr] = Field(default=None, description="firmware status", alias="fwStatus")
    fw_version: Optional[StrictStr] = Field(default=None, description="firmware version", alias="fwVersion")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the resource")
    life_left_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Life Left Percentage", alias="lifeLeftPCT")
    loop_a0: Optional[DiskLoop] = Field(default=None, alias="loopA0")
    loop_a1: Optional[DiskLoop] = Field(default=None, alias="loopA1")
    loop_b0: Optional[DiskLoop] = Field(default=None, alias="loopB0")
    loop_b1: Optional[DiskLoop] = Field(default=None, alias="loopB1")
    manufacturing: Optional[ManufacturingSingle] = None
    media_type: Optional[StrictStr] = Field(default=None, description="Media Type of the disk", alias="mediaType")
    mfg_capacity_gb: Optional[StrictInt] = Field(default=None, description="manufacturing capacity of disk in GB", alias="mfgCapacityGB")
    position_last: Optional[DiskPosition] = Field(default=None, alias="positionLast")
    position_now: Optional[DiskPositionNow] = Field(default=None, alias="positionNow")
    protocol: Optional[StrictStr] = Field(default=None, description="protocol over the disk")
    raw_size_mi_b: Optional[StrictInt] = Field(default=None, description="raw Size of disk in GB", alias="rawSizeMiB")
    read_errors: Optional[ErrorCount] = Field(default=None, alias="readErrors")
    request_uri: Optional[StrictStr] = Field(default=None, description="requestUri for detailed disk object", alias="requestUri")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed disk object", alias="resourceUri")
    sed_status: Optional[StrictStr] = Field(default=None, description="SED Status", alias="sedStatus")
    speed: Optional[StrictInt] = Field(default=None, description="speed")
    state: Optional[State] = None
    system_id: Optional[StrictStr] = Field(default=None, description="SystemId / SerialNumber of the array", alias="systemId")
    temp_max: Optional[StrictInt] = Field(default=None, description="Max Temp of the disk", alias="tempMax")
    temp_min: Optional[StrictInt] = Field(default=None, description="Min Temp of the disk", alias="tempMin")
    temp_now: Optional[StrictInt] = Field(default=None, description="Current Temp of the disk, will be updated at most once in an hour", alias="tempNow")
    type: Optional[StrictStr] = Field(default=None, description="type")
    write_errors: Optional[ErrorCount] = Field(default=None, alias="writeErrors")
    wwn: Optional[StrictStr] = Field(default=None, description="unique WWN of the disk")
    __properties: ClassVar[List[str]] = ["admitTime", "associatedLinks", "capacity", "commonResourceAttributes", "consoleUri", "consumableSizeMiB", "customerId", "devType", "diskId", "displayname", "domain", "fwStatus", "fwVersion", "generation", "id", "lifeLeftPCT", "loopA0", "loopA1", "loopB0", "loopB1", "manufacturing", "mediaType", "mfgCapacityGB", "positionLast", "positionNow", "protocol", "rawSizeMiB", "readErrors", "requestUri", "resourceUri", "sedStatus", "speed", "state", "systemId", "tempMax", "tempMin", "tempNow", "type", "writeErrors", "wwn"]

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
        """Create an instance of DiskDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of admit_time
        if self.admit_time:
            _dict['admitTime'] = self.admit_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in associated_links (list)
        _items = []
        if self.associated_links:
            for _item in self.associated_links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['associatedLinks'] = _items
        # override the default output from pydantic by calling `to_dict()` of capacity
        if self.capacity:
            _dict['capacity'] = self.capacity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loop_a0
        if self.loop_a0:
            _dict['loopA0'] = self.loop_a0.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loop_a1
        if self.loop_a1:
            _dict['loopA1'] = self.loop_a1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loop_b0
        if self.loop_b0:
            _dict['loopB0'] = self.loop_b0.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loop_b1
        if self.loop_b1:
            _dict['loopB1'] = self.loop_b1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manufacturing
        if self.manufacturing:
            _dict['manufacturing'] = self.manufacturing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of position_last
        if self.position_last:
            _dict['positionLast'] = self.position_last.to_dict()
        # override the default output from pydantic by calling `to_dict()` of position_now
        if self.position_now:
            _dict['positionNow'] = self.position_now.to_dict()
        # override the default output from pydantic by calling `to_dict()` of read_errors
        if self.read_errors:
            _dict['readErrors'] = self.read_errors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of write_errors
        if self.write_errors:
            _dict['writeErrors'] = self.write_errors.to_dict()
        # set to None if admit_time (nullable) is None
        # and model_fields_set contains the field
        if self.admit_time is None and "admit_time" in self.model_fields_set:
            _dict['admitTime'] = None

        # set to None if capacity (nullable) is None
        # and model_fields_set contains the field
        if self.capacity is None and "capacity" in self.model_fields_set:
            _dict['capacity'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if consumable_size_mi_b (nullable) is None
        # and model_fields_set contains the field
        if self.consumable_size_mi_b is None and "consumable_size_mi_b" in self.model_fields_set:
            _dict['consumableSizeMiB'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if dev_type (nullable) is None
        # and model_fields_set contains the field
        if self.dev_type is None and "dev_type" in self.model_fields_set:
            _dict['devType'] = None

        # set to None if disk_id (nullable) is None
        # and model_fields_set contains the field
        if self.disk_id is None and "disk_id" in self.model_fields_set:
            _dict['diskId'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if fw_status (nullable) is None
        # and model_fields_set contains the field
        if self.fw_status is None and "fw_status" in self.model_fields_set:
            _dict['fwStatus'] = None

        # set to None if fw_version (nullable) is None
        # and model_fields_set contains the field
        if self.fw_version is None and "fw_version" in self.model_fields_set:
            _dict['fwVersion'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if life_left_pct (nullable) is None
        # and model_fields_set contains the field
        if self.life_left_pct is None and "life_left_pct" in self.model_fields_set:
            _dict['lifeLeftPCT'] = None

        # set to None if loop_a0 (nullable) is None
        # and model_fields_set contains the field
        if self.loop_a0 is None and "loop_a0" in self.model_fields_set:
            _dict['loopA0'] = None

        # set to None if loop_a1 (nullable) is None
        # and model_fields_set contains the field
        if self.loop_a1 is None and "loop_a1" in self.model_fields_set:
            _dict['loopA1'] = None

        # set to None if loop_b0 (nullable) is None
        # and model_fields_set contains the field
        if self.loop_b0 is None and "loop_b0" in self.model_fields_set:
            _dict['loopB0'] = None

        # set to None if loop_b1 (nullable) is None
        # and model_fields_set contains the field
        if self.loop_b1 is None and "loop_b1" in self.model_fields_set:
            _dict['loopB1'] = None

        # set to None if manufacturing (nullable) is None
        # and model_fields_set contains the field
        if self.manufacturing is None and "manufacturing" in self.model_fields_set:
            _dict['manufacturing'] = None

        # set to None if media_type (nullable) is None
        # and model_fields_set contains the field
        if self.media_type is None and "media_type" in self.model_fields_set:
            _dict['mediaType'] = None

        # set to None if mfg_capacity_gb (nullable) is None
        # and model_fields_set contains the field
        if self.mfg_capacity_gb is None and "mfg_capacity_gb" in self.model_fields_set:
            _dict['mfgCapacityGB'] = None

        # set to None if position_last (nullable) is None
        # and model_fields_set contains the field
        if self.position_last is None and "position_last" in self.model_fields_set:
            _dict['positionLast'] = None

        # set to None if position_now (nullable) is None
        # and model_fields_set contains the field
        if self.position_now is None and "position_now" in self.model_fields_set:
            _dict['positionNow'] = None

        # set to None if protocol (nullable) is None
        # and model_fields_set contains the field
        if self.protocol is None and "protocol" in self.model_fields_set:
            _dict['protocol'] = None

        # set to None if raw_size_mi_b (nullable) is None
        # and model_fields_set contains the field
        if self.raw_size_mi_b is None and "raw_size_mi_b" in self.model_fields_set:
            _dict['rawSizeMiB'] = None

        # set to None if read_errors (nullable) is None
        # and model_fields_set contains the field
        if self.read_errors is None and "read_errors" in self.model_fields_set:
            _dict['readErrors'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestUri'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if sed_status (nullable) is None
        # and model_fields_set contains the field
        if self.sed_status is None and "sed_status" in self.model_fields_set:
            _dict['sedStatus'] = None

        # set to None if speed (nullable) is None
        # and model_fields_set contains the field
        if self.speed is None and "speed" in self.model_fields_set:
            _dict['speed'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if system_id (nullable) is None
        # and model_fields_set contains the field
        if self.system_id is None and "system_id" in self.model_fields_set:
            _dict['systemId'] = None

        # set to None if temp_max (nullable) is None
        # and model_fields_set contains the field
        if self.temp_max is None and "temp_max" in self.model_fields_set:
            _dict['tempMax'] = None

        # set to None if temp_min (nullable) is None
        # and model_fields_set contains the field
        if self.temp_min is None and "temp_min" in self.model_fields_set:
            _dict['tempMin'] = None

        # set to None if temp_now (nullable) is None
        # and model_fields_set contains the field
        if self.temp_now is None and "temp_now" in self.model_fields_set:
            _dict['tempNow'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if write_errors (nullable) is None
        # and model_fields_set contains the field
        if self.write_errors is None and "write_errors" in self.model_fields_set:
            _dict['writeErrors'] = None

        # set to None if wwn (nullable) is None
        # and model_fields_set contains the field
        if self.wwn is None and "wwn" in self.model_fields_set:
            _dict['wwn'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DiskDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "admitTime": AdmitTime.from_dict(obj["admitTime"]) if obj.get("admitTime") is not None else None,
            "associatedLinks": [AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "capacity": DiskCapacity.from_dict(obj["capacity"]) if obj.get("capacity") is not None else None,
            "commonResourceAttributes": PrimeraCommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "consoleUri": obj.get("consoleUri"),
            "consumableSizeMiB": obj.get("consumableSizeMiB"),
            "customerId": obj.get("customerId"),
            "devType": obj.get("devType"),
            "diskId": obj.get("diskId"),
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "fwStatus": obj.get("fwStatus"),
            "fwVersion": obj.get("fwVersion"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "lifeLeftPCT": obj.get("lifeLeftPCT"),
            "loopA0": DiskLoop.from_dict(obj["loopA0"]) if obj.get("loopA0") is not None else None,
            "loopA1": DiskLoop.from_dict(obj["loopA1"]) if obj.get("loopA1") is not None else None,
            "loopB0": DiskLoop.from_dict(obj["loopB0"]) if obj.get("loopB0") is not None else None,
            "loopB1": DiskLoop.from_dict(obj["loopB1"]) if obj.get("loopB1") is not None else None,
            "manufacturing": ManufacturingSingle.from_dict(obj["manufacturing"]) if obj.get("manufacturing") is not None else None,
            "mediaType": obj.get("mediaType"),
            "mfgCapacityGB": obj.get("mfgCapacityGB"),
            "positionLast": DiskPosition.from_dict(obj["positionLast"]) if obj.get("positionLast") is not None else None,
            "positionNow": DiskPositionNow.from_dict(obj["positionNow"]) if obj.get("positionNow") is not None else None,
            "protocol": obj.get("protocol"),
            "rawSizeMiB": obj.get("rawSizeMiB"),
            "readErrors": ErrorCount.from_dict(obj["readErrors"]) if obj.get("readErrors") is not None else None,
            "requestUri": obj.get("requestUri"),
            "resourceUri": obj.get("resourceUri"),
            "sedStatus": obj.get("sedStatus"),
            "speed": obj.get("speed"),
            "state": State.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "systemId": obj.get("systemId"),
            "tempMax": obj.get("tempMax"),
            "tempMin": obj.get("tempMin"),
            "tempNow": obj.get("tempNow"),
            "type": obj.get("type"),
            "writeErrors": ErrorCount.from_dict(obj["writeErrors"]) if obj.get("writeErrors") is not None else None,
            "wwn": obj.get("wwn")
        })
        return _obj


