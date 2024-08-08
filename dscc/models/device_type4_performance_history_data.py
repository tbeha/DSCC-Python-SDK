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
from dscc.models.common_resource_attributes_perf import CommonResourceAttributesPerf
from dscc.models.device_type4_performance_history_data_history_data import DeviceType4PerformanceHistoryDataHistoryData
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4PerformanceHistoryData(BaseModel):
    """
    performance trends for given granularity and time range for a component
    """ # noqa: E501
    common_resource_attributes: Optional[CommonResourceAttributesPerf] = Field(default=None, alias="commonResourceAttributes")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    end_time: Optional[StrictInt] = Field(default=None, description="end time of history data", alias="endTime")
    history_data: Optional[DeviceType4PerformanceHistoryDataHistoryData] = Field(default=None, alias="historyData")
    request_uri: Optional[StrictStr] = Field(default=None, description="requestUri for detailed storage object", alias="requestUri")
    start_time: Optional[StrictInt] = Field(default=None, description="start time of history data", alias="startTime")
    __properties: ClassVar[List[str]] = ["commonResourceAttributes", "customerId", "endTime", "historyData", "requestUri", "startTime"]

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
        """Create an instance of DeviceType4PerformanceHistoryData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of history_data
        if self.history_data:
            _dict['historyData'] = self.history_data.to_dict()
        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if end_time (nullable) is None
        # and model_fields_set contains the field
        if self.end_time is None and "end_time" in self.model_fields_set:
            _dict['endTime'] = None

        # set to None if history_data (nullable) is None
        # and model_fields_set contains the field
        if self.history_data is None and "history_data" in self.model_fields_set:
            _dict['historyData'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestUri'] = None

        # set to None if start_time (nullable) is None
        # and model_fields_set contains the field
        if self.start_time is None and "start_time" in self.model_fields_set:
            _dict['startTime'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4PerformanceHistoryData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "commonResourceAttributes": CommonResourceAttributesPerf.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "customerId": obj.get("customerId"),
            "endTime": obj.get("endTime"),
            "historyData": DeviceType4PerformanceHistoryDataHistoryData.from_dict(obj["historyData"]) if obj.get("historyData") is not None else None,
            "requestUri": obj.get("requestUri"),
            "startTime": obj.get("startTime")
        })
        return _obj


