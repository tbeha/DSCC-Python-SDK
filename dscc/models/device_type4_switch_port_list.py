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
from dscc.models.device_type4_state import DeviceType4State
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4SwitchPortList(BaseModel):
    """
    DeviceType4SwitchPortList
    """ # noqa: E501
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    common_resource_attributes: Optional[CommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    device: Optional[StrictStr] = Field(default=None, description="Device (either node or IOM) to which the switch port is connected to")
    device_port: Optional[StrictStr] = Field(default=None, description="Port on device that the switch port is connected to", alias="devicePort")
    displayname: Optional[StrictStr] = Field(default=None, description="Name to be used for display purposes")
    domain: Optional[StrictStr] = Field(default=None, description="Domain that the resource belongs to")
    enclosure: Optional[StrictStr] = Field(default=None, description="Enclosure (cage) to which the switch port is connected to")
    generation: Optional[StrictInt] = Field(default=None, description="generation `Filter, Sort`")
    id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the resource. `Filter`")
    ip_address: Optional[StrictStr] = Field(default=None, description="Switch port IP Address", alias="ipAddress")
    mac_address: Optional[StrictStr] = Field(default=None, description="MAC address of the switch port", alias="macAddress")
    port_description: Optional[StrictStr] = Field(default=None, description="Switch port description", alias="portDescription")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed switch port object", alias="resourceUri")
    state: Optional[DeviceType4State] = None
    switch_name: Optional[StrictStr] = Field(default=None, description="Switch name.", alias="switchName")
    switch_port_id: Optional[StrictInt] = Field(default=None, description="ID of the resource", alias="switchPortId")
    switch_uid: Optional[StrictStr] = Field(default=None, description="Switch UID", alias="switchUid")
    system_id: Optional[StrictStr] = Field(default=None, description="SystemUid/Serial Number  of the array.", alias="systemId")
    type: Optional[StrictStr] = Field(default=None, description="type")
    __properties: ClassVar[List[str]] = ["associatedLinks", "commonResourceAttributes", "customerId", "device", "devicePort", "displayname", "domain", "enclosure", "generation", "id", "ipAddress", "macAddress", "portDescription", "resourceUri", "state", "switchName", "switchPortId", "switchUid", "systemId", "type"]

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
        """Create an instance of DeviceType4SwitchPortList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # set to None if associated_links (nullable) is None
        # and model_fields_set contains the field
        if self.associated_links is None and "associated_links" in self.model_fields_set:
            _dict['associatedLinks'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if device (nullable) is None
        # and model_fields_set contains the field
        if self.device is None and "device" in self.model_fields_set:
            _dict['device'] = None

        # set to None if device_port (nullable) is None
        # and model_fields_set contains the field
        if self.device_port is None and "device_port" in self.model_fields_set:
            _dict['devicePort'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if enclosure (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure is None and "enclosure" in self.model_fields_set:
            _dict['enclosure'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if ip_address (nullable) is None
        # and model_fields_set contains the field
        if self.ip_address is None and "ip_address" in self.model_fields_set:
            _dict['ipAddress'] = None

        # set to None if mac_address (nullable) is None
        # and model_fields_set contains the field
        if self.mac_address is None and "mac_address" in self.model_fields_set:
            _dict['macAddress'] = None

        # set to None if port_description (nullable) is None
        # and model_fields_set contains the field
        if self.port_description is None and "port_description" in self.model_fields_set:
            _dict['portDescription'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if switch_name (nullable) is None
        # and model_fields_set contains the field
        if self.switch_name is None and "switch_name" in self.model_fields_set:
            _dict['switchName'] = None

        # set to None if switch_port_id (nullable) is None
        # and model_fields_set contains the field
        if self.switch_port_id is None and "switch_port_id" in self.model_fields_set:
            _dict['switchPortId'] = None

        # set to None if switch_uid (nullable) is None
        # and model_fields_set contains the field
        if self.switch_uid is None and "switch_uid" in self.model_fields_set:
            _dict['switchUid'] = None

        # set to None if system_id (nullable) is None
        # and model_fields_set contains the field
        if self.system_id is None and "system_id" in self.model_fields_set:
            _dict['systemId'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4SwitchPortList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedLinks": [AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "commonResourceAttributes": CommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "customerId": obj.get("customerId"),
            "device": obj.get("device"),
            "devicePort": obj.get("devicePort"),
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "enclosure": obj.get("enclosure"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "ipAddress": obj.get("ipAddress"),
            "macAddress": obj.get("macAddress"),
            "portDescription": obj.get("portDescription"),
            "resourceUri": obj.get("resourceUri"),
            "state": DeviceType4State.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "switchName": obj.get("switchName"),
            "switchPortId": obj.get("switchPortId"),
            "switchUid": obj.get("switchUid"),
            "systemId": obj.get("systemId"),
            "type": obj.get("type")
        })
        return _obj


