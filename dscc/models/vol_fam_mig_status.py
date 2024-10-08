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
from dscc.models.array_mig_status import ArrayMigStatus
from typing import Optional, Set
from typing_extensions import Self

class VolFamMigStatus(BaseModel):
    """
    Data migration status for a group of related volumes.
    """ # noqa: E501
    array_list: Optional[List[Optional[ArrayMigStatus]]] = Field(default=None, description="Data migration status for the arrays that store the volumes.")
    dest_pool_id: Optional[StrictStr] = Field(default=None, description="ID of the destination pool, where the volumes are moved.")
    dest_pool_name: Optional[StrictStr] = Field(default=None, description="Name of the destination pool, where the volumes are moved.")
    move_bytes_migrated: Optional[StrictInt] = Field(default=None, description="The bytes of volumes which have been moved.")
    move_bytes_remaining: Optional[StrictInt] = Field(default=None, description="The bytes of volumes which have not been moved.")
    move_est_compl_time: Optional[StrictInt] = Field(default=None, description="The estimated time of completion of a move.")
    move_start_time: Optional[StrictInt] = Field(default=None, description="The start time when the volumes was moved.")
    root_vol_id: Optional[StrictStr] = Field(default=None, description="ID of the root volume in the group.")
    root_vol_name: Optional[StrictStr] = Field(default=None, description="Name of the root volume in the group.")
    source_pool_id: Optional[StrictStr] = Field(default=None, description="ID of the source pool, where the volumes originally locate.")
    source_pool_name: Optional[StrictStr] = Field(default=None, description="Name of the source pool, where the volumes originally locate.")
    __properties: ClassVar[List[str]] = ["array_list", "dest_pool_id", "dest_pool_name", "move_bytes_migrated", "move_bytes_remaining", "move_est_compl_time", "move_start_time", "root_vol_id", "root_vol_name", "source_pool_id", "source_pool_name"]

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
        """Create an instance of VolFamMigStatus from a JSON string"""
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
        # set to None if array_list (nullable) is None
        # and model_fields_set contains the field
        if self.array_list is None and "array_list" in self.model_fields_set:
            _dict['array_list'] = None

        # set to None if dest_pool_id (nullable) is None
        # and model_fields_set contains the field
        if self.dest_pool_id is None and "dest_pool_id" in self.model_fields_set:
            _dict['dest_pool_id'] = None

        # set to None if dest_pool_name (nullable) is None
        # and model_fields_set contains the field
        if self.dest_pool_name is None and "dest_pool_name" in self.model_fields_set:
            _dict['dest_pool_name'] = None

        # set to None if move_bytes_migrated (nullable) is None
        # and model_fields_set contains the field
        if self.move_bytes_migrated is None and "move_bytes_migrated" in self.model_fields_set:
            _dict['move_bytes_migrated'] = None

        # set to None if move_bytes_remaining (nullable) is None
        # and model_fields_set contains the field
        if self.move_bytes_remaining is None and "move_bytes_remaining" in self.model_fields_set:
            _dict['move_bytes_remaining'] = None

        # set to None if move_est_compl_time (nullable) is None
        # and model_fields_set contains the field
        if self.move_est_compl_time is None and "move_est_compl_time" in self.model_fields_set:
            _dict['move_est_compl_time'] = None

        # set to None if move_start_time (nullable) is None
        # and model_fields_set contains the field
        if self.move_start_time is None and "move_start_time" in self.model_fields_set:
            _dict['move_start_time'] = None

        # set to None if root_vol_id (nullable) is None
        # and model_fields_set contains the field
        if self.root_vol_id is None and "root_vol_id" in self.model_fields_set:
            _dict['root_vol_id'] = None

        # set to None if root_vol_name (nullable) is None
        # and model_fields_set contains the field
        if self.root_vol_name is None and "root_vol_name" in self.model_fields_set:
            _dict['root_vol_name'] = None

        # set to None if source_pool_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_pool_id is None and "source_pool_id" in self.model_fields_set:
            _dict['source_pool_id'] = None

        # set to None if source_pool_name (nullable) is None
        # and model_fields_set contains the field
        if self.source_pool_name is None and "source_pool_name" in self.model_fields_set:
            _dict['source_pool_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VolFamMigStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "array_list": [ArrayMigStatus.from_dict(_item) for _item in obj["array_list"]] if obj.get("array_list") is not None else None,
            "dest_pool_id": obj.get("dest_pool_id"),
            "dest_pool_name": obj.get("dest_pool_name"),
            "move_bytes_migrated": obj.get("move_bytes_migrated"),
            "move_bytes_remaining": obj.get("move_bytes_remaining"),
            "move_est_compl_time": obj.get("move_est_compl_time"),
            "move_start_time": obj.get("move_start_time"),
            "root_vol_id": obj.get("root_vol_id"),
            "root_vol_name": obj.get("root_vol_name"),
            "source_pool_id": obj.get("source_pool_id"),
            "source_pool_name": obj.get("source_pool_name")
        })
        return _obj


