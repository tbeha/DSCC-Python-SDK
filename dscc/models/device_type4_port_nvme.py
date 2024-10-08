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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dscc.models.device_type4_nvme_vlan import DeviceType4NVMeVLAN
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4PortNVMe(BaseModel):
    """
    DeviceType4PortNVMe
    """ # noqa: E501
    delimited_mac_address: Optional[StrictStr] = Field(default=None, description="MAC address of the NVMe port", alias="delimitedMacAddress")
    eth: Optional[StrictStr] = Field(default=None, description="Ethernet name used by the NVMe port")
    gateway_address: Optional[StrictStr] = Field(default=None, description="Gateway of the NVMe port", alias="gatewayAddress")
    gateway_address_v6: Optional[StrictStr] = Field(default=None, description="Gateway address for the NVMe port.", alias="gatewayAddressV6")
    ip_address: Optional[StrictStr] = Field(default=None, description="IP address of the NVMe port", alias="ipAddress")
    ip_address_v6: Optional[StrictStr] = Field(default=None, description="IPV6 address for the NVMe port.", alias="ipAddressV6")
    mac_address: Optional[StrictStr] = Field(default=None, description="MAC address of the NVMe port", alias="macAddress")
    mode: Optional[StrictStr] = Field(default=None, description="Current mode the port is in")
    mtu: Optional[StrictStr] = Field(default=None, description="Maximum transmission unit (MTU) size")
    nqn: Optional[StrictStr] = Field(default=None, description="NVMe qualified name of the NVMe port")
    pcidev: Optional[StrictStr] = Field(default=None, description="PCI device used by the NVMe port")
    prefix_length: Optional[StrictInt] = Field(default=None, description="Prefix Length of the NVMe port", alias="prefixLength")
    prefix_length_v6: Optional[StrictInt] = Field(default=None, description="Prefix length of the NVMe port.", alias="prefixLengthV6")
    protocol: Optional[StrictStr] = Field(default=None, description="Current protocol the port is in")
    rate: Optional[StrictStr] = Field(default=None, description="Configured speed of the NVMe port")
    state: Optional[StrictStr] = Field(default=None, description="State of the resource")
    vlan_count: Optional[StrictInt] = Field(default=None, description="Number of configured VLANs on this NVMe port", alias="vlanCount")
    vlans: Optional[List[DeviceType4NVMeVLAN]] = None
    __properties: ClassVar[List[str]] = ["delimitedMacAddress", "eth", "gatewayAddress", "gatewayAddressV6", "ipAddress", "ipAddressV6", "macAddress", "mode", "mtu", "nqn", "pcidev", "prefixLength", "prefixLengthV6", "protocol", "rate", "state", "vlanCount", "vlans"]

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
        """Create an instance of DeviceType4PortNVMe from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in vlans (list)
        _items = []
        if self.vlans:
            for _item in self.vlans:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vlans'] = _items
        # set to None if delimited_mac_address (nullable) is None
        # and model_fields_set contains the field
        if self.delimited_mac_address is None and "delimited_mac_address" in self.model_fields_set:
            _dict['delimitedMacAddress'] = None

        # set to None if eth (nullable) is None
        # and model_fields_set contains the field
        if self.eth is None and "eth" in self.model_fields_set:
            _dict['eth'] = None

        # set to None if gateway_address (nullable) is None
        # and model_fields_set contains the field
        if self.gateway_address is None and "gateway_address" in self.model_fields_set:
            _dict['gatewayAddress'] = None

        # set to None if gateway_address_v6 (nullable) is None
        # and model_fields_set contains the field
        if self.gateway_address_v6 is None and "gateway_address_v6" in self.model_fields_set:
            _dict['gatewayAddressV6'] = None

        # set to None if ip_address (nullable) is None
        # and model_fields_set contains the field
        if self.ip_address is None and "ip_address" in self.model_fields_set:
            _dict['ipAddress'] = None

        # set to None if ip_address_v6 (nullable) is None
        # and model_fields_set contains the field
        if self.ip_address_v6 is None and "ip_address_v6" in self.model_fields_set:
            _dict['ipAddressV6'] = None

        # set to None if mac_address (nullable) is None
        # and model_fields_set contains the field
        if self.mac_address is None and "mac_address" in self.model_fields_set:
            _dict['macAddress'] = None

        # set to None if mtu (nullable) is None
        # and model_fields_set contains the field
        if self.mtu is None and "mtu" in self.model_fields_set:
            _dict['mtu'] = None

        # set to None if nqn (nullable) is None
        # and model_fields_set contains the field
        if self.nqn is None and "nqn" in self.model_fields_set:
            _dict['nqn'] = None

        # set to None if pcidev (nullable) is None
        # and model_fields_set contains the field
        if self.pcidev is None and "pcidev" in self.model_fields_set:
            _dict['pcidev'] = None

        # set to None if prefix_length (nullable) is None
        # and model_fields_set contains the field
        if self.prefix_length is None and "prefix_length" in self.model_fields_set:
            _dict['prefixLength'] = None

        # set to None if prefix_length_v6 (nullable) is None
        # and model_fields_set contains the field
        if self.prefix_length_v6 is None and "prefix_length_v6" in self.model_fields_set:
            _dict['prefixLengthV6'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if vlan_count (nullable) is None
        # and model_fields_set contains the field
        if self.vlan_count is None and "vlan_count" in self.model_fields_set:
            _dict['vlanCount'] = None

        # set to None if vlans (nullable) is None
        # and model_fields_set contains the field
        if self.vlans is None and "vlans" in self.model_fields_set:
            _dict['vlans'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4PortNVMe from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "delimitedMacAddress": obj.get("delimitedMacAddress"),
            "eth": obj.get("eth"),
            "gatewayAddress": obj.get("gatewayAddress"),
            "gatewayAddressV6": obj.get("gatewayAddressV6"),
            "ipAddress": obj.get("ipAddress"),
            "ipAddressV6": obj.get("ipAddressV6"),
            "macAddress": obj.get("macAddress"),
            "mode": obj.get("mode"),
            "mtu": obj.get("mtu"),
            "nqn": obj.get("nqn"),
            "pcidev": obj.get("pcidev"),
            "prefixLength": obj.get("prefixLength"),
            "prefixLengthV6": obj.get("prefixLengthV6"),
            "protocol": obj.get("protocol"),
            "rate": obj.get("rate"),
            "state": obj.get("state"),
            "vlanCount": obj.get("vlanCount"),
            "vlans": [DeviceType4NVMeVLAN.from_dict(_item) for _item in obj["vlans"]] if obj.get("vlans") is not None else None
        })
        return _obj


