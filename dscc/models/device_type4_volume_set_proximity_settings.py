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
from dscc.models.device_type4_volume_set_host_group_list import DeviceType4VolumeSetHostGroupList
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4VolumeSetProximitySettings(BaseModel):
    """
    DeviceType4VolumeSetProximitySettings
    """ # noqa: E501
    items: Optional[List[DeviceType4VolumeSetHostGroupList]] = None
    page_limit: Optional[StrictInt] = Field(default=None, description="page limit", alias="pageLimit")
    page_offset: Optional[StrictInt] = Field(default=None, description="page offset", alias="pageOffset")
    resource_uri: Optional[StrictStr] = Field(default=None, description="Resource URI for volume set proximity details", alias="resourceURI")
    total: Optional[StrictInt] = Field(default=None, description="Total number of host groups")
    __properties: ClassVar[List[str]] = ["items", "pageLimit", "pageOffset", "resourceURI", "total"]

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
        """Create an instance of DeviceType4VolumeSetProximitySettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # set to None if items (nullable) is None
        # and model_fields_set contains the field
        if self.items is None and "items" in self.model_fields_set:
            _dict['items'] = None

        # set to None if page_limit (nullable) is None
        # and model_fields_set contains the field
        if self.page_limit is None and "page_limit" in self.model_fields_set:
            _dict['pageLimit'] = None

        # set to None if page_offset (nullable) is None
        # and model_fields_set contains the field
        if self.page_offset is None and "page_offset" in self.model_fields_set:
            _dict['pageOffset'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceURI'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4VolumeSetProximitySettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "items": [DeviceType4VolumeSetHostGroupList.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "pageLimit": obj.get("pageLimit"),
            "pageOffset": obj.get("pageOffset"),
            "resourceURI": obj.get("resourceURI"),
            "total": obj.get("total")
        })
        return _obj


