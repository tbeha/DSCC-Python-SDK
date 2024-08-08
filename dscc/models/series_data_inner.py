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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from dscc.models.histogram_bucket_inner import HistogramBucketInner
from typing import Optional, Set
from typing_extensions import Self

class SeriesDataInner(BaseModel):
    """
    SeriesDataInner
    """ # noqa: E501
    read_buckets: Optional[List[Optional[HistogramBucketInner]]] = Field(default=None, description="Histogram data of io buckets", alias="readBuckets")
    timestamp: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Timestamp in epoch milliseconds for which the metrics are listed")
    write_buckets: Optional[List[Optional[HistogramBucketInner]]] = Field(default=None, description="Histogram data of io buckets", alias="writeBuckets")
    __properties: ClassVar[List[str]] = ["readBuckets", "timestamp", "writeBuckets"]

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
        """Create an instance of SeriesDataInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in read_buckets (list)
        _items = []
        if self.read_buckets:
            for _item in self.read_buckets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['readBuckets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in write_buckets (list)
        _items = []
        if self.write_buckets:
            for _item in self.write_buckets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['writeBuckets'] = _items
        # set to None if read_buckets (nullable) is None
        # and model_fields_set contains the field
        if self.read_buckets is None and "read_buckets" in self.model_fields_set:
            _dict['readBuckets'] = None

        # set to None if write_buckets (nullable) is None
        # and model_fields_set contains the field
        if self.write_buckets is None and "write_buckets" in self.model_fields_set:
            _dict['writeBuckets'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SeriesDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "readBuckets": [HistogramBucketInner.from_dict(_item) for _item in obj["readBuckets"]] if obj.get("readBuckets") is not None else None,
            "timestamp": obj.get("timestamp"),
            "writeBuckets": [HistogramBucketInner.from_dict(_item) for _item in obj["writeBuckets"]] if obj.get("writeBuckets") is not None else None
        })
        return _obj


