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
from dscc.models.common_resource_attributes import CommonResourceAttributes
from dscc.models.device_type4_associated_links_inner import DeviceType4AssociatedLinksInner
from dscc.models.device_type4_calendar import DeviceType4Calendar
from dscc.models.license_feature import LicenseFeature
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4Licenses(BaseModel):
    """
    System licenses
    """ # noqa: E501
    associated_links: Optional[List[DeviceType4AssociatedLinksInner]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    common_resource_attributes: Optional[CommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    disk_count: Optional[StrictStr] = Field(default=None, description="The disk count from the system license", alias="diskCount")
    features: Optional[Dict[str, Optional[List[Optional[LicenseFeature]]]]] = Field(default=None, description="The raw list of individual licensed features")
    issue_date: Optional[DeviceType4Calendar] = Field(default=None, alias="issueDate")
    request_uri: Optional[StrictStr] = Field(default=None, description="requestUri for detailed licenses object", alias="requestUri")
    resource_uri: Optional[StrictStr] = Field(default=None, description="Resource Uri", alias="resourceUri")
    type: Optional[StrictStr] = Field(default=None, description="Type of resource")
    version: Optional[StrictInt] = Field(default=None, description="The version number of the system licenses")
    __properties: ClassVar[List[str]] = ["associatedLinks", "commonResourceAttributes", "consoleUri", "customerId", "diskCount", "features", "issueDate", "requestUri", "resourceUri", "type", "version"]

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
        """Create an instance of DeviceType4Licenses from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in features (dict of array)
        _field_dict_of_array = {}
        if self.features:
            for _key in self.features:
                if self.features[_key] is not None:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.features[_key]
                    ]
            _dict['features'] = _field_dict_of_array
        # override the default output from pydantic by calling `to_dict()` of issue_date
        if self.issue_date:
            _dict['issueDate'] = self.issue_date.to_dict()
        # set to None if associated_links (nullable) is None
        # and model_fields_set contains the field
        if self.associated_links is None and "associated_links" in self.model_fields_set:
            _dict['associatedLinks'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if disk_count (nullable) is None
        # and model_fields_set contains the field
        if self.disk_count is None and "disk_count" in self.model_fields_set:
            _dict['diskCount'] = None

        # set to None if features (nullable) is None
        # and model_fields_set contains the field
        if self.features is None and "features" in self.model_fields_set:
            _dict['features'] = None

        # set to None if issue_date (nullable) is None
        # and model_fields_set contains the field
        if self.issue_date is None and "issue_date" in self.model_fields_set:
            _dict['issueDate'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestUri'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4Licenses from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedLinks": [DeviceType4AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "commonResourceAttributes": CommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "diskCount": obj.get("diskCount"),
            "features": dict(
                (_k,
                        [LicenseFeature.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("features", {}).items()
            ),
            "issueDate": DeviceType4Calendar.from_dict(obj["issueDate"]) if obj.get("issueDate") is not None else None,
            "requestUri": obj.get("requestUri"),
            "resourceUri": obj.get("resourceUri"),
            "type": obj.get("type"),
            "version": obj.get("version")
        })
        return _obj


