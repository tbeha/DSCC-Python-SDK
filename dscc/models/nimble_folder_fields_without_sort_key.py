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

class NimbleFolderFieldsWithoutSortKey(BaseModel):
    """
    NimbleFolderFieldsWithoutSortKey
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Identifier of the folder.")
    name: Optional[StrictStr] = Field(default=None, description="Name of the folder.")
    pool_id: Optional[StrictStr] = Field(default=None, description="ID of the pool where the folder resides.")
    pool_name: Optional[StrictStr] = Field(default=None, description="Name of the pool where the folder resides.")
    __properties: ClassVar[List[str]] = ["id", "name", "pool_id", "pool_name"]

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
        """Create an instance of NimbleFolderFieldsWithoutSortKey from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if pool_id (nullable) is None
        # and model_fields_set contains the field
        if self.pool_id is None and "pool_id" in self.model_fields_set:
            _dict['pool_id'] = None

        # set to None if pool_name (nullable) is None
        # and model_fields_set contains the field
        if self.pool_name is None and "pool_name" in self.model_fields_set:
            _dict['pool_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleFolderFieldsWithoutSortKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "pool_id": obj.get("pool_id"),
            "pool_name": obj.get("pool_name")
        })
        return _obj


