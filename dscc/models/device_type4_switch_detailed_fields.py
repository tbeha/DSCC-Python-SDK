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
from dscc.models.common_resource_attributes import CommonResourceAttributes
from dscc.models.device_type4_state import DeviceType4State
from dscc.models.device_type4_switch_detailed_fields_switch_fans import DeviceType4SwitchDetailedFieldsSwitchFans
from dscc.models.device_type4_switch_detailed_fields_switch_port import DeviceType4SwitchDetailedFieldsSwitchPort
from dscc.models.device_type4_switch_detailed_fields_switch_power_supplies import DeviceType4SwitchDetailedFieldsSwitchPowerSupplies
from dscc.models.device_type4manufacturing import DeviceType4manufacturing
from dscc.models.switch_device_dhcp_server_inner import SwitchDeviceDHCPServerInner
from dscc.models.switch_device_vlan_inner import SwitchDeviceVlanInner
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4SwitchDetailedFields(BaseModel):
    """
    DeviceType4SwitchDetailedFields
    """ # noqa: E501
    active_ip_address: Optional[StrictStr] = Field(default=None, description="Switch active IP Address", alias="activeIPAddress")
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    common_resource_attributes: Optional[CommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    dhcp_servers: Optional[List[Optional[SwitchDeviceDHCPServerInner]]] = Field(default=None, alias="dhcpServers")
    displayname: Optional[StrictStr] = Field(default=None, description="Name to be used for display purposes")
    domain: Optional[StrictStr] = Field(default=None, description="Domain that the resource belongs to")
    fan_state: Optional[DeviceType4State] = Field(default=None, alias="fanState")
    fw_version: Optional[StrictStr] = Field(default=None, description="Switch firmware version", alias="fwVersion")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the resource.")
    locate_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if the locate beacon is enabled or not", alias="locateEnabled")
    mac_address: Optional[StrictStr] = Field(default=None, description="MAC address of the switch", alias="macAddress")
    manufacturing: Optional[DeviceType4manufacturing] = None
    mode: Optional[StrictStr] = Field(default=None, description="Switch mode")
    name: Optional[StrictStr] = Field(default=None, description="Name of the resource.")
    primary_path: Optional[StrictStr] = Field(default=None, description="Switch primary path state", alias="primaryPath")
    ps1_state: Optional[DeviceType4State] = Field(default=None, alias="ps1State")
    ps2_state: Optional[DeviceType4State] = Field(default=None, alias="ps2State")
    request_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed enclosure object", alias="requestUri")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed enclosure object", alias="resourceUri")
    secondary_path: Optional[StrictStr] = Field(default=None, description="Switch secondary path state", alias="secondaryPath")
    state: Optional[DeviceType4State] = None
    switch_fans: Optional[DeviceType4SwitchDetailedFieldsSwitchFans] = Field(default=None, alias="switchFans")
    switch_id: Optional[StrictInt] = Field(default=None, description="ID of the resource", alias="switchId")
    switch_port: Optional[DeviceType4SwitchDetailedFieldsSwitchPort] = Field(default=None, alias="switchPort")
    switch_power_supplies: Optional[DeviceType4SwitchDetailedFieldsSwitchPowerSupplies] = Field(default=None, alias="switchPowerSupplies")
    system_id: Optional[StrictStr] = Field(default=None, description="SystemUid/Serial Number  of the array.", alias="systemId")
    temperature_detail: Optional[StrictStr] = Field(default=None, description="Switch mode", alias="temperatureDetail")
    temperature_state: Optional[DeviceType4State] = Field(default=None, alias="temperatureState")
    type: Optional[StrictStr] = Field(default=None, description="type")
    vlans: Optional[List[Optional[SwitchDeviceVlanInner]]] = None
    __properties: ClassVar[List[str]] = ["activeIPAddress", "associatedLinks", "commonResourceAttributes", "consoleUri", "customerId", "dhcpServers", "displayname", "domain", "fanState", "fwVersion", "generation", "id", "locateEnabled", "macAddress", "manufacturing", "mode", "name", "primaryPath", "ps1State", "ps2State", "requestUri", "resourceUri", "secondaryPath", "state", "switchFans", "switchId", "switchPort", "switchPowerSupplies", "systemId", "temperatureDetail", "temperatureState", "type", "vlans"]

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
        """Create an instance of DeviceType4SwitchDetailedFields from a JSON string"""
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
            _dict['associatedLinks'] = _items
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in dhcp_servers (list)
        _items = []
        if self.dhcp_servers:
            for _item in self.dhcp_servers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dhcpServers'] = _items
        # override the default output from pydantic by calling `to_dict()` of fan_state
        if self.fan_state:
            _dict['fanState'] = self.fan_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manufacturing
        if self.manufacturing:
            _dict['manufacturing'] = self.manufacturing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ps1_state
        if self.ps1_state:
            _dict['ps1State'] = self.ps1_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ps2_state
        if self.ps2_state:
            _dict['ps2State'] = self.ps2_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of switch_fans
        if self.switch_fans:
            _dict['switchFans'] = self.switch_fans.to_dict()
        # override the default output from pydantic by calling `to_dict()` of switch_port
        if self.switch_port:
            _dict['switchPort'] = self.switch_port.to_dict()
        # override the default output from pydantic by calling `to_dict()` of switch_power_supplies
        if self.switch_power_supplies:
            _dict['switchPowerSupplies'] = self.switch_power_supplies.to_dict()
        # override the default output from pydantic by calling `to_dict()` of temperature_state
        if self.temperature_state:
            _dict['temperatureState'] = self.temperature_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in vlans (list)
        _items = []
        if self.vlans:
            for _item in self.vlans:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vlans'] = _items
        # set to None if active_ip_address (nullable) is None
        # and model_fields_set contains the field
        if self.active_ip_address is None and "active_ip_address" in self.model_fields_set:
            _dict['activeIPAddress'] = None

        # set to None if associated_links (nullable) is None
        # and model_fields_set contains the field
        if self.associated_links is None and "associated_links" in self.model_fields_set:
            _dict['associatedLinks'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if dhcp_servers (nullable) is None
        # and model_fields_set contains the field
        if self.dhcp_servers is None and "dhcp_servers" in self.model_fields_set:
            _dict['dhcpServers'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if fan_state (nullable) is None
        # and model_fields_set contains the field
        if self.fan_state is None and "fan_state" in self.model_fields_set:
            _dict['fanState'] = None

        # set to None if fw_version (nullable) is None
        # and model_fields_set contains the field
        if self.fw_version is None and "fw_version" in self.model_fields_set:
            _dict['fwVersion'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if locate_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.locate_enabled is None and "locate_enabled" in self.model_fields_set:
            _dict['locateEnabled'] = None

        # set to None if mac_address (nullable) is None
        # and model_fields_set contains the field
        if self.mac_address is None and "mac_address" in self.model_fields_set:
            _dict['macAddress'] = None

        # set to None if manufacturing (nullable) is None
        # and model_fields_set contains the field
        if self.manufacturing is None and "manufacturing" in self.model_fields_set:
            _dict['manufacturing'] = None

        # set to None if mode (nullable) is None
        # and model_fields_set contains the field
        if self.mode is None and "mode" in self.model_fields_set:
            _dict['mode'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if primary_path (nullable) is None
        # and model_fields_set contains the field
        if self.primary_path is None and "primary_path" in self.model_fields_set:
            _dict['primaryPath'] = None

        # set to None if ps1_state (nullable) is None
        # and model_fields_set contains the field
        if self.ps1_state is None and "ps1_state" in self.model_fields_set:
            _dict['ps1State'] = None

        # set to None if ps2_state (nullable) is None
        # and model_fields_set contains the field
        if self.ps2_state is None and "ps2_state" in self.model_fields_set:
            _dict['ps2State'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestUri'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if secondary_path (nullable) is None
        # and model_fields_set contains the field
        if self.secondary_path is None and "secondary_path" in self.model_fields_set:
            _dict['secondaryPath'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if switch_fans (nullable) is None
        # and model_fields_set contains the field
        if self.switch_fans is None and "switch_fans" in self.model_fields_set:
            _dict['switchFans'] = None

        # set to None if switch_id (nullable) is None
        # and model_fields_set contains the field
        if self.switch_id is None and "switch_id" in self.model_fields_set:
            _dict['switchId'] = None

        # set to None if switch_port (nullable) is None
        # and model_fields_set contains the field
        if self.switch_port is None and "switch_port" in self.model_fields_set:
            _dict['switchPort'] = None

        # set to None if switch_power_supplies (nullable) is None
        # and model_fields_set contains the field
        if self.switch_power_supplies is None and "switch_power_supplies" in self.model_fields_set:
            _dict['switchPowerSupplies'] = None

        # set to None if system_id (nullable) is None
        # and model_fields_set contains the field
        if self.system_id is None and "system_id" in self.model_fields_set:
            _dict['systemId'] = None

        # set to None if temperature_detail (nullable) is None
        # and model_fields_set contains the field
        if self.temperature_detail is None and "temperature_detail" in self.model_fields_set:
            _dict['temperatureDetail'] = None

        # set to None if temperature_state (nullable) is None
        # and model_fields_set contains the field
        if self.temperature_state is None and "temperature_state" in self.model_fields_set:
            _dict['temperatureState'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if vlans (nullable) is None
        # and model_fields_set contains the field
        if self.vlans is None and "vlans" in self.model_fields_set:
            _dict['vlans'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4SwitchDetailedFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activeIPAddress": obj.get("activeIPAddress"),
            "associatedLinks": [AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "commonResourceAttributes": CommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "dhcpServers": [SwitchDeviceDHCPServerInner.from_dict(_item) for _item in obj["dhcpServers"]] if obj.get("dhcpServers") is not None else None,
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "fanState": DeviceType4State.from_dict(obj["fanState"]) if obj.get("fanState") is not None else None,
            "fwVersion": obj.get("fwVersion"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "locateEnabled": obj.get("locateEnabled"),
            "macAddress": obj.get("macAddress"),
            "manufacturing": DeviceType4manufacturing.from_dict(obj["manufacturing"]) if obj.get("manufacturing") is not None else None,
            "mode": obj.get("mode"),
            "name": obj.get("name"),
            "primaryPath": obj.get("primaryPath"),
            "ps1State": DeviceType4State.from_dict(obj["ps1State"]) if obj.get("ps1State") is not None else None,
            "ps2State": DeviceType4State.from_dict(obj["ps2State"]) if obj.get("ps2State") is not None else None,
            "requestUri": obj.get("requestUri"),
            "resourceUri": obj.get("resourceUri"),
            "secondaryPath": obj.get("secondaryPath"),
            "state": DeviceType4State.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "switchFans": DeviceType4SwitchDetailedFieldsSwitchFans.from_dict(obj["switchFans"]) if obj.get("switchFans") is not None else None,
            "switchId": obj.get("switchId"),
            "switchPort": DeviceType4SwitchDetailedFieldsSwitchPort.from_dict(obj["switchPort"]) if obj.get("switchPort") is not None else None,
            "switchPowerSupplies": DeviceType4SwitchDetailedFieldsSwitchPowerSupplies.from_dict(obj["switchPowerSupplies"]) if obj.get("switchPowerSupplies") is not None else None,
            "systemId": obj.get("systemId"),
            "temperatureDetail": obj.get("temperatureDetail"),
            "temperatureState": DeviceType4State.from_dict(obj["temperatureState"]) if obj.get("temperatureState") is not None else None,
            "type": obj.get("type"),
            "vlans": [SwitchDeviceVlanInner.from_dict(_item) for _item in obj["vlans"]] if obj.get("vlans") is not None else None
        })
        return _obj


