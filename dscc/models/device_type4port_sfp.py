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
from dscc.models.device_type4_manufacturing_single import DeviceType4ManufacturingSingle
from dscc.models.device_type4_state import DeviceType4State
from dscc.models.device_type4rx_loss_pin import DeviceType4rxLossPin
from dscc.models.device_type4tx_disable_pin import DeviceType4txDisablePin
from dscc.models.device_type4tx_fault_pin import DeviceType4txFaultPin
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4portSfp(BaseModel):
    """
    DeviceType4portSfp
    """ # noqa: E501
    fw_version: Optional[StrictStr] = Field(default=None, description="Firmware version", alias="fwVersion")
    manufacturing: Optional[DeviceType4ManufacturingSingle] = None
    qualified: Optional[StrictBool] = Field(default=None, description="Indicates if the SFP is qualified or not")
    rx_loss_pin: Optional[DeviceType4rxLossPin] = Field(default=None, alias="rxLossPin")
    rx_power_low: Optional[StrictBool] = Field(default=None, description="Indicates if RX power is low or not", alias="rxPowerLow")
    speed: Optional[StrictInt] = Field(default=None, description="Speed in bits per second")
    state: Optional[DeviceType4State] = None
    support_ddm: Optional[StrictBool] = Field(default=None, description="Indicates if the SFP supports DDM", alias="supportDDM")
    tx_disable_pin: Optional[DeviceType4txDisablePin] = Field(default=None, alias="txDisablePin")
    tx_fault_pin: Optional[DeviceType4txFaultPin] = Field(default=None, alias="txFaultPin")
    __properties: ClassVar[List[str]] = ["fwVersion", "manufacturing", "qualified", "rxLossPin", "rxPowerLow", "speed", "state", "supportDDM", "txDisablePin", "txFaultPin"]

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
        """Create an instance of DeviceType4portSfp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rx_loss_pin
        if self.rx_loss_pin:
            _dict['rxLossPin'] = self.rx_loss_pin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tx_disable_pin
        if self.tx_disable_pin:
            _dict['txDisablePin'] = self.tx_disable_pin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tx_fault_pin
        if self.tx_fault_pin:
            _dict['txFaultPin'] = self.tx_fault_pin.to_dict()
        # set to None if fw_version (nullable) is None
        # and model_fields_set contains the field
        if self.fw_version is None and "fw_version" in self.model_fields_set:
            _dict['fwVersion'] = None

        # set to None if manufacturing (nullable) is None
        # and model_fields_set contains the field
        if self.manufacturing is None and "manufacturing" in self.model_fields_set:
            _dict['manufacturing'] = None

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

        # set to None if support_ddm (nullable) is None
        # and model_fields_set contains the field
        if self.support_ddm is None and "support_ddm" in self.model_fields_set:
            _dict['supportDDM'] = None

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
        """Create an instance of DeviceType4portSfp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fwVersion": obj.get("fwVersion"),
            "manufacturing": DeviceType4ManufacturingSingle.from_dict(obj["manufacturing"]) if obj.get("manufacturing") is not None else None,
            "qualified": obj.get("qualified"),
            "rxLossPin": DeviceType4rxLossPin.from_dict(obj["rxLossPin"]) if obj.get("rxLossPin") is not None else None,
            "rxPowerLow": obj.get("rxPowerLow"),
            "speed": obj.get("speed"),
            "state": DeviceType4State.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "supportDDM": obj.get("supportDDM"),
            "txDisablePin": DeviceType4txDisablePin.from_dict(obj["txDisablePin"]) if obj.get("txDisablePin") is not None else None,
            "txFaultPin": DeviceType4txFaultPin.from_dict(obj["txFaultPin"]) if obj.get("txFaultPin") is not None else None
        })
        return _obj


