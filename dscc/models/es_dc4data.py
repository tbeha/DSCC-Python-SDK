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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from dscc.models.led import LED
from typing import Optional, Set
from typing_extensions import Self

class EsDc4data(BaseModel):
    """
    EsDc4data
    """ # noqa: E501
    hpl_led: Optional[LED] = Field(default=None, alias="hplLED")
    left: Optional[StrictBool] = None
    right: Optional[StrictBool] = None
    system_led: Optional[LED] = Field(default=None, alias="systemLED")
    __properties: ClassVar[List[str]] = ["hplLED", "left", "right", "systemLED"]

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
        """Create an instance of EsDc4data from a JSON string"""
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
        # set to None if hpl_led (nullable) is None
        # and model_fields_set contains the field
        if self.hpl_led is None and "hpl_led" in self.model_fields_set:
            _dict['hplLED'] = None

        # set to None if left (nullable) is None
        # and model_fields_set contains the field
        if self.left is None and "left" in self.model_fields_set:
            _dict['left'] = None

        # set to None if right (nullable) is None
        # and model_fields_set contains the field
        if self.right is None and "right" in self.model_fields_set:
            _dict['right'] = None

        # set to None if system_led (nullable) is None
        # and model_fields_set contains the field
        if self.system_led is None and "system_led" in self.model_fields_set:
            _dict['systemLED'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EsDc4data from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hplLED": obj.get("hplLED"),
            "left": obj.get("left"),
            "right": obj.get("right"),
            "systemLED": obj.get("systemLED")
        })
        return _obj


