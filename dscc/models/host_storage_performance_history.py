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
from dscc.models.host_history_data import HostHistoryData
from typing import Optional, Set
from typing_extensions import Self

class HostStoragePerformanceHistory(BaseModel):
    """
    HostStoragePerformanceHistory
    """ # noqa: E501
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    host_volume_perf_trend_data: Optional[HostHistoryData] = Field(default=None, alias="hostVolumePerfTrendData")
    request_uri: Optional[StrictStr] = Field(default=None, description="requestUri for host storage performance history data", alias="requestURI")
    __properties: ClassVar[List[str]] = ["customerId", "hostVolumePerfTrendData", "requestURI"]

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
        """Create an instance of HostStoragePerformanceHistory from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of host_volume_perf_trend_data
        if self.host_volume_perf_trend_data:
            _dict['hostVolumePerfTrendData'] = self.host_volume_perf_trend_data.to_dict()
        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if host_volume_perf_trend_data (nullable) is None
        # and model_fields_set contains the field
        if self.host_volume_perf_trend_data is None and "host_volume_perf_trend_data" in self.model_fields_set:
            _dict['hostVolumePerfTrendData'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestURI'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HostStoragePerformanceHistory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customerId": obj.get("customerId"),
            "hostVolumePerfTrendData": HostHistoryData.from_dict(obj["hostVolumePerfTrendData"]) if obj.get("hostVolumePerfTrendData") is not None else None,
            "requestURI": obj.get("requestURI")
        })
        return _obj


