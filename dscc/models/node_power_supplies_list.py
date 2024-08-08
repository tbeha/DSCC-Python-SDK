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
from typing_extensions import Annotated
from dscc.models.associated_links_inner import AssociatedLinksInner
from dscc.models.led import LED
from dscc.models.manufacturing_single import ManufacturingSingle
from dscc.models.primera_common_resource_attributes import PrimeraCommonResourceAttributes
from dscc.models.state import STATE
from typing import Optional, Set
from typing_extensions import Self

class NodePowerSuppliesList(BaseModel):
    """
    NodePowerSuppliesList
    """ # noqa: E501
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    common_resource_attributes: Optional[PrimeraCommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    displayname: Optional[StrictStr] = Field(default=None, description="Name to be used for display purposes")
    domain: Optional[StrictStr] = Field(default=None, description="Domain that the resource belongs to")
    fanspeed: Optional[StrictStr] = Field(default=None, description="Fan speed of the node power supply")
    fanstate: Optional[STATE] = None
    generation: Optional[StrictInt] = Field(default=None, description="generation `Filter, Sort`")
    id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the resource. `Filter`")
    locate_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if the locate beacon is enabled or not", alias="locateEnabled")
    manufacturing: Optional[ManufacturingSingle] = None
    name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Name of the resource. `Filter, Sort`")
    node_power_id: Optional[StrictInt] = Field(default=None, description="Numeric ID of the resource", alias="nodePowerId")
    primary_node_id: Optional[StrictInt] = Field(default=None, description="Primary node ID. `Filter, Sort`", alias="primaryNodeId")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed node power object", alias="resourceUri")
    safe_to_remove: Optional[StrictBool] = Field(default=None, description="Indicates if the component is safe to remove", alias="safeToRemove")
    secondary_node_id: Optional[StrictInt] = Field(default=None, description="Secondary node ID", alias="secondaryNodeId")
    service_led: Optional[LED] = Field(default=None, alias="serviceLED")
    state: Optional[STATE] = None
    system_id: Optional[StrictStr] = Field(default=None, description="SystemUid/Serial Number  of the array.", alias="systemId")
    type: Optional[StrictStr] = Field(default=None, description="type")
    __properties: ClassVar[List[str]] = ["associatedLinks", "commonResourceAttributes", "customerId", "displayname", "domain", "fanspeed", "fanstate", "generation", "id", "locateEnabled", "manufacturing", "name", "nodePowerId", "primaryNodeId", "resourceUri", "safeToRemove", "secondaryNodeId", "serviceLED", "state", "systemId", "type"]

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
        """Create an instance of NodePowerSuppliesList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of fanstate
        if self.fanstate:
            _dict['fanstate'] = self.fanstate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manufacturing
        if self.manufacturing:
            _dict['manufacturing'] = self.manufacturing.to_dict()
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

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if fanspeed (nullable) is None
        # and model_fields_set contains the field
        if self.fanspeed is None and "fanspeed" in self.model_fields_set:
            _dict['fanspeed'] = None

        # set to None if fanstate (nullable) is None
        # and model_fields_set contains the field
        if self.fanstate is None and "fanstate" in self.model_fields_set:
            _dict['fanstate'] = None

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

        # set to None if manufacturing (nullable) is None
        # and model_fields_set contains the field
        if self.manufacturing is None and "manufacturing" in self.model_fields_set:
            _dict['manufacturing'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if node_power_id (nullable) is None
        # and model_fields_set contains the field
        if self.node_power_id is None and "node_power_id" in self.model_fields_set:
            _dict['nodePowerId'] = None

        # set to None if primary_node_id (nullable) is None
        # and model_fields_set contains the field
        if self.primary_node_id is None and "primary_node_id" in self.model_fields_set:
            _dict['primaryNodeId'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if safe_to_remove (nullable) is None
        # and model_fields_set contains the field
        if self.safe_to_remove is None and "safe_to_remove" in self.model_fields_set:
            _dict['safeToRemove'] = None

        # set to None if secondary_node_id (nullable) is None
        # and model_fields_set contains the field
        if self.secondary_node_id is None and "secondary_node_id" in self.model_fields_set:
            _dict['secondaryNodeId'] = None

        # set to None if service_led (nullable) is None
        # and model_fields_set contains the field
        if self.service_led is None and "service_led" in self.model_fields_set:
            _dict['serviceLED'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

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
        """Create an instance of NodePowerSuppliesList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedLinks": [AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "commonResourceAttributes": PrimeraCommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "customerId": obj.get("customerId"),
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "fanspeed": obj.get("fanspeed"),
            "fanstate": STATE.from_dict(obj["fanstate"]) if obj.get("fanstate") is not None else None,
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "locateEnabled": obj.get("locateEnabled"),
            "manufacturing": ManufacturingSingle.from_dict(obj["manufacturing"]) if obj.get("manufacturing") is not None else None,
            "name": obj.get("name"),
            "nodePowerId": obj.get("nodePowerId"),
            "primaryNodeId": obj.get("primaryNodeId"),
            "resourceUri": obj.get("resourceUri"),
            "safeToRemove": obj.get("safeToRemove"),
            "secondaryNodeId": obj.get("secondaryNodeId"),
            "serviceLED": obj.get("serviceLED"),
            "state": STATE.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "systemId": obj.get("systemId"),
            "type": obj.get("type")
        })
        return _obj


