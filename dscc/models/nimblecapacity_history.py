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
from dscc.models.nimblecapacity_series_data import NimblecapacitySeriesData
from typing import Optional, Set
from typing_extensions import Self

class NimblecapacityHistory(BaseModel):
    """
    capacity performance trends for given granularity
    """ # noqa: E501
    count: Optional[StrictInt] = Field(default=None, description="count of series data")
    request_uri: Optional[StrictStr] = Field(default=None, description="requestUri for detailed storage object", alias="requestURI")
    series_data: Optional[List[Optional[NimblecapacitySeriesData]]] = None
    __properties: ClassVar[List[str]] = ["count", "requestURI", "series_data"]

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
        """Create an instance of NimblecapacityHistory from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in series_data (list)
        _items = []
        if self.series_data:
            for _item in self.series_data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['series_data'] = _items
        # set to None if count (nullable) is None
        # and model_fields_set contains the field
        if self.count is None and "count" in self.model_fields_set:
            _dict['count'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestURI'] = None

        # set to None if series_data (nullable) is None
        # and model_fields_set contains the field
        if self.series_data is None and "series_data" in self.model_fields_set:
            _dict['series_data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimblecapacityHistory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "requestURI": obj.get("requestURI"),
            "series_data": [NimblecapacitySeriesData.from_dict(_item) for _item in obj["series_data"]] if obj.get("series_data") is not None else None
        })
        return _obj


