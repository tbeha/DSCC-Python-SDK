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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from dscc.models.edit_throttle import EditThrottle
from typing import Optional, Set
from typing_extensions import Self

class EditSystemParameters(BaseModel):
    """
    EditSystemParameters
    """ # noqa: E501
    alarms_enabled: Optional[StrictBool] = Field(default=None, description="Enable or disable alarm feature.")
    default_volume_limit: Optional[StrictInt] = Field(default=None, description="Default limit for a volume space usage as a percentage of volume size. Volume will be taken offline/made non-writable on exceeding its limit. Percentage as integer from 0 to 100.")
    fc_enabled: Optional[StrictBool] = Field(default=None, description="Enable or disable FC.This flag can be modified only on the physical array which supports FC.")
    group_target_enabled: Optional[StrictBool] = Field(default=None, description="Enable or disable group target.")
    iscsi_enabled: Optional[StrictBool] = Field(default=None, description="Enable or disable iSCSI.")
    repl_throttle_list: Optional[List[Optional[EditThrottle]]] = Field(default=None, description="All the replication bandwidth limits on the system. All the throttles for the partner.")
    vss_validation_timeout: Optional[StrictInt] = Field(default=None, description="The amount of time in seconds to validate Microsoft VSS application synchronization before timing out. VSS validation timeout in second, valid range is from 1 to 3600 (60 minutes).")
    __properties: ClassVar[List[str]] = ["alarms_enabled", "default_volume_limit", "fc_enabled", "group_target_enabled", "iscsi_enabled", "repl_throttle_list", "vss_validation_timeout"]

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
        """Create an instance of EditSystemParameters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in repl_throttle_list (list)
        _items = []
        if self.repl_throttle_list:
            for _item in self.repl_throttle_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['repl_throttle_list'] = _items
        # set to None if alarms_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.alarms_enabled is None and "alarms_enabled" in self.model_fields_set:
            _dict['alarms_enabled'] = None

        # set to None if default_volume_limit (nullable) is None
        # and model_fields_set contains the field
        if self.default_volume_limit is None and "default_volume_limit" in self.model_fields_set:
            _dict['default_volume_limit'] = None

        # set to None if fc_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.fc_enabled is None and "fc_enabled" in self.model_fields_set:
            _dict['fc_enabled'] = None

        # set to None if group_target_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.group_target_enabled is None and "group_target_enabled" in self.model_fields_set:
            _dict['group_target_enabled'] = None

        # set to None if iscsi_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.iscsi_enabled is None and "iscsi_enabled" in self.model_fields_set:
            _dict['iscsi_enabled'] = None

        # set to None if repl_throttle_list (nullable) is None
        # and model_fields_set contains the field
        if self.repl_throttle_list is None and "repl_throttle_list" in self.model_fields_set:
            _dict['repl_throttle_list'] = None

        # set to None if vss_validation_timeout (nullable) is None
        # and model_fields_set contains the field
        if self.vss_validation_timeout is None and "vss_validation_timeout" in self.model_fields_set:
            _dict['vss_validation_timeout'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EditSystemParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alarms_enabled": obj.get("alarms_enabled"),
            "default_volume_limit": obj.get("default_volume_limit"),
            "fc_enabled": obj.get("fc_enabled"),
            "group_target_enabled": obj.get("group_target_enabled"),
            "iscsi_enabled": obj.get("iscsi_enabled"),
            "repl_throttle_list": [EditThrottle.from_dict(_item) for _item in obj["repl_throttle_list"]] if obj.get("repl_throttle_list") is not None else None,
            "vss_validation_timeout": obj.get("vss_validation_timeout")
        })
        return _obj


