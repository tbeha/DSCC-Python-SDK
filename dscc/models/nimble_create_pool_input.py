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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dscc.models.create_pool_nimble_array_detail import CreatePoolNimbleArrayDetail
from typing import Optional, Set
from typing_extensions import Self

class NimbleCreatePoolInput(BaseModel):
    """
    Create a pool with given input.
    """ # noqa: E501
    array_list: List[CreatePoolNimbleArrayDetail] = Field(description="List of arrays identified by their IDs, in the pool.")
    dedupe_all_volumes: Optional[StrictBool] = Field(default=None, description="Indicates if dedupe is enabled by default for new volumes on this pool. Defaults to false.")
    description: Optional[StrictStr] = Field(default=None, description="Text description of pool. String of up to 255 printable ASCII characters. Defaults to empty string.")
    name: StrictStr = Field(description="Name of pool. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.")
    __properties: ClassVar[List[str]] = ["array_list", "dedupe_all_volumes", "description", "name"]

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
        """Create an instance of NimbleCreatePoolInput from a JSON string"""
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
            _dict['array_list'] = _items
        # set to None if dedupe_all_volumes (nullable) is None
        # and model_fields_set contains the field
        if self.dedupe_all_volumes is None and "dedupe_all_volumes" in self.model_fields_set:
            _dict['dedupe_all_volumes'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleCreatePoolInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "array_list": [CreatePoolNimbleArrayDetail.from_dict(_item) for _item in obj["array_list"]] if obj.get("array_list") is not None else None,
            "dedupe_all_volumes": obj.get("dedupe_all_volumes"),
            "description": obj.get("description"),
            "name": obj.get("name")
        })
        return _obj


