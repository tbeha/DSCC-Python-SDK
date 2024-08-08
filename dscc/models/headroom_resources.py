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
from dscc.models.time_series_data import TimeSeriesData
from typing import Optional, Set
from typing_extensions import Self

class HeadroomResources(BaseModel):
    """
    HeadroomResources
    """ # noqa: E501
    resource_name: Optional[StrictStr] = Field(default=None, description="Name of the resource", alias="resourceName")
    series_data: Optional[List[TimeSeriesData]] = Field(default=None, alias="seriesData")
    __properties: ClassVar[List[str]] = ["resourceName", "seriesData"]

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
        """Create an instance of HeadroomResources from a JSON string"""
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
            _dict['seriesData'] = _items
        # set to None if resource_name (nullable) is None
        # and model_fields_set contains the field
        if self.resource_name is None and "resource_name" in self.model_fields_set:
            _dict['resourceName'] = None

        # set to None if series_data (nullable) is None
        # and model_fields_set contains the field
        if self.series_data is None and "series_data" in self.model_fields_set:
            _dict['seriesData'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeadroomResources from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "resourceName": obj.get("resourceName"),
            "seriesData": [TimeSeriesData.from_dict(_item) for _item in obj["seriesData"]] if obj.get("seriesData") is not None else None
        })
        return _obj


