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
from dscc.models.associated_links_inner import AssociatedLinksInner
from dscc.models.common_resource_attributes import CommonResourceAttributes
from dscc.models.device_type4_address import DeviceType4Address
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4sysPortManagement(BaseModel):
    """
    Port Management details for a device
    """ # noqa: E501
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    authentication_required: Optional[StrictStr] = Field(default=None, description="Is authentication required. Allowed values are enabled or disabled", alias="authenticationRequired")
    common_resource_attributes: Optional[CommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="The customer application identifier", alias="customerId")
    default_route_ipv4: Optional[StrictStr] = Field(default=None, description="Default IPV4 route address of the network port", alias="defaultRouteIPv4")
    default_route_ipv6: Optional[StrictStr] = Field(default=None, description="Default IPV6 route address of the network port", alias="defaultRouteIPv6")
    displayname: Optional[StrictStr] = Field(default=None, description="Name to be used for display purposes")
    dns_server: Optional[StrictStr] = Field(default=None, description="DNS Server of the network port", alias="dnsServer")
    domain: Optional[StrictStr] = Field(default=None, description="Domain that the resource belongs to")
    generation: Optional[StrictInt] = Field(default=None, description="A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.")
    id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the resource")
    ip_v4_data: Optional[DeviceType4Address] = Field(default=None, alias="ipV4Data")
    ip_v6_data: Optional[DeviceType4Address] = Field(default=None, alias="ipV6Data")
    new_default_route_ipv4: Optional[StrictStr] = Field(default=None, description="New default IPV4 route address of the network port", alias="newDefaultRouteIPv4")
    new_default_route_ipv6: Optional[StrictStr] = Field(default=None, description="New default IPV6 route address of the network port", alias="newDefaultRouteIPv6")
    new_ip_v4_data: Optional[DeviceType4Address] = Field(default=None, alias="newIpV4Data")
    new_ipv6_data: Optional[DeviceType4Address] = Field(default=None, alias="newIpv6Data")
    ntp_server: Optional[StrictStr] = Field(default=None, description="NTP Server of the network port", alias="ntpServer")
    proxy_port: Optional[StrictInt] = Field(default=None, description="Proxy Server Port. Allowed values are 1-65535", alias="proxyPort")
    proxy_protocol: Optional[StrictStr] = Field(default=None, description="Supported proxy protocols are HTTP, SOCKS4 and SOCKS5.", alias="proxyProtocol")
    proxy_server: Optional[StrictStr] = Field(default=None, description="Proxy server IP address", alias="proxyServer")
    proxy_user: Optional[StrictStr] = Field(default=None, description="Username for authentication. (Required only if Authentication required is enabled)", alias="proxyUser")
    system_id: Optional[StrictStr] = Field(default=None, description="Serial Number of the array", alias="systemId")
    type: Optional[StrictStr] = Field(default=None, description="The type of resource.")
    __properties: ClassVar[List[str]] = ["associatedLinks", "authenticationRequired", "commonResourceAttributes", "consoleUri", "customerId", "defaultRouteIPv4", "defaultRouteIPv6", "displayname", "dnsServer", "domain", "generation", "id", "ipV4Data", "ipV6Data", "newDefaultRouteIPv4", "newDefaultRouteIPv6", "newIpV4Data", "newIpv6Data", "ntpServer", "proxyPort", "proxyProtocol", "proxyServer", "proxyUser", "systemId", "type"]

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
        """Create an instance of DeviceType4sysPortManagement from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ip_v4_data
        if self.ip_v4_data:
            _dict['ipV4Data'] = self.ip_v4_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ip_v6_data
        if self.ip_v6_data:
            _dict['ipV6Data'] = self.ip_v6_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of new_ip_v4_data
        if self.new_ip_v4_data:
            _dict['newIpV4Data'] = self.new_ip_v4_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of new_ipv6_data
        if self.new_ipv6_data:
            _dict['newIpv6Data'] = self.new_ipv6_data.to_dict()
        # set to None if associated_links (nullable) is None
        # and model_fields_set contains the field
        if self.associated_links is None and "associated_links" in self.model_fields_set:
            _dict['associatedLinks'] = None

        # set to None if authentication_required (nullable) is None
        # and model_fields_set contains the field
        if self.authentication_required is None and "authentication_required" in self.model_fields_set:
            _dict['authenticationRequired'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if default_route_ipv4 (nullable) is None
        # and model_fields_set contains the field
        if self.default_route_ipv4 is None and "default_route_ipv4" in self.model_fields_set:
            _dict['defaultRouteIPv4'] = None

        # set to None if default_route_ipv6 (nullable) is None
        # and model_fields_set contains the field
        if self.default_route_ipv6 is None and "default_route_ipv6" in self.model_fields_set:
            _dict['defaultRouteIPv6'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if dns_server (nullable) is None
        # and model_fields_set contains the field
        if self.dns_server is None and "dns_server" in self.model_fields_set:
            _dict['dnsServer'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if ip_v4_data (nullable) is None
        # and model_fields_set contains the field
        if self.ip_v4_data is None and "ip_v4_data" in self.model_fields_set:
            _dict['ipV4Data'] = None

        # set to None if ip_v6_data (nullable) is None
        # and model_fields_set contains the field
        if self.ip_v6_data is None and "ip_v6_data" in self.model_fields_set:
            _dict['ipV6Data'] = None

        # set to None if new_default_route_ipv4 (nullable) is None
        # and model_fields_set contains the field
        if self.new_default_route_ipv4 is None and "new_default_route_ipv4" in self.model_fields_set:
            _dict['newDefaultRouteIPv4'] = None

        # set to None if new_default_route_ipv6 (nullable) is None
        # and model_fields_set contains the field
        if self.new_default_route_ipv6 is None and "new_default_route_ipv6" in self.model_fields_set:
            _dict['newDefaultRouteIPv6'] = None

        # set to None if new_ip_v4_data (nullable) is None
        # and model_fields_set contains the field
        if self.new_ip_v4_data is None and "new_ip_v4_data" in self.model_fields_set:
            _dict['newIpV4Data'] = None

        # set to None if new_ipv6_data (nullable) is None
        # and model_fields_set contains the field
        if self.new_ipv6_data is None and "new_ipv6_data" in self.model_fields_set:
            _dict['newIpv6Data'] = None

        # set to None if ntp_server (nullable) is None
        # and model_fields_set contains the field
        if self.ntp_server is None and "ntp_server" in self.model_fields_set:
            _dict['ntpServer'] = None

        # set to None if proxy_port (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_port is None and "proxy_port" in self.model_fields_set:
            _dict['proxyPort'] = None

        # set to None if proxy_protocol (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_protocol is None and "proxy_protocol" in self.model_fields_set:
            _dict['proxyProtocol'] = None

        # set to None if proxy_server (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_server is None and "proxy_server" in self.model_fields_set:
            _dict['proxyServer'] = None

        # set to None if proxy_user (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_user is None and "proxy_user" in self.model_fields_set:
            _dict['proxyUser'] = None

        # set to None if system_id (nullable) is None
        # and model_fields_set contains the field
        if self.system_id is None and "system_id" in self.model_fields_set:
            _dict['systemId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4sysPortManagement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedLinks": [AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "authenticationRequired": obj.get("authenticationRequired"),
            "commonResourceAttributes": CommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "defaultRouteIPv4": obj.get("defaultRouteIPv4"),
            "defaultRouteIPv6": obj.get("defaultRouteIPv6"),
            "displayname": obj.get("displayname"),
            "dnsServer": obj.get("dnsServer"),
            "domain": obj.get("domain"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "ipV4Data": DeviceType4Address.from_dict(obj["ipV4Data"]) if obj.get("ipV4Data") is not None else None,
            "ipV6Data": DeviceType4Address.from_dict(obj["ipV6Data"]) if obj.get("ipV6Data") is not None else None,
            "newDefaultRouteIPv4": obj.get("newDefaultRouteIPv4"),
            "newDefaultRouteIPv6": obj.get("newDefaultRouteIPv6"),
            "newIpV4Data": DeviceType4Address.from_dict(obj["newIpV4Data"]) if obj.get("newIpV4Data") is not None else None,
            "newIpv6Data": DeviceType4Address.from_dict(obj["newIpv6Data"]) if obj.get("newIpv6Data") is not None else None,
            "ntpServer": obj.get("ntpServer"),
            "proxyPort": obj.get("proxyPort"),
            "proxyProtocol": obj.get("proxyProtocol"),
            "proxyServer": obj.get("proxyServer"),
            "proxyUser": obj.get("proxyUser"),
            "systemId": obj.get("systemId"),
            "type": obj.get("type")
        })
        return _obj


