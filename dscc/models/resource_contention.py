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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dscc.models.associated_links_inner import AssociatedLinksInner
from dscc.models.resource_contention_data import ResourceContentionData
from typing import Optional, Set
from typing_extensions import Self

class ResourceContention(BaseModel):
    """
    Resource contention response structure
    """ # noqa: E501
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    cpu_contention: Optional[ResourceContentionData] = Field(default=None, alias="cpuContention")
    customer_id: Optional[StrictStr] = Field(default=None, description="CustomerId", alias="customerId")
    disk_contention: Optional[ResourceContentionData] = Field(default=None, alias="diskContention")
    end_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="End time of the interval for which resource contention is computed", alias="endTime")
    request_uri: Optional[StrictStr] = Field(default=None, description="requestUri for HPE Alletra Storage MP insights resource contention", alias="requestUri")
    start_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Start time of the interval for which resource contention is computed", alias="startTime")
    system_id: Optional[StrictStr] = Field(default=None, description="Serial number of the array", alias="systemId")
    __properties: ClassVar[List[str]] = ["associatedLinks", "cpuContention", "customerId", "diskContention", "endTime", "requestUri", "startTime", "systemId"]

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
        """Create an instance of ResourceContention from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cpu_contention
        if self.cpu_contention:
            _dict['cpuContention'] = self.cpu_contention.to_dict()
        # override the default output from pydantic by calling `to_dict()` of disk_contention
        if self.disk_contention:
            _dict['diskContention'] = self.disk_contention.to_dict()
        # set to None if associated_links (nullable) is None
        # and model_fields_set contains the field
        if self.associated_links is None and "associated_links" in self.model_fields_set:
            _dict['associatedLinks'] = None

        # set to None if cpu_contention (nullable) is None
        # and model_fields_set contains the field
        if self.cpu_contention is None and "cpu_contention" in self.model_fields_set:
            _dict['cpuContention'] = None

        # set to None if disk_contention (nullable) is None
        # and model_fields_set contains the field
        if self.disk_contention is None and "disk_contention" in self.model_fields_set:
            _dict['diskContention'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestUri'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResourceContention from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedLinks": [AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "cpuContention": ResourceContentionData.from_dict(obj["cpuContention"]) if obj.get("cpuContention") is not None else None,
            "customerId": obj.get("customerId"),
            "diskContention": ResourceContentionData.from_dict(obj["diskContention"]) if obj.get("diskContention") is not None else None,
            "endTime": obj.get("endTime"),
            "requestUri": obj.get("requestUri"),
            "startTime": obj.get("startTime"),
            "systemId": obj.get("systemId")
        })
        return _obj


