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
from dscc.models.associated_links_inner import AssociatedLinksInner
from dscc.models.nimble_common_resource_attributes import NimbleCommonResourceAttributes
from dscc.models.nimble_ns_ctrlr_hw_sensor_info import NimbleNsCtrlrHwSensorInfo
from dscc.models.nimble_ns_ctrlr_nvme_card import NimbleNsCtrlrNvmeCard
from dscc.models.nimble_ns_ctrlr_raid_info import NimbleNsCtrlrRaidInfo
from typing import Optional, Set
from typing_extensions import Self

class NimbleControllerDetailsWithRequestUri(BaseModel):
    """
    NimbleControllerDetailsWithRequestUri
    """ # noqa: E501
    request_uri: Optional[StrictStr] = Field(default=None, description="requestUri for detailed controller object", alias="requestUri")
    array_id: Optional[StrictStr] = Field(default=None, description="Rest ID of the array containing this controller.")
    array_name: Optional[StrictStr] = Field(default=None, description="Name of the array containing this controller.")
    id: Optional[StrictStr] = Field(default=None, description="Identifier of the controller.")
    name: Optional[StrictStr] = Field(default=None, description="Name of the controller.")
    serial: Optional[StrictStr] = Field(default=None, description="Serial number for this controller.")
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details")
    asup_time: Optional[StrictInt] = Field(default=None, description="Time of the last autosupport by the controller.")
    common_resource_attributes: Optional[NimbleCommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    ctrlr_side: Optional[StrictStr] = Field(default=None, description="Identifies which controller this is on its array. Possible values: 'A', 'B'.")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    fan_status: Optional[StrictStr] = Field(default=None, description="Overall fan status for the controller. Possible values: 'fan_failed', 'fan_okay', 'fan_alerted', 'fan_unknown'.")
    fans: Optional[List[Optional[NimbleNsCtrlrHwSensorInfo]]] = Field(default=None, description="Status for each fan in the controller.")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    hostname: Optional[StrictStr] = Field(default=None, description="Host name for the controller.")
    nvme_cards: Optional[List[Optional[NimbleNsCtrlrNvmeCard]]] = Field(default=None, description="List of NVMe accelerator cards.")
    nvme_cards_enabled: Optional[StrictInt] = Field(default=None, description="Indicates if the NVMe accelerator card is enabled.")
    partial_response_ok: Optional[StrictBool] = Field(default=None, description="Indicate that it is ok to provide partially available response.")
    partition_status: Optional[List[NimbleNsCtrlrRaidInfo]] = Field(default=None, description="Status of the system's raid partitions.")
    power_status: Optional[StrictStr] = Field(default=None, description="Overall power supply status for the controller. Possible values: 'ps_alerted', 'ps_okay', 'ps_failed', 'ps_unknown'.")
    power_supplies: Optional[List[Optional[NimbleNsCtrlrHwSensorInfo]]] = Field(default=None, description="Status for each power supply in the controller.")
    resource_uri: Optional[StrictStr] = Field(default=None, description="Link to the object URI", alias="resourceUri")
    state: Optional[StrictStr] = Field(default=None, description="Indicates whether this controller is active or not. Possible values: 'start_active', 'start_standby', 'stale', 'standby', 'active', 'solo', 'none'.")
    support_address: Optional[StrictStr] = Field(default=None, description="IP address used for support.")
    support_netmask: Optional[StrictStr] = Field(default=None, description="IP netmask used for support.")
    support_nic: Optional[StrictStr] = Field(default=None, description="Network card used for support.")
    temperature_sensors: Optional[List[Optional[NimbleNsCtrlrHwSensorInfo]]] = Field(default=None, description="Status for temperature sensor in the controller.")
    temperature_status: Optional[StrictStr] = Field(default=None, description="Overall temperature status for the controller. Possible values: 'temperature_unknown', 'temperature_alerted', 'temperature_okay', 'temperature_fail'.")
    type: Optional[StrictStr] = Field(default=None, description="type")
    update_end_time: Optional[StrictInt] = Field(default=None, description="End time of last update. Seconds since last epoch i.e. 00:00 January 1, 1970.")
    update_error_code: Optional[StrictStr] = Field(default=None, description="If the software update has failed, this indicates the error code corresponding to the failure. Non-negative integer in range [0,9000].")
    update_progress_msg: Optional[StrictStr] = Field(default=None, description="Group update detailed progress message. Plain string.")
    update_start_time: Optional[StrictInt] = Field(default=None, description="Start time of last update. Seconds since last epoch i.e. 00:00 January 1, 1970.")
    update_state: Optional[StrictStr] = Field(default=None, description="Group update state.Possible values: 'invalid', 'normal', 'updating', 'timed_out', 'failed', 'paused'.")
    version_current: Optional[StrictStr] = Field(default=None, description="Version of software running on the group.")
    version_rollback: Optional[StrictStr] = Field(default=None, description="Rollback software version for the group.")
    version_target: Optional[StrictStr] = Field(default=None, description="Desired software version for the group.")
    __properties: ClassVar[List[str]] = ["array_id", "array_name", "id", "name", "serial", "associated_links", "asup_time", "commonResourceAttributes", "consoleUri", "ctrlr_side", "customerId", "fan_status", "fans", "generation", "hostname", "nvme_cards", "nvme_cards_enabled", "partial_response_ok", "partition_status", "power_status", "power_supplies", "resourceUri", "state", "support_address", "support_netmask", "support_nic", "temperature_sensors", "temperature_status", "type", "update_end_time", "update_error_code", "update_progress_msg", "update_start_time", "update_state", "version_current", "version_rollback", "version_target"]

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
        """Create an instance of NimbleControllerDetailsWithRequestUri from a JSON string"""
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
            _dict['associated_links'] = _items
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fans (list)
        _items = []
        if self.fans:
            for _item in self.fans:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fans'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in nvme_cards (list)
        _items = []
        if self.nvme_cards:
            for _item in self.nvme_cards:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nvme_cards'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in partition_status (list)
        _items = []
        if self.partition_status:
            for _item in self.partition_status:
                if _item:
                    _items.append(_item.to_dict())
            _dict['partition_status'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in power_supplies (list)
        _items = []
        if self.power_supplies:
            for _item in self.power_supplies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['power_supplies'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in temperature_sensors (list)
        _items = []
        if self.temperature_sensors:
            for _item in self.temperature_sensors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['temperature_sensors'] = _items
        # set to None if array_id (nullable) is None
        # and model_fields_set contains the field
        if self.array_id is None and "array_id" in self.model_fields_set:
            _dict['array_id'] = None

        # set to None if array_name (nullable) is None
        # and model_fields_set contains the field
        if self.array_name is None and "array_name" in self.model_fields_set:
            _dict['array_name'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if serial (nullable) is None
        # and model_fields_set contains the field
        if self.serial is None and "serial" in self.model_fields_set:
            _dict['serial'] = None

        # set to None if asup_time (nullable) is None
        # and model_fields_set contains the field
        if self.asup_time is None and "asup_time" in self.model_fields_set:
            _dict['asup_time'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if ctrlr_side (nullable) is None
        # and model_fields_set contains the field
        if self.ctrlr_side is None and "ctrlr_side" in self.model_fields_set:
            _dict['ctrlr_side'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if fan_status (nullable) is None
        # and model_fields_set contains the field
        if self.fan_status is None and "fan_status" in self.model_fields_set:
            _dict['fan_status'] = None

        # set to None if fans (nullable) is None
        # and model_fields_set contains the field
        if self.fans is None and "fans" in self.model_fields_set:
            _dict['fans'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if hostname (nullable) is None
        # and model_fields_set contains the field
        if self.hostname is None and "hostname" in self.model_fields_set:
            _dict['hostname'] = None

        # set to None if nvme_cards (nullable) is None
        # and model_fields_set contains the field
        if self.nvme_cards is None and "nvme_cards" in self.model_fields_set:
            _dict['nvme_cards'] = None

        # set to None if nvme_cards_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.nvme_cards_enabled is None and "nvme_cards_enabled" in self.model_fields_set:
            _dict['nvme_cards_enabled'] = None

        # set to None if partial_response_ok (nullable) is None
        # and model_fields_set contains the field
        if self.partial_response_ok is None and "partial_response_ok" in self.model_fields_set:
            _dict['partial_response_ok'] = None

        # set to None if partition_status (nullable) is None
        # and model_fields_set contains the field
        if self.partition_status is None and "partition_status" in self.model_fields_set:
            _dict['partition_status'] = None

        # set to None if power_status (nullable) is None
        # and model_fields_set contains the field
        if self.power_status is None and "power_status" in self.model_fields_set:
            _dict['power_status'] = None

        # set to None if power_supplies (nullable) is None
        # and model_fields_set contains the field
        if self.power_supplies is None and "power_supplies" in self.model_fields_set:
            _dict['power_supplies'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if support_address (nullable) is None
        # and model_fields_set contains the field
        if self.support_address is None and "support_address" in self.model_fields_set:
            _dict['support_address'] = None

        # set to None if support_netmask (nullable) is None
        # and model_fields_set contains the field
        if self.support_netmask is None and "support_netmask" in self.model_fields_set:
            _dict['support_netmask'] = None

        # set to None if support_nic (nullable) is None
        # and model_fields_set contains the field
        if self.support_nic is None and "support_nic" in self.model_fields_set:
            _dict['support_nic'] = None

        # set to None if temperature_sensors (nullable) is None
        # and model_fields_set contains the field
        if self.temperature_sensors is None and "temperature_sensors" in self.model_fields_set:
            _dict['temperature_sensors'] = None

        # set to None if temperature_status (nullable) is None
        # and model_fields_set contains the field
        if self.temperature_status is None and "temperature_status" in self.model_fields_set:
            _dict['temperature_status'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if update_end_time (nullable) is None
        # and model_fields_set contains the field
        if self.update_end_time is None and "update_end_time" in self.model_fields_set:
            _dict['update_end_time'] = None

        # set to None if update_error_code (nullable) is None
        # and model_fields_set contains the field
        if self.update_error_code is None and "update_error_code" in self.model_fields_set:
            _dict['update_error_code'] = None

        # set to None if update_progress_msg (nullable) is None
        # and model_fields_set contains the field
        if self.update_progress_msg is None and "update_progress_msg" in self.model_fields_set:
            _dict['update_progress_msg'] = None

        # set to None if update_start_time (nullable) is None
        # and model_fields_set contains the field
        if self.update_start_time is None and "update_start_time" in self.model_fields_set:
            _dict['update_start_time'] = None

        # set to None if update_state (nullable) is None
        # and model_fields_set contains the field
        if self.update_state is None and "update_state" in self.model_fields_set:
            _dict['update_state'] = None

        # set to None if version_current (nullable) is None
        # and model_fields_set contains the field
        if self.version_current is None and "version_current" in self.model_fields_set:
            _dict['version_current'] = None

        # set to None if version_rollback (nullable) is None
        # and model_fields_set contains the field
        if self.version_rollback is None and "version_rollback" in self.model_fields_set:
            _dict['version_rollback'] = None

        # set to None if version_target (nullable) is None
        # and model_fields_set contains the field
        if self.version_target is None and "version_target" in self.model_fields_set:
            _dict['version_target'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleControllerDetailsWithRequestUri from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "array_id": obj.get("array_id"),
            "array_name": obj.get("array_name"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "serial": obj.get("serial"),
            "associated_links": [AssociatedLinksInner.from_dict(_item) for _item in obj["associated_links"]] if obj.get("associated_links") is not None else None,
            "asup_time": obj.get("asup_time"),
            "commonResourceAttributes": NimbleCommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "consoleUri": obj.get("consoleUri"),
            "ctrlr_side": obj.get("ctrlr_side"),
            "customerId": obj.get("customerId"),
            "fan_status": obj.get("fan_status"),
            "fans": [NimbleNsCtrlrHwSensorInfo.from_dict(_item) for _item in obj["fans"]] if obj.get("fans") is not None else None,
            "generation": obj.get("generation"),
            "hostname": obj.get("hostname"),
            "nvme_cards": [NimbleNsCtrlrNvmeCard.from_dict(_item) for _item in obj["nvme_cards"]] if obj.get("nvme_cards") is not None else None,
            "nvme_cards_enabled": obj.get("nvme_cards_enabled"),
            "partial_response_ok": obj.get("partial_response_ok"),
            "partition_status": [NimbleNsCtrlrRaidInfo.from_dict(_item) for _item in obj["partition_status"]] if obj.get("partition_status") is not None else None,
            "power_status": obj.get("power_status"),
            "power_supplies": [NimbleNsCtrlrHwSensorInfo.from_dict(_item) for _item in obj["power_supplies"]] if obj.get("power_supplies") is not None else None,
            "resourceUri": obj.get("resourceUri"),
            "state": obj.get("state"),
            "support_address": obj.get("support_address"),
            "support_netmask": obj.get("support_netmask"),
            "support_nic": obj.get("support_nic"),
            "temperature_sensors": [NimbleNsCtrlrHwSensorInfo.from_dict(_item) for _item in obj["temperature_sensors"]] if obj.get("temperature_sensors") is not None else None,
            "temperature_status": obj.get("temperature_status"),
            "type": obj.get("type"),
            "update_end_time": obj.get("update_end_time"),
            "update_error_code": obj.get("update_error_code"),
            "update_progress_msg": obj.get("update_progress_msg"),
            "update_start_time": obj.get("update_start_time"),
            "update_state": obj.get("update_state"),
            "version_current": obj.get("version_current"),
            "version_rollback": obj.get("version_rollback"),
            "version_target": obj.get("version_target")
        })
        return _obj


