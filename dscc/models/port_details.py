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
from dscc.models.card_type import CardType
from dscc.models.device_type4connected_devices_inner import DeviceType4connectedDevicesInner
from dscc.models.initiator_port import InitiatorPort
from dscc.models.manufacturing_single import ManufacturingSingle
from dscc.models.partner_port import PartnerPort
from dscc.models.port_fc import PortFC
from dscc.models.port_ip import PortIP
from dscc.models.port_iscsi import PortISCSI
from dscc.models.port_position import PortPosition
from dscc.models.port_sfp import PortSfp
from dscc.models.primera_common_resource_attributes import PrimeraCommonResourceAttributes
from dscc.models.state import State
from dscc.models.vlan import Vlan
from typing import Optional, Set
from typing_extensions import Self

class PortDetails(BaseModel):
    """
    PortDetails
    """ # noqa: E501
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    card_type: Optional[CardType] = Field(default=None, alias="cardType")
    var_class: Optional[StrictInt] = Field(default=None, description="Fibre Channel class (can be either 2 or 3)", alias="class")
    class2: Optional[StrictStr] = Field(default=None, description="Class2 state and configuration")
    common_resource_attributes: Optional[PrimeraCommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    config: Optional[StrictStr] = Field(default=None, description="Configuration state of port")
    config_mode: Optional[StrictStr] = Field(default=None, description="Connection mode of the port", alias="configMode")
    connection_type: Optional[StrictStr] = Field(default=None, description="port connection type", alias="connectionType")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    devices: Optional[List[Optional[DeviceType4connectedDevicesInner]]] = None
    displayname: Optional[StrictStr] = Field(default=None, description="Name to be used for display purposes")
    domain: Optional[StrictStr] = Field(default=None, description="Domain that the resource belongs to")
    failover_status: Optional[StrictStr] = Field(default=None, description="Failover status of this port and the partner", alias="failoverStatus")
    fc_data: Optional[PortFC] = Field(default=None, alias="fcData")
    fw_version: Optional[StrictStr] = Field(default=None, description="Firmware version", alias="fwVersion")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the resource")
    initiator_ports: Optional[InitiatorPort] = Field(default=None, alias="initiatorPorts")
    interrupt_coalesce: Optional[StrictStr] = Field(default=None, description="Interrupt Coalesce", alias="interruptCoalesce")
    ip_data: Optional[PortIP] = Field(default=None, alias="ipData")
    iscsi_data: Optional[PortISCSI] = Field(default=None, alias="iscsiData")
    label: Optional[StrictStr] = Field(default=None, description="Label")
    manufacturing: Optional[ManufacturingSingle] = None
    mode: Optional[StrictStr] = Field(default=None, description="Current mode the port is in")
    mode_change: Optional[StrictStr] = Field(default=None, description="Indicates if the mode change is allowed or prohibited", alias="modeChange")
    name: Optional[StrictStr] = Field(default=None, description="Name of the resource")
    node_card_id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the node adapter card", alias="nodeCardId")
    node_id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the node", alias="nodeId")
    partner: Optional[PartnerPort] = None
    port_sfp: Optional[PortSfp] = Field(default=None, alias="portSfp")
    port_type: Optional[StrictStr] = Field(default=None, description="Type of the port based on the device it is connected to", alias="portType")
    position: Optional[PortPosition] = None
    protocol: Optional[StrictStr] = Field(default=None, description="Current protocol the port is in")
    request_uri: Optional[StrictStr] = Field(default=None, description="requestUri for detailed ports object", alias="requestUri")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed ports object", alias="resourceUri")
    revision: Optional[StrictStr] = Field(default=None, description="Revision of the Host Bus Adapter")
    smart_san: Optional[StrictStr] = Field(default=None, description="Smart SAN status", alias="smartSAN")
    speed_actual: Optional[StrictStr] = Field(default=None, description="Actual speed that port is running at", alias="speedActual")
    speed_configured: Optional[StrictStr] = Field(default=None, description="Speed that is configured to run as", alias="speedConfigured")
    speed_max: Optional[StrictStr] = Field(default=None, description="Maximum speed that port can run at", alias="speedMax")
    speed_min: Optional[StrictStr] = Field(default=None, description="Minimum speed that port can run at", alias="speedMin")
    state: Optional[State] = None
    state_description: Optional[List[Optional[StrictStr]]] = Field(default=None, description="Detailed descriptions of the port state", alias="stateDescription")
    system_id: Optional[StrictStr] = Field(default=None, description="SystemUid / SerialNumber of the array", alias="systemId")
    tgt_mode_write_opt: Optional[StrictStr] = Field(default=None, description="Target mode write optimization setting", alias="tgtModeWriteOpt")
    type: Optional[StrictStr] = Field(default=None, description="type")
    unique_wwn: Optional[StrictStr] = Field(default=None, description="Unique WWN setting", alias="uniqueWWN")
    vlans: Optional[List[Optional[Vlan]]] = None
    __properties: ClassVar[List[str]] = ["associatedLinks", "cardType", "class", "class2", "commonResourceAttributes", "config", "configMode", "connectionType", "consoleUri", "customerId", "devices", "displayname", "domain", "failoverStatus", "fcData", "fwVersion", "generation", "id", "initiatorPorts", "interruptCoalesce", "ipData", "iscsiData", "label", "manufacturing", "mode", "modeChange", "name", "nodeCardId", "nodeId", "partner", "portSfp", "portType", "position", "protocol", "requestUri", "resourceUri", "revision", "smartSAN", "speedActual", "speedConfigured", "speedMax", "speedMin", "state", "stateDescription", "systemId", "tgtModeWriteOpt", "type", "uniqueWWN", "vlans"]

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
        """Create an instance of PortDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of card_type
        if self.card_type:
            _dict['cardType'] = self.card_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in devices (list)
        _items = []
        if self.devices:
            for _item in self.devices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['devices'] = _items
        # override the default output from pydantic by calling `to_dict()` of fc_data
        if self.fc_data:
            _dict['fcData'] = self.fc_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of initiator_ports
        if self.initiator_ports:
            _dict['initiatorPorts'] = self.initiator_ports.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ip_data
        if self.ip_data:
            _dict['ipData'] = self.ip_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of iscsi_data
        if self.iscsi_data:
            _dict['iscsiData'] = self.iscsi_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manufacturing
        if self.manufacturing:
            _dict['manufacturing'] = self.manufacturing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of partner
        if self.partner:
            _dict['partner'] = self.partner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of port_sfp
        if self.port_sfp:
            _dict['portSfp'] = self.port_sfp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of position
        if self.position:
            _dict['position'] = self.position.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in vlans (list)
        _items = []
        if self.vlans:
            for _item in self.vlans:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vlans'] = _items
        # set to None if card_type (nullable) is None
        # and model_fields_set contains the field
        if self.card_type is None and "card_type" in self.model_fields_set:
            _dict['cardType'] = None

        # set to None if var_class (nullable) is None
        # and model_fields_set contains the field
        if self.var_class is None and "var_class" in self.model_fields_set:
            _dict['class'] = None

        # set to None if class2 (nullable) is None
        # and model_fields_set contains the field
        if self.class2 is None and "class2" in self.model_fields_set:
            _dict['class2'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if config (nullable) is None
        # and model_fields_set contains the field
        if self.config is None and "config" in self.model_fields_set:
            _dict['config'] = None

        # set to None if config_mode (nullable) is None
        # and model_fields_set contains the field
        if self.config_mode is None and "config_mode" in self.model_fields_set:
            _dict['configMode'] = None

        # set to None if connection_type (nullable) is None
        # and model_fields_set contains the field
        if self.connection_type is None and "connection_type" in self.model_fields_set:
            _dict['connectionType'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if devices (nullable) is None
        # and model_fields_set contains the field
        if self.devices is None and "devices" in self.model_fields_set:
            _dict['devices'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if failover_status (nullable) is None
        # and model_fields_set contains the field
        if self.failover_status is None and "failover_status" in self.model_fields_set:
            _dict['failoverStatus'] = None

        # set to None if fc_data (nullable) is None
        # and model_fields_set contains the field
        if self.fc_data is None and "fc_data" in self.model_fields_set:
            _dict['fcData'] = None

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

        # set to None if initiator_ports (nullable) is None
        # and model_fields_set contains the field
        if self.initiator_ports is None and "initiator_ports" in self.model_fields_set:
            _dict['initiatorPorts'] = None

        # set to None if interrupt_coalesce (nullable) is None
        # and model_fields_set contains the field
        if self.interrupt_coalesce is None and "interrupt_coalesce" in self.model_fields_set:
            _dict['interruptCoalesce'] = None

        # set to None if ip_data (nullable) is None
        # and model_fields_set contains the field
        if self.ip_data is None and "ip_data" in self.model_fields_set:
            _dict['ipData'] = None

        # set to None if iscsi_data (nullable) is None
        # and model_fields_set contains the field
        if self.iscsi_data is None and "iscsi_data" in self.model_fields_set:
            _dict['iscsiData'] = None

        # set to None if label (nullable) is None
        # and model_fields_set contains the field
        if self.label is None and "label" in self.model_fields_set:
            _dict['label'] = None

        # set to None if manufacturing (nullable) is None
        # and model_fields_set contains the field
        if self.manufacturing is None and "manufacturing" in self.model_fields_set:
            _dict['manufacturing'] = None

        # set to None if mode (nullable) is None
        # and model_fields_set contains the field
        if self.mode is None and "mode" in self.model_fields_set:
            _dict['mode'] = None

        # set to None if mode_change (nullable) is None
        # and model_fields_set contains the field
        if self.mode_change is None and "mode_change" in self.model_fields_set:
            _dict['modeChange'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if node_card_id (nullable) is None
        # and model_fields_set contains the field
        if self.node_card_id is None and "node_card_id" in self.model_fields_set:
            _dict['nodeCardId'] = None

        # set to None if node_id (nullable) is None
        # and model_fields_set contains the field
        if self.node_id is None and "node_id" in self.model_fields_set:
            _dict['nodeId'] = None

        # set to None if partner (nullable) is None
        # and model_fields_set contains the field
        if self.partner is None and "partner" in self.model_fields_set:
            _dict['partner'] = None

        # set to None if port_sfp (nullable) is None
        # and model_fields_set contains the field
        if self.port_sfp is None and "port_sfp" in self.model_fields_set:
            _dict['portSfp'] = None

        # set to None if port_type (nullable) is None
        # and model_fields_set contains the field
        if self.port_type is None and "port_type" in self.model_fields_set:
            _dict['portType'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if protocol (nullable) is None
        # and model_fields_set contains the field
        if self.protocol is None and "protocol" in self.model_fields_set:
            _dict['protocol'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestUri'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if revision (nullable) is None
        # and model_fields_set contains the field
        if self.revision is None and "revision" in self.model_fields_set:
            _dict['revision'] = None

        # set to None if smart_san (nullable) is None
        # and model_fields_set contains the field
        if self.smart_san is None and "smart_san" in self.model_fields_set:
            _dict['smartSAN'] = None

        # set to None if speed_actual (nullable) is None
        # and model_fields_set contains the field
        if self.speed_actual is None and "speed_actual" in self.model_fields_set:
            _dict['speedActual'] = None

        # set to None if speed_configured (nullable) is None
        # and model_fields_set contains the field
        if self.speed_configured is None and "speed_configured" in self.model_fields_set:
            _dict['speedConfigured'] = None

        # set to None if speed_max (nullable) is None
        # and model_fields_set contains the field
        if self.speed_max is None and "speed_max" in self.model_fields_set:
            _dict['speedMax'] = None

        # set to None if speed_min (nullable) is None
        # and model_fields_set contains the field
        if self.speed_min is None and "speed_min" in self.model_fields_set:
            _dict['speedMin'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if state_description (nullable) is None
        # and model_fields_set contains the field
        if self.state_description is None and "state_description" in self.model_fields_set:
            _dict['stateDescription'] = None

        # set to None if system_id (nullable) is None
        # and model_fields_set contains the field
        if self.system_id is None and "system_id" in self.model_fields_set:
            _dict['systemId'] = None

        # set to None if tgt_mode_write_opt (nullable) is None
        # and model_fields_set contains the field
        if self.tgt_mode_write_opt is None and "tgt_mode_write_opt" in self.model_fields_set:
            _dict['tgtModeWriteOpt'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if unique_wwn (nullable) is None
        # and model_fields_set contains the field
        if self.unique_wwn is None and "unique_wwn" in self.model_fields_set:
            _dict['uniqueWWN'] = None

        # set to None if vlans (nullable) is None
        # and model_fields_set contains the field
        if self.vlans is None and "vlans" in self.model_fields_set:
            _dict['vlans'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PortDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedLinks": [AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "cardType": CardType.from_dict(obj["cardType"]) if obj.get("cardType") is not None else None,
            "class": obj.get("class"),
            "class2": obj.get("class2"),
            "commonResourceAttributes": PrimeraCommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "config": obj.get("config"),
            "configMode": obj.get("configMode"),
            "connectionType": obj.get("connectionType"),
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "devices": [DeviceType4connectedDevicesInner.from_dict(_item) for _item in obj["devices"]] if obj.get("devices") is not None else None,
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "failoverStatus": obj.get("failoverStatus"),
            "fcData": PortFC.from_dict(obj["fcData"]) if obj.get("fcData") is not None else None,
            "fwVersion": obj.get("fwVersion"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "initiatorPorts": InitiatorPort.from_dict(obj["initiatorPorts"]) if obj.get("initiatorPorts") is not None else None,
            "interruptCoalesce": obj.get("interruptCoalesce"),
            "ipData": PortIP.from_dict(obj["ipData"]) if obj.get("ipData") is not None else None,
            "iscsiData": PortISCSI.from_dict(obj["iscsiData"]) if obj.get("iscsiData") is not None else None,
            "label": obj.get("label"),
            "manufacturing": ManufacturingSingle.from_dict(obj["manufacturing"]) if obj.get("manufacturing") is not None else None,
            "mode": obj.get("mode"),
            "modeChange": obj.get("modeChange"),
            "name": obj.get("name"),
            "nodeCardId": obj.get("nodeCardId"),
            "nodeId": obj.get("nodeId"),
            "partner": PartnerPort.from_dict(obj["partner"]) if obj.get("partner") is not None else None,
            "portSfp": PortSfp.from_dict(obj["portSfp"]) if obj.get("portSfp") is not None else None,
            "portType": obj.get("portType"),
            "position": PortPosition.from_dict(obj["position"]) if obj.get("position") is not None else None,
            "protocol": obj.get("protocol"),
            "requestUri": obj.get("requestUri"),
            "resourceUri": obj.get("resourceUri"),
            "revision": obj.get("revision"),
            "smartSAN": obj.get("smartSAN"),
            "speedActual": obj.get("speedActual"),
            "speedConfigured": obj.get("speedConfigured"),
            "speedMax": obj.get("speedMax"),
            "speedMin": obj.get("speedMin"),
            "state": State.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "stateDescription": obj.get("stateDescription"),
            "systemId": obj.get("systemId"),
            "tgtModeWriteOpt": obj.get("tgtModeWriteOpt"),
            "type": obj.get("type"),
            "uniqueWWN": obj.get("uniqueWWN"),
            "vlans": [Vlan.from_dict(_item) for _item in obj["vlans"]] if obj.get("vlans") is not None else None
        })
        return _obj


