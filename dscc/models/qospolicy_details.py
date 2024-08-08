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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from dscc.models.capped_obj_data import CappedObjData
from dscc.models.uncapped_obj_data import UncappedObjData
from typing import Optional, Set
from typing_extensions import Self

class QospolicyDetails(BaseModel):
    """
    QoS policy details for given time range for a device
    """ # noqa: E501
    qos_capped_objs_data: Optional[CappedObjData] = Field(default=None, alias="qosCappedObjsData")
    qos_un_capped_objs_data: Optional[UncappedObjData] = Field(default=None, alias="qosUnCappedObjsData")
    recvd_total: Optional[StrictInt] = Field(default=None, description="Total number of received QoS policy details for a device based on the given query parameters", alias="recvdTotal")
    total: Optional[StrictInt] = Field(default=None, description="Total number of QoS policy details for a device based on the given query parameters")
    __properties: ClassVar[List[str]] = ["qosCappedObjsData", "qosUnCappedObjsData", "recvdTotal", "total"]

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
        """Create an instance of QospolicyDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of qos_capped_objs_data
        if self.qos_capped_objs_data:
            _dict['qosCappedObjsData'] = self.qos_capped_objs_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of qos_un_capped_objs_data
        if self.qos_un_capped_objs_data:
            _dict['qosUnCappedObjsData'] = self.qos_un_capped_objs_data.to_dict()
        # set to None if qos_capped_objs_data (nullable) is None
        # and model_fields_set contains the field
        if self.qos_capped_objs_data is None and "qos_capped_objs_data" in self.model_fields_set:
            _dict['qosCappedObjsData'] = None

        # set to None if qos_un_capped_objs_data (nullable) is None
        # and model_fields_set contains the field
        if self.qos_un_capped_objs_data is None and "qos_un_capped_objs_data" in self.model_fields_set:
            _dict['qosUnCappedObjsData'] = None

        # set to None if recvd_total (nullable) is None
        # and model_fields_set contains the field
        if self.recvd_total is None and "recvd_total" in self.model_fields_set:
            _dict['recvdTotal'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QospolicyDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "qosCappedObjsData": CappedObjData.from_dict(obj["qosCappedObjsData"]) if obj.get("qosCappedObjsData") is not None else None,
            "qosUnCappedObjsData": UncappedObjData.from_dict(obj["qosUnCappedObjsData"]) if obj.get("qosUnCappedObjsData") is not None else None,
            "recvdTotal": obj.get("recvdTotal"),
            "total": obj.get("total")
        })
        return _obj


