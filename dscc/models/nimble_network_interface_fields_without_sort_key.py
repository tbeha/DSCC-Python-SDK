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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class NimbleNetworkInterfaceFieldsWithoutSortKey(BaseModel):
    """
    NimbleNetworkInterfaceFieldsWithoutSortKey
    """ # noqa: E501
    array_id: Optional[StrictStr] = Field(default=None, description="Identifier for the array. A 42 digit hexadecimal number.")
    array_name_or_serial: Optional[StrictStr] = Field(default=None, description="Name or serial of the array where the interface is hosted String of up to 64 alphanumeric characters, - and . and : are allowed after first character.")
    id: Optional[StrictStr] = Field(default=None, description="Identifier for the array. A 42 digit hexadecimal number.")
    mac: Optional[StrictStr] = Field(default=None, description="MAC address of the interface. Mac address of an interfaces.")
    __properties: ClassVar[List[str]] = ["array_id", "array_name_or_serial", "id", "mac"]

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
        """Create an instance of NimbleNetworkInterfaceFieldsWithoutSortKey from a JSON string"""
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
        # set to None if array_id (nullable) is None
        # and model_fields_set contains the field
        if self.array_id is None and "array_id" in self.model_fields_set:
            _dict['array_id'] = None

        # set to None if array_name_or_serial (nullable) is None
        # and model_fields_set contains the field
        if self.array_name_or_serial is None and "array_name_or_serial" in self.model_fields_set:
            _dict['array_name_or_serial'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if mac (nullable) is None
        # and model_fields_set contains the field
        if self.mac is None and "mac" in self.model_fields_set:
            _dict['mac'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleNetworkInterfaceFieldsWithoutSortKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "array_id": obj.get("array_id"),
            "array_name_or_serial": obj.get("array_name_or_serial"),
            "id": obj.get("id"),
            "mac": obj.get("mac")
        })
        return _obj


