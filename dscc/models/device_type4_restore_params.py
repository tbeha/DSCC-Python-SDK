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
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4RestoreParams(BaseModel):
    """
    DeviceType4RestoreParams
    """ # noqa: E501
    no_snapshot: Optional[StrictBool] = Field(default=None, description="Specifies that snapshots are not taken of application sets that are switched from secondary to primary. Additionally, existing snapshots are deleted if application sets are switched from primary to secondary. The use of this option may result in a full synchronization of the secondary volumes.", alias="noSnapshot")
    skip_start: Optional[StrictBool] = Field(default=None, description="Specifies that protection is not started after restore action is completed.", alias="skipStart")
    skip_sync: Optional[StrictBool] = Field(default=None, description="Specifies that protection is not synced after restore action is completed.", alias="skipSync")
    target_name: Optional[StrictStr] = Field(default=None, description="Replication partner name (target name) on which the restore action to be performed.", alias="targetName")
    __properties: ClassVar[List[str]] = ["noSnapshot", "skipStart", "skipSync", "targetName"]

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
        """Create an instance of DeviceType4RestoreParams from a JSON string"""
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
        # set to None if no_snapshot (nullable) is None
        # and model_fields_set contains the field
        if self.no_snapshot is None and "no_snapshot" in self.model_fields_set:
            _dict['noSnapshot'] = None

        # set to None if skip_start (nullable) is None
        # and model_fields_set contains the field
        if self.skip_start is None and "skip_start" in self.model_fields_set:
            _dict['skipStart'] = None

        # set to None if skip_sync (nullable) is None
        # and model_fields_set contains the field
        if self.skip_sync is None and "skip_sync" in self.model_fields_set:
            _dict['skipSync'] = None

        # set to None if target_name (nullable) is None
        # and model_fields_set contains the field
        if self.target_name is None and "target_name" in self.model_fields_set:
            _dict['targetName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4RestoreParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "noSnapshot": obj.get("noSnapshot"),
            "skipStart": obj.get("skipStart"),
            "skipSync": obj.get("skipSync"),
            "targetName": obj.get("targetName")
        })
        return _obj


