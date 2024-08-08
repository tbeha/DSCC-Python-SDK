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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from dscc.models.nimble_host_group_detail import NimbleHostGroupDetail
from typing import Optional, Set
from typing_extensions import Self

class NimbleVolumeExportDetails(BaseModel):
    """
    NimbleVolumeExportDetails
    """ # noqa: E501
    host_groups: Optional[List[Optional[NimbleHostGroupDetail]]] = None
    __properties: ClassVar[List[str]] = ["host_groups"]

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
        """Create an instance of NimbleVolumeExportDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in host_groups (list)
        _items = []
        if self.host_groups:
            for _item in self.host_groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['host_groups'] = _items
        # set to None if host_groups (nullable) is None
        # and model_fields_set contains the field
        if self.host_groups is None and "host_groups" in self.model_fields_set:
            _dict['host_groups'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleVolumeExportDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "host_groups": [NimbleHostGroupDetail.from_dict(_item) for _item in obj["host_groups"]] if obj.get("host_groups") is not None else None
        })
        return _obj


