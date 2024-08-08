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
from typing import Optional, Set
from typing_extensions import Self

class NimbleNsCtrlrRaidInfo(BaseModel):
    """
    NimbleNsCtrlrRaidInfo
    """ # noqa: E501
    cur_copies: Optional[StrictInt] = Field(default=None, description="Current number of copies.")
    is_resyncing: Optional[StrictBool] = Field(default=None, description="Is this raid array resynchronizing.")
    max_copies: Optional[StrictInt] = Field(default=None, description="Maximum number of copies.")
    raid_id: Optional[StrictInt] = Field(default=None, description="Raid ID for this raid array.")
    raid_type: Optional[StrictStr] = Field(default=None, description="Type of raid for this array.")
    __properties: ClassVar[List[str]] = ["cur_copies", "is_resyncing", "max_copies", "raid_id", "raid_type"]

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
        """Create an instance of NimbleNsCtrlrRaidInfo from a JSON string"""
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
        # set to None if cur_copies (nullable) is None
        # and model_fields_set contains the field
        if self.cur_copies is None and "cur_copies" in self.model_fields_set:
            _dict['cur_copies'] = None

        # set to None if is_resyncing (nullable) is None
        # and model_fields_set contains the field
        if self.is_resyncing is None and "is_resyncing" in self.model_fields_set:
            _dict['is_resyncing'] = None

        # set to None if max_copies (nullable) is None
        # and model_fields_set contains the field
        if self.max_copies is None and "max_copies" in self.model_fields_set:
            _dict['max_copies'] = None

        # set to None if raid_id (nullable) is None
        # and model_fields_set contains the field
        if self.raid_id is None and "raid_id" in self.model_fields_set:
            _dict['raid_id'] = None

        # set to None if raid_type (nullable) is None
        # and model_fields_set contains the field
        if self.raid_type is None and "raid_type" in self.model_fields_set:
            _dict['raid_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleNsCtrlrRaidInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cur_copies": obj.get("cur_copies"),
            "is_resyncing": obj.get("is_resyncing"),
            "max_copies": obj.get("max_copies"),
            "raid_id": obj.get("raid_id"),
            "raid_type": obj.get("raid_type")
        })
        return _obj


