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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dscc.models.manufacturing_single import ManufacturingSingle
from dscc.models.state import State
from typing import Optional, Set
from typing_extensions import Self

class FcPortSfp(BaseModel):
    """
    FcPortSfp
    """ # noqa: E501
    fw_version: Optional[StrictStr] = Field(default=None, alias="fwVersion")
    manufacturing: Optional[ManufacturingSingle] = None
    name: Optional[StrictStr] = None
    qualified: Optional[StrictBool] = None
    rx_loss_pin: Optional[StrictStr] = Field(default=None, alias="rxLossPin")
    rx_power_low: Optional[StrictBool] = Field(default=None, alias="rxPowerLow")
    speed: Optional[StrictInt] = None
    state: Optional[State] = None
    tx_disable_pin: Optional[StrictStr] = Field(default=None, alias="txDisablePin")
    tx_fault_pin: Optional[StrictStr] = Field(default=None, alias="txFaultPin")
    __properties: ClassVar[List[str]] = ["fwVersion", "manufacturing", "name", "qualified", "rxLossPin", "rxPowerLow", "speed", "state", "txDisablePin", "txFaultPin"]

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
        """Create an instance of FcPortSfp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of manufacturing
        if self.manufacturing:
            _dict['manufacturing'] = self.manufacturing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # set to None if fw_version (nullable) is None
        # and model_fields_set contains the field
        if self.fw_version is None and "fw_version" in self.model_fields_set:
            _dict['fwVersion'] = None

        # set to None if manufacturing (nullable) is None
        # and model_fields_set contains the field
        if self.manufacturing is None and "manufacturing" in self.model_fields_set:
            _dict['manufacturing'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if qualified (nullable) is None
        # and model_fields_set contains the field
        if self.qualified is None and "qualified" in self.model_fields_set:
            _dict['qualified'] = None

        # set to None if rx_loss_pin (nullable) is None
        # and model_fields_set contains the field
        if self.rx_loss_pin is None and "rx_loss_pin" in self.model_fields_set:
            _dict['rxLossPin'] = None

        # set to None if rx_power_low (nullable) is None
        # and model_fields_set contains the field
        if self.rx_power_low is None and "rx_power_low" in self.model_fields_set:
            _dict['rxPowerLow'] = None

        # set to None if speed (nullable) is None
        # and model_fields_set contains the field
        if self.speed is None and "speed" in self.model_fields_set:
            _dict['speed'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if tx_disable_pin (nullable) is None
        # and model_fields_set contains the field
        if self.tx_disable_pin is None and "tx_disable_pin" in self.model_fields_set:
            _dict['txDisablePin'] = None

        # set to None if tx_fault_pin (nullable) is None
        # and model_fields_set contains the field
        if self.tx_fault_pin is None and "tx_fault_pin" in self.model_fields_set:
            _dict['txFaultPin'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FcPortSfp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fwVersion": obj.get("fwVersion"),
            "manufacturing": ManufacturingSingle.from_dict(obj["manufacturing"]) if obj.get("manufacturing") is not None else None,
            "name": obj.get("name"),
            "qualified": obj.get("qualified"),
            "rxLossPin": obj.get("rxLossPin"),
            "rxPowerLow": obj.get("rxPowerLow"),
            "speed": obj.get("speed"),
            "state": State.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "txDisablePin": obj.get("txDisablePin"),
            "txFaultPin": obj.get("txFaultPin")
        })
        return _obj


