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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dscc.models.associated_links_inner import AssociatedLinksInner
from dscc.models.led import LED
from dscc.models.manufacturing_single import ManufacturingSingle
from dscc.models.nodeuptime import Nodeuptime
from dscc.models.primera_common_resource_attributes import PrimeraCommonResourceAttributes
from dscc.models.state import STATE
from typing import Optional, Set
from typing_extensions import Self

class NodeDetails(BaseModel):
    """
    NodeDetails
    """ # noqa: E501
    node_id: Optional[StrictInt] = Field(default=None, description="Numeric ID of the resource.", alias="NodeId")
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    bios_version: Optional[StrictStr] = Field(default=None, description="Bios version", alias="biosVersion")
    cache_available_pct: Optional[StrictInt] = Field(default=None, description="Percentage of the cache available", alias="cacheAvailablePct")
    cache_enabled: Optional[StrictInt] = Field(default=None, description="Percentage of the cache enabled on the node", alias="cacheEnabled")
    common_resource_attributes: Optional[PrimeraCommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    control_memory_mi_b: Optional[StrictInt] = Field(default=None, description="Total control memory in the node in MiB", alias="controlMemoryMiB")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    data_memory_mi_b: Optional[StrictInt] = Field(default=None, description="Total data memory in the node in MiB", alias="dataMemoryMiB")
    displayname: Optional[StrictStr] = Field(default=None, description="Name to be used for display purposes")
    domain: Optional[StrictStr] = Field(default=None, description="Domain that the resource belongs to")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the resource.")
    in_cluster: Optional[StrictBool] = Field(default=None, description="Indicates if this node is part of the cluster.", alias="inCluster")
    kernel_version: Optional[StrictStr] = Field(default=None, description="Kernel version", alias="kernelVersion")
    locate_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if the locate beacon is enabled or not", alias="locateEnabled")
    manufacturing: Optional[ManufacturingSingle] = None
    master: Optional[StrictBool] = Field(default=None, description="Indicates if this is the master node.")
    name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Name of the resource.")
    online: Optional[StrictBool] = Field(default=None, description="Indicates if this node is online")
    request_uri: Optional[StrictStr] = Field(default=None, description="requestUri for detailed node object", alias="requestUri")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed node object", alias="resourceUri")
    safe_to_remove: Optional[StrictBool] = Field(default=None, description="Indicates if the component is safe to remove", alias="safeToRemove")
    service_led: Optional[StrictStr] = Field(default=None, description="LED state.", alias="serviceLED")
    state: Optional[STATE] = None
    state_description: Optional[StrictStr] = Field(default=None, description="State of the resource", alias="stateDescription")
    system_id: Optional[StrictStr] = Field(default=None, description="SystemId/Serial Number  of the array.", alias="systemId")
    system_led: Optional[LED] = Field(default=None, alias="systemLED")
    type: Optional[StrictStr] = Field(default=None, description="type")
    uptime: Optional[Nodeuptime] = None
    __properties: ClassVar[List[str]] = ["NodeId", "associatedLinks", "biosVersion", "cacheAvailablePct", "cacheEnabled", "commonResourceAttributes", "consoleUri", "controlMemoryMiB", "customerId", "dataMemoryMiB", "displayname", "domain", "generation", "id", "inCluster", "kernelVersion", "locateEnabled", "manufacturing", "master", "name", "online", "requestUri", "resourceUri", "safeToRemove", "serviceLED", "state", "stateDescription", "systemId", "systemLED", "type", "uptime"]

    @field_validator('service_led')
    def service_led_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LED_UNKNOWN', 'LED_OFF', 'LED_GREEN', 'LED_GREEN_BLNK', 'LED_AMBER', 'LED_AMBER_BLNK', 'LED_BLUE', 'LED_BLUE_BLNK', 'null']):
            raise ValueError("must be one of enum values ('LED_UNKNOWN', 'LED_OFF', 'LED_GREEN', 'LED_GREEN_BLNK', 'LED_AMBER', 'LED_AMBER_BLNK', 'LED_BLUE', 'LED_BLUE_BLNK', 'null')")
        return value

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
        """Create an instance of NodeDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of manufacturing
        if self.manufacturing:
            _dict['manufacturing'] = self.manufacturing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of uptime
        if self.uptime:
            _dict['uptime'] = self.uptime.to_dict()
        # set to None if node_id (nullable) is None
        # and model_fields_set contains the field
        if self.node_id is None and "node_id" in self.model_fields_set:
            _dict['NodeId'] = None

        # set to None if bios_version (nullable) is None
        # and model_fields_set contains the field
        if self.bios_version is None and "bios_version" in self.model_fields_set:
            _dict['biosVersion'] = None

        # set to None if cache_available_pct (nullable) is None
        # and model_fields_set contains the field
        if self.cache_available_pct is None and "cache_available_pct" in self.model_fields_set:
            _dict['cacheAvailablePct'] = None

        # set to None if cache_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.cache_enabled is None and "cache_enabled" in self.model_fields_set:
            _dict['cacheEnabled'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if control_memory_mi_b (nullable) is None
        # and model_fields_set contains the field
        if self.control_memory_mi_b is None and "control_memory_mi_b" in self.model_fields_set:
            _dict['controlMemoryMiB'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if data_memory_mi_b (nullable) is None
        # and model_fields_set contains the field
        if self.data_memory_mi_b is None and "data_memory_mi_b" in self.model_fields_set:
            _dict['dataMemoryMiB'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if in_cluster (nullable) is None
        # and model_fields_set contains the field
        if self.in_cluster is None and "in_cluster" in self.model_fields_set:
            _dict['inCluster'] = None

        # set to None if kernel_version (nullable) is None
        # and model_fields_set contains the field
        if self.kernel_version is None and "kernel_version" in self.model_fields_set:
            _dict['kernelVersion'] = None

        # set to None if locate_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.locate_enabled is None and "locate_enabled" in self.model_fields_set:
            _dict['locateEnabled'] = None

        # set to None if manufacturing (nullable) is None
        # and model_fields_set contains the field
        if self.manufacturing is None and "manufacturing" in self.model_fields_set:
            _dict['manufacturing'] = None

        # set to None if master (nullable) is None
        # and model_fields_set contains the field
        if self.master is None and "master" in self.model_fields_set:
            _dict['master'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if online (nullable) is None
        # and model_fields_set contains the field
        if self.online is None and "online" in self.model_fields_set:
            _dict['online'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestUri'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if safe_to_remove (nullable) is None
        # and model_fields_set contains the field
        if self.safe_to_remove is None and "safe_to_remove" in self.model_fields_set:
            _dict['safeToRemove'] = None

        # set to None if service_led (nullable) is None
        # and model_fields_set contains the field
        if self.service_led is None and "service_led" in self.model_fields_set:
            _dict['serviceLED'] = None

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

        # set to None if system_led (nullable) is None
        # and model_fields_set contains the field
        if self.system_led is None and "system_led" in self.model_fields_set:
            _dict['systemLED'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if uptime (nullable) is None
        # and model_fields_set contains the field
        if self.uptime is None and "uptime" in self.model_fields_set:
            _dict['uptime'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodeDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "NodeId": obj.get("NodeId"),
            "associatedLinks": [AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "biosVersion": obj.get("biosVersion"),
            "cacheAvailablePct": obj.get("cacheAvailablePct"),
            "cacheEnabled": obj.get("cacheEnabled"),
            "commonResourceAttributes": PrimeraCommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "consoleUri": obj.get("consoleUri"),
            "controlMemoryMiB": obj.get("controlMemoryMiB"),
            "customerId": obj.get("customerId"),
            "dataMemoryMiB": obj.get("dataMemoryMiB"),
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "inCluster": obj.get("inCluster"),
            "kernelVersion": obj.get("kernelVersion"),
            "locateEnabled": obj.get("locateEnabled"),
            "manufacturing": ManufacturingSingle.from_dict(obj["manufacturing"]) if obj.get("manufacturing") is not None else None,
            "master": obj.get("master"),
            "name": obj.get("name"),
            "online": obj.get("online"),
            "requestUri": obj.get("requestUri"),
            "resourceUri": obj.get("resourceUri"),
            "safeToRemove": obj.get("safeToRemove"),
            "serviceLED": obj.get("serviceLED"),
            "state": STATE.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "stateDescription": obj.get("stateDescription"),
            "systemId": obj.get("systemId"),
            "systemLED": obj.get("systemLED"),
            "type": obj.get("type"),
            "uptime": Nodeuptime.from_dict(obj["uptime"]) if obj.get("uptime") is not None else None
        })
        return _obj


