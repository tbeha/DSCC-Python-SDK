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
from dscc.models.latency_annotation_metrics import LatencyAnnotationMetrics
from typing import Optional, Set
from typing_extensions import Self

class LatencyAnnotations(BaseModel):
    """
    Volume latency annotations response structure
    """ # noqa: E501
    read: Optional[List[LatencyAnnotationMetrics]] = None
    write: Optional[List[LatencyAnnotationMetrics]] = None
    __properties: ClassVar[List[str]] = ["read", "write"]

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
        """Create an instance of LatencyAnnotations from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in read (list)
        _items = []
        if self.read:
            for _item in self.read:
                if _item:
                    _items.append(_item.to_dict())
            _dict['read'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in write (list)
        _items = []
        if self.write:
            for _item in self.write:
                if _item:
                    _items.append(_item.to_dict())
            _dict['write'] = _items
        # set to None if read (nullable) is None
        # and model_fields_set contains the field
        if self.read is None and "read" in self.model_fields_set:
            _dict['read'] = None

        # set to None if write (nullable) is None
        # and model_fields_set contains the field
        if self.write is None and "write" in self.model_fields_set:
            _dict['write'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LatencyAnnotations from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "read": [LatencyAnnotationMetrics.from_dict(_item) for _item in obj["read"]] if obj.get("read") is not None else None,
            "write": [LatencyAnnotationMetrics.from_dict(_item) for _item in obj["write"]] if obj.get("write") is not None else None
        })
        return _obj


