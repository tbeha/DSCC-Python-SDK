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
from dscc.models.associated_links_inner import AssociatedLinksInner
from dscc.models.device_type4calendar_time import DeviceType4calendarTime
from dscc.models.device_type4sw_recommended_package_id import DeviceType4swRecommendedPackageId
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4Recommendation(BaseModel):
    """
    Reccomendations for the device
    """ # noqa: E501
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    check_time: Optional[DeviceType4calendarTime] = Field(default=None, alias="checkTime")
    displayname: Optional[StrictStr] = Field(default=None, description="Display name")
    domain: Optional[StrictStr] = Field(default=None, description="Domain that the resource belongs to")
    id: Optional[StrictStr] = Field(default=None, description="SystemWWN/UUID string uniquely identifying the object.")
    patches: Optional[List[Optional[DeviceType4swRecommendedPackageId]]] = None
    releases: Optional[List[Optional[DeviceType4swRecommendedPackageId]]] = None
    request_uri: Optional[StrictStr] = Field(default=None, description="requestUri for detailed storage object", alias="requestUri")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed storage object", alias="resourceUri")
    system_id: Optional[StrictStr] = Field(default=None, description="SystemUid/serialNumber of the array.", alias="systemId")
    update_time: Optional[DeviceType4calendarTime] = Field(default=None, alias="updateTime")
    __properties: ClassVar[List[str]] = ["associatedLinks", "checkTime", "displayname", "domain", "id", "patches", "releases", "requestUri", "resourceUri", "systemId", "updateTime"]

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
        """Create an instance of DeviceType4Recommendation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in associated_links (list)
        _items = []
        if self.associated_links:
            for _item in self.associated_links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['associatedLinks'] = _items
        # override the default output from pydantic by calling `to_dict()` of check_time
        if self.check_time:
            _dict['checkTime'] = self.check_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in patches (list)
        _items = []
        if self.patches:
            for _item in self.patches:
                if _item:
                    _items.append(_item.to_dict())
            _dict['patches'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in releases (list)
        _items = []
        if self.releases:
            for _item in self.releases:
                if _item:
                    _items.append(_item.to_dict())
            _dict['releases'] = _items
        # override the default output from pydantic by calling `to_dict()` of update_time
        if self.update_time:
            _dict['updateTime'] = self.update_time.to_dict()
        # set to None if associated_links (nullable) is None
        # and model_fields_set contains the field
        if self.associated_links is None and "associated_links" in self.model_fields_set:
            _dict['associatedLinks'] = None

        # set to None if check_time (nullable) is None
        # and model_fields_set contains the field
        if self.check_time is None and "check_time" in self.model_fields_set:
            _dict['checkTime'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestUri'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if system_id (nullable) is None
        # and model_fields_set contains the field
        if self.system_id is None and "system_id" in self.model_fields_set:
            _dict['systemId'] = None

        # set to None if update_time (nullable) is None
        # and model_fields_set contains the field
        if self.update_time is None and "update_time" in self.model_fields_set:
            _dict['updateTime'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4Recommendation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedLinks": [AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "checkTime": DeviceType4calendarTime.from_dict(obj["checkTime"]) if obj.get("checkTime") is not None else None,
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "id": obj.get("id"),
            "patches": [DeviceType4swRecommendedPackageId.from_dict(_item) for _item in obj["patches"]] if obj.get("patches") is not None else None,
            "releases": [DeviceType4swRecommendedPackageId.from_dict(_item) for _item in obj["releases"]] if obj.get("releases") is not None else None,
            "requestUri": obj.get("requestUri"),
            "resourceUri": obj.get("resourceUri"),
            "systemId": obj.get("systemId"),
            "updateTime": DeviceType4calendarTime.from_dict(obj["updateTime"]) if obj.get("updateTime") is not None else None
        })
        return _obj


