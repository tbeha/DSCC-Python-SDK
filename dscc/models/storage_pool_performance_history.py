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
from dscc.models.nimble_common_resource_attributes import NimbleCommonResourceAttributes
from dscc.models.nimblehistorical_metric_data import NimblehistoricalMetricData
from typing import Optional, Set
from typing_extensions import Self

class StoragePoolPerformanceHistory(BaseModel):
    """
    storage pool performance trends for given granularity and time range
    """ # noqa: E501
    common_resource_attributes: Optional[NimbleCommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    iops_metrics_data: Optional[NimblehistoricalMetricData] = None
    latency_metrics_data: Optional[NimblehistoricalMetricData] = None
    request_uri: Optional[StrictStr] = Field(default=None, description="requestUri for detailed storage object", alias="requestURI")
    throughput_metrics_data: Optional[NimblehistoricalMetricData] = None
    __properties: ClassVar[List[str]] = ["commonResourceAttributes", "iops_metrics_data", "latency_metrics_data", "requestURI", "throughput_metrics_data"]

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
        """Create an instance of StoragePoolPerformanceHistory from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of iops_metrics_data
        if self.iops_metrics_data:
            _dict['iops_metrics_data'] = self.iops_metrics_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of latency_metrics_data
        if self.latency_metrics_data:
            _dict['latency_metrics_data'] = self.latency_metrics_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of throughput_metrics_data
        if self.throughput_metrics_data:
            _dict['throughput_metrics_data'] = self.throughput_metrics_data.to_dict()
        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if iops_metrics_data (nullable) is None
        # and model_fields_set contains the field
        if self.iops_metrics_data is None and "iops_metrics_data" in self.model_fields_set:
            _dict['iops_metrics_data'] = None

        # set to None if latency_metrics_data (nullable) is None
        # and model_fields_set contains the field
        if self.latency_metrics_data is None and "latency_metrics_data" in self.model_fields_set:
            _dict['latency_metrics_data'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestURI'] = None

        # set to None if throughput_metrics_data (nullable) is None
        # and model_fields_set contains the field
        if self.throughput_metrics_data is None and "throughput_metrics_data" in self.model_fields_set:
            _dict['throughput_metrics_data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StoragePoolPerformanceHistory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "commonResourceAttributes": NimbleCommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "iops_metrics_data": NimblehistoricalMetricData.from_dict(obj["iops_metrics_data"]) if obj.get("iops_metrics_data") is not None else None,
            "latency_metrics_data": NimblehistoricalMetricData.from_dict(obj["latency_metrics_data"]) if obj.get("latency_metrics_data") is not None else None,
            "requestURI": obj.get("requestURI"),
            "throughput_metrics_data": NimblehistoricalMetricData.from_dict(obj["throughput_metrics_data"]) if obj.get("throughput_metrics_data") is not None else None
        })
        return _obj


