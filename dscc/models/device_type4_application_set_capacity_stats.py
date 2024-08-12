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
from typing_extensions import Annotated
from dscc.models.associated_links_inner import AssociatedLinksInner
from dscc.models.common_resource_attributes import CommonResourceAttributes
from dscc.models.device_type4_application_set_capacity_stats_capacity_summary import DeviceType4ApplicationSetCapacityStatsCapacitySummary
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4ApplicationSetCapacityStats(BaseModel):
    """
    DeviceType4ApplicationSetCapacityStats
    """ # noqa: E501
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    capacity_summary: Optional[DeviceType4ApplicationSetCapacityStatsCapacitySummary] = Field(default=None, alias="capacitySummary")
    common_resource_attributes: Optional[CommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    customer_id: Optional[StrictStr] = Field(default=None, description="The customer application identifier", alias="customerId")
    id: Optional[StrictStr] = Field(default=None, description="Uid of the applicationset")
    members: Optional[List[Optional[StrictStr]]] = Field(default=None, description="Volume Names")
    name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Name of the application set")
    request_uri: Optional[StrictStr] = Field(default=None, description="RequestUri for applicationsets resources", alias="requestUri")
    system_id: Optional[StrictStr] = Field(default=None, description="SystemId/serialNumber of the array.", alias="systemId")
    __properties: ClassVar[List[str]] = ["associatedLinks", "capacitySummary", "commonResourceAttributes", "customerId", "id", "members", "name", "requestUri", "systemId"]

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
        """Create an instance of DeviceType4ApplicationSetCapacityStats from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of capacity_summary
        if self.capacity_summary:
            _dict['capacitySummary'] = self.capacity_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # set to None if capacity_summary (nullable) is None
        # and model_fields_set contains the field
        if self.capacity_summary is None and "capacity_summary" in self.model_fields_set:
            _dict['capacitySummary'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if members (nullable) is None
        # and model_fields_set contains the field
        if self.members is None and "members" in self.model_fields_set:
            _dict['members'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestUri'] = None

        # set to None if system_id (nullable) is None
        # and model_fields_set contains the field
        if self.system_id is None and "system_id" in self.model_fields_set:
            _dict['systemId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4ApplicationSetCapacityStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedLinks": [AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "capacitySummary": DeviceType4ApplicationSetCapacityStatsCapacitySummary.from_dict(obj["capacitySummary"]) if obj.get("capacitySummary") is not None else None,
            "commonResourceAttributes": CommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "customerId": obj.get("customerId"),
            "id": obj.get("id"),
            "members": obj.get("members"),
            "name": obj.get("name"),
            "requestUri": obj.get("requestUri"),
            "systemId": obj.get("systemId")
        })
        return _obj


