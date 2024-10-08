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
from dscc.models.nimble_ns_shelf_ctrlr_attr_set import NimbleNsShelfCtrlrAttrSet
from dscc.models.nimble_ns_shelf_port_info import NimbleNsShelfPortInfo
from dscc.models.nimble_ns_shelf_sensor import NimbleNsShelfSensor
from typing import Optional, Set
from typing_extensions import Self

class NimbleNsShelfCtrlr(BaseModel):
    """
    NimbleNsShelfCtrlr
    """ # noqa: E501
    cached_serial: Optional[StrictStr] = Field(default=None, description="CachedSerial - Cached serial.")
    ctrlr_attrset_list: Optional[List[Optional[NimbleNsShelfCtrlrAttrSet]]] = Field(default=None, description="List of ctrlr attribute set for each logical controller.")
    ctrlr_hw_model: Optional[StrictStr] = Field(default=None, description="Controller hardware model. Possible values:'head_x9', 'head_x8', 'head_gen5_2u', 'es2_4u', 'head_vmware', 'es1_3u', 'head_x9_2u', 'head_x10', 'head_gen5', 'es3_4u', 'unknown'.")
    ctrlr_sensor_last_run: Optional[StrictInt] = Field(default=None, description="The time of last valid sensor reading, in epoch seconds.")
    ctrlr_sensors: Optional[List[Optional[NimbleNsShelfSensor]]] = Field(default=None, description="The list of individual sensor reading in this controller.")
    ctrlr_side: Optional[StrictStr] = Field(default=None, description="Position of this controller in the chassis. Possible values:'A', 'B', 'unknown'.")
    enc_loc_id: Optional[StrictInt] = Field(default=None, description="Location ID based on SAS topology.")
    exp_sas_addr: Optional[StrictStr] = Field(default=None, description="Expander SAS address.")
    extra_attributes: Optional[List[Optional[StrictStr]]] = Field(default=None, description="Extra attributes as attribute value pairs.")
    fan_overall_status: Optional[StrictStr] = Field(default=None, description="The overall status for the fans on this controller. Possible values:'Missing', 'Failed', 'OK', 'Alerted'.")
    hw_master_state: Optional[StrictStr] = Field(default=None, description="SES device hardware mastership state. Possible values:'not master', 'failed', 'unknown', 'master'.")
    hw_mship_failure: Optional[StrictBool] = Field(default=None, description="SES device hardware mastership failure.")
    identify_status: Optional[StrictBool] = Field(default=None, description="Status of chassis identifier.")
    port_info: Optional[List[Optional[NimbleNsShelfPortInfo]]] = Field(default=None, description="Port info for each SAS port.")
    psu_overall_status: Optional[StrictStr] = Field(default=None, description="The overall status for the PSU on this controller.. Possible values: 'OK', 'Alerted', 'Failed', 'Missing'.")
    sw_master_state: Optional[StrictStr] = Field(default=None, description="SES device software mastership state. Possible values:'not master', 'want master', 'unknown', 'master', 'release master'.")
    temp_overall_status: Optional[StrictStr] = Field(default=None, description="The overall status for the temperature of this controller.  Possible values:'Missing', 'Failed', 'OK', 'Alerted'.")
    __properties: ClassVar[List[str]] = ["cached_serial", "ctrlr_attrset_list", "ctrlr_hw_model", "ctrlr_sensor_last_run", "ctrlr_sensors", "ctrlr_side", "enc_loc_id", "exp_sas_addr", "extra_attributes", "fan_overall_status", "hw_master_state", "hw_mship_failure", "identify_status", "port_info", "psu_overall_status", "sw_master_state", "temp_overall_status"]

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
        """Create an instance of NimbleNsShelfCtrlr from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in ctrlr_attrset_list (list)
        _items = []
        if self.ctrlr_attrset_list:
            for _item in self.ctrlr_attrset_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ctrlr_attrset_list'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ctrlr_sensors (list)
        _items = []
        if self.ctrlr_sensors:
            for _item in self.ctrlr_sensors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ctrlr_sensors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in port_info (list)
        _items = []
        if self.port_info:
            for _item in self.port_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['port_info'] = _items
        # set to None if cached_serial (nullable) is None
        # and model_fields_set contains the field
        if self.cached_serial is None and "cached_serial" in self.model_fields_set:
            _dict['cached_serial'] = None

        # set to None if ctrlr_attrset_list (nullable) is None
        # and model_fields_set contains the field
        if self.ctrlr_attrset_list is None and "ctrlr_attrset_list" in self.model_fields_set:
            _dict['ctrlr_attrset_list'] = None

        # set to None if ctrlr_hw_model (nullable) is None
        # and model_fields_set contains the field
        if self.ctrlr_hw_model is None and "ctrlr_hw_model" in self.model_fields_set:
            _dict['ctrlr_hw_model'] = None

        # set to None if ctrlr_sensor_last_run (nullable) is None
        # and model_fields_set contains the field
        if self.ctrlr_sensor_last_run is None and "ctrlr_sensor_last_run" in self.model_fields_set:
            _dict['ctrlr_sensor_last_run'] = None

        # set to None if ctrlr_sensors (nullable) is None
        # and model_fields_set contains the field
        if self.ctrlr_sensors is None and "ctrlr_sensors" in self.model_fields_set:
            _dict['ctrlr_sensors'] = None

        # set to None if ctrlr_side (nullable) is None
        # and model_fields_set contains the field
        if self.ctrlr_side is None and "ctrlr_side" in self.model_fields_set:
            _dict['ctrlr_side'] = None

        # set to None if enc_loc_id (nullable) is None
        # and model_fields_set contains the field
        if self.enc_loc_id is None and "enc_loc_id" in self.model_fields_set:
            _dict['enc_loc_id'] = None

        # set to None if exp_sas_addr (nullable) is None
        # and model_fields_set contains the field
        if self.exp_sas_addr is None and "exp_sas_addr" in self.model_fields_set:
            _dict['exp_sas_addr'] = None

        # set to None if extra_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.extra_attributes is None and "extra_attributes" in self.model_fields_set:
            _dict['extra_attributes'] = None

        # set to None if fan_overall_status (nullable) is None
        # and model_fields_set contains the field
        if self.fan_overall_status is None and "fan_overall_status" in self.model_fields_set:
            _dict['fan_overall_status'] = None

        # set to None if hw_master_state (nullable) is None
        # and model_fields_set contains the field
        if self.hw_master_state is None and "hw_master_state" in self.model_fields_set:
            _dict['hw_master_state'] = None

        # set to None if hw_mship_failure (nullable) is None
        # and model_fields_set contains the field
        if self.hw_mship_failure is None and "hw_mship_failure" in self.model_fields_set:
            _dict['hw_mship_failure'] = None

        # set to None if identify_status (nullable) is None
        # and model_fields_set contains the field
        if self.identify_status is None and "identify_status" in self.model_fields_set:
            _dict['identify_status'] = None

        # set to None if port_info (nullable) is None
        # and model_fields_set contains the field
        if self.port_info is None and "port_info" in self.model_fields_set:
            _dict['port_info'] = None

        # set to None if psu_overall_status (nullable) is None
        # and model_fields_set contains the field
        if self.psu_overall_status is None and "psu_overall_status" in self.model_fields_set:
            _dict['psu_overall_status'] = None

        # set to None if sw_master_state (nullable) is None
        # and model_fields_set contains the field
        if self.sw_master_state is None and "sw_master_state" in self.model_fields_set:
            _dict['sw_master_state'] = None

        # set to None if temp_overall_status (nullable) is None
        # and model_fields_set contains the field
        if self.temp_overall_status is None and "temp_overall_status" in self.model_fields_set:
            _dict['temp_overall_status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleNsShelfCtrlr from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cached_serial": obj.get("cached_serial"),
            "ctrlr_attrset_list": [NimbleNsShelfCtrlrAttrSet.from_dict(_item) for _item in obj["ctrlr_attrset_list"]] if obj.get("ctrlr_attrset_list") is not None else None,
            "ctrlr_hw_model": obj.get("ctrlr_hw_model"),
            "ctrlr_sensor_last_run": obj.get("ctrlr_sensor_last_run"),
            "ctrlr_sensors": [NimbleNsShelfSensor.from_dict(_item) for _item in obj["ctrlr_sensors"]] if obj.get("ctrlr_sensors") is not None else None,
            "ctrlr_side": obj.get("ctrlr_side"),
            "enc_loc_id": obj.get("enc_loc_id"),
            "exp_sas_addr": obj.get("exp_sas_addr"),
            "extra_attributes": obj.get("extra_attributes"),
            "fan_overall_status": obj.get("fan_overall_status"),
            "hw_master_state": obj.get("hw_master_state"),
            "hw_mship_failure": obj.get("hw_mship_failure"),
            "identify_status": obj.get("identify_status"),
            "port_info": [NimbleNsShelfPortInfo.from_dict(_item) for _item in obj["port_info"]] if obj.get("port_info") is not None else None,
            "psu_overall_status": obj.get("psu_overall_status"),
            "sw_master_state": obj.get("sw_master_state"),
            "temp_overall_status": obj.get("temp_overall_status")
        })
        return _obj


