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

class NetworkInterfaceFilterableFields(BaseModel):
    """
    NetworkInterfaceFilterableFields
    """ # noqa: E501
    array_id: Optional[StrictStr] = Field(default=None, description="Identifier for the array. A 42 digit hexadecimal number. `Filter`")
    controller_name: Optional[StrictStr] = Field(default=None, description="Name (A or B) of the controller where the interface is hosted. Plain string. `Filter`")
    id: Optional[StrictStr] = Field(default=None, description="Identifier for the interface. A 42 digit hexadecimal number. `Filter`")
    name: Optional[StrictStr] = Field(default=None, description="Name of the interface. `Filter`")
    __properties: ClassVar[List[str]] = ["array_id", "controller_name", "id", "name"]

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
        """Create an instance of NetworkInterfaceFilterableFields from a JSON string"""
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

        # set to None if controller_name (nullable) is None
        # and model_fields_set contains the field
        if self.controller_name is None and "controller_name" in self.model_fields_set:
            _dict['controller_name'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetworkInterfaceFilterableFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "array_id": obj.get("array_id"),
            "controller_name": obj.get("controller_name"),
            "id": obj.get("id"),
            "name": obj.get("name")
        })
        return _obj


