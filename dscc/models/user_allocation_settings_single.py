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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dscc.models.deprecated_device_type4user_allocation_settings_single_ha import DeprecatedDeviceType4userAllocationSettingsSingleHA
from dscc.models.device_speed_single import DeviceSpeedSingle
from typing import Optional, Set
from typing_extensions import Self

class UserAllocationSettingsSingle(BaseModel):
    """
    UserAllocationSettingsSingle
    """ # noqa: E501
    ha: Optional[DeprecatedDeviceType4userAllocationSettingsSingleHA] = Field(default=None, alias="HA")
    raid_type: Optional[StrictStr] = Field(default=None, alias="RAIDType")
    device_speed: Optional[DeviceSpeedSingle] = Field(default=None, alias="deviceSpeed")
    device_type: Optional[StrictStr] = Field(default=None, alias="deviceType")
    disk_filter: Optional[StrictStr] = Field(default=None, alias="diskFilter")
    requested_ha: Optional[DeprecatedDeviceType4userAllocationSettingsSingleHA] = Field(default=None, alias="requestedHA")
    set_size: Optional[StrictStr] = Field(default=None, alias="setSize")
    step_size: Optional[StrictInt] = Field(default=None, alias="stepSize")
    __properties: ClassVar[List[str]] = ["HA", "RAIDType", "deviceSpeed", "deviceType", "diskFilter", "requestedHA", "setSize", "stepSize"]

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
        """Create an instance of UserAllocationSettingsSingle from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ha
        if self.ha:
            _dict['HA'] = self.ha.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device_speed
        if self.device_speed:
            _dict['deviceSpeed'] = self.device_speed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requested_ha
        if self.requested_ha:
            _dict['requestedHA'] = self.requested_ha.to_dict()
        # set to None if ha (nullable) is None
        # and model_fields_set contains the field
        if self.ha is None and "ha" in self.model_fields_set:
            _dict['HA'] = None

        # set to None if raid_type (nullable) is None
        # and model_fields_set contains the field
        if self.raid_type is None and "raid_type" in self.model_fields_set:
            _dict['RAIDType'] = None

        # set to None if device_speed (nullable) is None
        # and model_fields_set contains the field
        if self.device_speed is None and "device_speed" in self.model_fields_set:
            _dict['deviceSpeed'] = None

        # set to None if device_type (nullable) is None
        # and model_fields_set contains the field
        if self.device_type is None and "device_type" in self.model_fields_set:
            _dict['deviceType'] = None

        # set to None if disk_filter (nullable) is None
        # and model_fields_set contains the field
        if self.disk_filter is None and "disk_filter" in self.model_fields_set:
            _dict['diskFilter'] = None

        # set to None if requested_ha (nullable) is None
        # and model_fields_set contains the field
        if self.requested_ha is None and "requested_ha" in self.model_fields_set:
            _dict['requestedHA'] = None

        # set to None if set_size (nullable) is None
        # and model_fields_set contains the field
        if self.set_size is None and "set_size" in self.model_fields_set:
            _dict['setSize'] = None

        # set to None if step_size (nullable) is None
        # and model_fields_set contains the field
        if self.step_size is None and "step_size" in self.model_fields_set:
            _dict['stepSize'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserAllocationSettingsSingle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "HA": DeprecatedDeviceType4userAllocationSettingsSingleHA.from_dict(obj["HA"]) if obj.get("HA") is not None else None,
            "RAIDType": obj.get("RAIDType"),
            "deviceSpeed": DeviceSpeedSingle.from_dict(obj["deviceSpeed"]) if obj.get("deviceSpeed") is not None else None,
            "deviceType": obj.get("deviceType"),
            "diskFilter": obj.get("diskFilter"),
            "requestedHA": DeprecatedDeviceType4userAllocationSettingsSingleHA.from_dict(obj["requestedHA"]) if obj.get("requestedHA") is not None else None,
            "setSize": obj.get("setSize"),
            "stepSize": obj.get("stepSize")
        })
        return _obj


