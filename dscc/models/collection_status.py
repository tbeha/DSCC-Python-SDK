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
from dscc.models.collection_status_config_status import CollectionStatusConfigStatus
from dscc.models.hstatus import Hstatus
from typing import Optional, Set
from typing_extensions import Self

class CollectionStatus(BaseModel):
    """
    CollectionStatus
    """ # noqa: E501
    config_status: Optional[CollectionStatusConfigStatus] = Field(default=None, alias="configStatus")
    metric_status: Optional[CollectionStatusConfigStatus] = Field(default=None, alias="metricStatus")
    over_all_status: Optional[Hstatus] = Field(default=None, alias="overAllStatus")
    __properties: ClassVar[List[str]] = ["configStatus", "metricStatus", "overAllStatus"]

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
        """Create an instance of CollectionStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of config_status
        if self.config_status:
            _dict['configStatus'] = self.config_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metric_status
        if self.metric_status:
            _dict['metricStatus'] = self.metric_status.to_dict()
        # set to None if config_status (nullable) is None
        # and model_fields_set contains the field
        if self.config_status is None and "config_status" in self.model_fields_set:
            _dict['configStatus'] = None

        # set to None if metric_status (nullable) is None
        # and model_fields_set contains the field
        if self.metric_status is None and "metric_status" in self.model_fields_set:
            _dict['metricStatus'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CollectionStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "configStatus": CollectionStatusConfigStatus.from_dict(obj["configStatus"]) if obj.get("configStatus") is not None else None,
            "metricStatus": CollectionStatusConfigStatus.from_dict(obj["metricStatus"]) if obj.get("metricStatus") is not None else None,
            "overAllStatus": obj.get("overAllStatus")
        })
        return _obj


