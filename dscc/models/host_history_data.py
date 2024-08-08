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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from dscc.models.host_perf_history import HostPerfHistory
from typing import Optional, Set
from typing_extensions import Self

class HostHistoryData(BaseModel):
    """
    Performance history data for given time range and granularily for a volume
    """ # noqa: E501
    iops_metrics_data: Optional[List[Optional[HostPerfHistory]]] = Field(default=None, alias="iopsMetricsData")
    latency_metrics_data_ms: Optional[List[Optional[HostPerfHistory]]] = Field(default=None, alias="latencyMetricsDataMs")
    throughput_metrics_data_kbps: Optional[List[Optional[HostPerfHistory]]] = Field(default=None, alias="throughputMetricsDataKbps")
    __properties: ClassVar[List[str]] = ["iopsMetricsData", "latencyMetricsDataMs", "throughputMetricsDataKbps"]

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
        """Create an instance of HostHistoryData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in iops_metrics_data (list)
        _items = []
        if self.iops_metrics_data:
            for _item in self.iops_metrics_data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['iopsMetricsData'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in latency_metrics_data_ms (list)
        _items = []
        if self.latency_metrics_data_ms:
            for _item in self.latency_metrics_data_ms:
                if _item:
                    _items.append(_item.to_dict())
            _dict['latencyMetricsDataMs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in throughput_metrics_data_kbps (list)
        _items = []
        if self.throughput_metrics_data_kbps:
            for _item in self.throughput_metrics_data_kbps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['throughputMetricsDataKbps'] = _items
        # set to None if iops_metrics_data (nullable) is None
        # and model_fields_set contains the field
        if self.iops_metrics_data is None and "iops_metrics_data" in self.model_fields_set:
            _dict['iopsMetricsData'] = None

        # set to None if latency_metrics_data_ms (nullable) is None
        # and model_fields_set contains the field
        if self.latency_metrics_data_ms is None and "latency_metrics_data_ms" in self.model_fields_set:
            _dict['latencyMetricsDataMs'] = None

        # set to None if throughput_metrics_data_kbps (nullable) is None
        # and model_fields_set contains the field
        if self.throughput_metrics_data_kbps is None and "throughput_metrics_data_kbps" in self.model_fields_set:
            _dict['throughputMetricsDataKbps'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HostHistoryData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "iopsMetricsData": [HostPerfHistory.from_dict(_item) for _item in obj["iopsMetricsData"]] if obj.get("iopsMetricsData") is not None else None,
            "latencyMetricsDataMs": [HostPerfHistory.from_dict(_item) for _item in obj["latencyMetricsDataMs"]] if obj.get("latencyMetricsDataMs") is not None else None,
            "throughputMetricsDataKbps": [HostPerfHistory.from_dict(_item) for _item in obj["throughputMetricsDataKbps"]] if obj.get("throughputMetricsDataKbps") is not None else None
        })
        return _obj


