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
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4DiskPositionNow(BaseModel):
    """
    Disk Position Now
    """ # noqa: E501
    cage: Optional[StrictInt] = Field(default=None, description="cage ID")
    disk: Optional[StrictInt] = Field(default=None, description="disk ID. This field is deprecated.")
    side: Optional[StrictStr] = Field(default=None, description="disk side. This field is deprecated.")
    sled: Optional[StrictInt] = Field(default=None, description="sled ID")
    __properties: ClassVar[List[str]] = ["cage", "disk", "side", "sled"]

    @field_validator('side')
    def side_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SIDE_NONE', 'SIDE_LEFT', 'SIDE_RIGHT', 'null']):
            raise ValueError("must be one of enum values ('SIDE_NONE', 'SIDE_LEFT', 'SIDE_RIGHT', 'null')")
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
        """Create an instance of DeviceType4DiskPositionNow from a JSON string"""
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
        # set to None if cage (nullable) is None
        # and model_fields_set contains the field
        if self.cage is None and "cage" in self.model_fields_set:
            _dict['cage'] = None

        # set to None if disk (nullable) is None
        # and model_fields_set contains the field
        if self.disk is None and "disk" in self.model_fields_set:
            _dict['disk'] = None

        # set to None if side (nullable) is None
        # and model_fields_set contains the field
        if self.side is None and "side" in self.model_fields_set:
            _dict['side'] = None

        # set to None if sled (nullable) is None
        # and model_fields_set contains the field
        if self.sled is None and "sled" in self.model_fields_set:
            _dict['sled'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4DiskPositionNow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cage": obj.get("cage"),
            "disk": obj.get("disk"),
            "side": obj.get("side"),
            "sled": obj.get("sled")
        })
        return _obj


