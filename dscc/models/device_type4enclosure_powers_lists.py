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
from dscc.models.device_type4_manufacturing_single import DeviceType4ManufacturingSingle
from dscc.models.device_type4_state import DeviceType4State
from dscc.models.device_type4enclosure_type_single import DeviceType4enclosureTypeSingle
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4enclosurePowersLists(BaseModel):
    """
    DeviceType4enclosurePowersLists
    """ # noqa: E501
    ac_status: Optional[StrictStr] = Field(default=None, alias="acStatus")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    dc_status: Optional[StrictStr] = Field(default=None, alias="dcStatus")
    displayname: Optional[StrictStr] = Field(default=None, description="Enclosure power Display name")
    domain: Optional[StrictStr] = Field(default=None, description="Domain that the resource belongs to")
    element_status_code: Optional[StrictStr] = Field(default=None, description="Enclosure status code", alias="elementStatusCode")
    enclosure_id: Optional[StrictInt] = Field(default=None, alias="enclosureId")
    enclosure_name: Optional[StrictStr] = Field(default=None, description="Name of the enclosure power.", alias="enclosureName")
    enclosure_power_id: Optional[StrictInt] = Field(default=None, description="Numeric ID of the resource. This is deprecated.", alias="enclosurePowerId")
    enclosure_power_supply_id: Optional[StrictInt] = Field(default=None, description="Numeric ID of the resource.", alias="enclosurePowerSupplyId")
    enclosure_type: Optional[DeviceType4enclosureTypeSingle] = Field(default=None, alias="enclosureType")
    enclosure_uid: Optional[StrictStr] = Field(default=None, description="Parent UID of the resource.", alias="enclosureUid")
    fail_indicator: Optional[StrictBool] = Field(default=None, alias="failIndicator")
    fail_input: Optional[StrictBool] = Field(default=None, alias="failInput")
    fail_output: Optional[StrictBool] = Field(default=None, alias="failOutput")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the resource.")
    locate_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if the locate beacon is enabled or not", alias="locateEnabled")
    manufacturing: Optional[DeviceType4ManufacturingSingle] = None
    model_read_only: Optional[StrictBool] = Field(default=None, alias="modelReadOnly")
    name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Name of the resource.")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed enclosure object", alias="resourceUri")
    safe_to_remove: Optional[StrictBool] = Field(default=None, alias="safeToRemove")
    state: Optional[DeviceType4State] = None
    system_id: Optional[StrictStr] = Field(default=None, description="SystemUid/Serial Number  of the array.", alias="systemId")
    type: Optional[StrictStr] = Field(default=None, description="type")
    __properties: ClassVar[List[str]] = ["acStatus", "customerId", "dcStatus", "displayname", "domain", "elementStatusCode", "enclosureId", "enclosureName", "enclosurePowerId", "enclosurePowerSupplyId", "enclosureType", "enclosureUid", "failIndicator", "failInput", "failOutput", "generation", "id", "locateEnabled", "manufacturing", "modelReadOnly", "name", "resourceUri", "safeToRemove", "state", "systemId", "type"]

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
        """Create an instance of DeviceType4enclosurePowersLists from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # set to None if ac_status (nullable) is None
        # and model_fields_set contains the field
        if self.ac_status is None and "ac_status" in self.model_fields_set:
            _dict['acStatus'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if dc_status (nullable) is None
        # and model_fields_set contains the field
        if self.dc_status is None and "dc_status" in self.model_fields_set:
            _dict['dcStatus'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if element_status_code (nullable) is None
        # and model_fields_set contains the field
        if self.element_status_code is None and "element_status_code" in self.model_fields_set:
            _dict['elementStatusCode'] = None

        # set to None if enclosure_id (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_id is None and "enclosure_id" in self.model_fields_set:
            _dict['enclosureId'] = None

        # set to None if enclosure_name (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_name is None and "enclosure_name" in self.model_fields_set:
            _dict['enclosureName'] = None

        # set to None if enclosure_power_id (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_power_id is None and "enclosure_power_id" in self.model_fields_set:
            _dict['enclosurePowerId'] = None

        # set to None if enclosure_power_supply_id (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_power_supply_id is None and "enclosure_power_supply_id" in self.model_fields_set:
            _dict['enclosurePowerSupplyId'] = None

        # set to None if enclosure_uid (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_uid is None and "enclosure_uid" in self.model_fields_set:
            _dict['enclosureUid'] = None

        # set to None if fail_indicator (nullable) is None
        # and model_fields_set contains the field
        if self.fail_indicator is None and "fail_indicator" in self.model_fields_set:
            _dict['failIndicator'] = None

        # set to None if fail_input (nullable) is None
        # and model_fields_set contains the field
        if self.fail_input is None and "fail_input" in self.model_fields_set:
            _dict['failInput'] = None

        # set to None if fail_output (nullable) is None
        # and model_fields_set contains the field
        if self.fail_output is None and "fail_output" in self.model_fields_set:
            _dict['failOutput'] = None

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

        # set to None if model_read_only (nullable) is None
        # and model_fields_set contains the field
        if self.model_read_only is None and "model_read_only" in self.model_fields_set:
            _dict['modelReadOnly'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if safe_to_remove (nullable) is None
        # and model_fields_set contains the field
        if self.safe_to_remove is None and "safe_to_remove" in self.model_fields_set:
            _dict['safeToRemove'] = None

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
        """Create an instance of DeviceType4enclosurePowersLists from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "acStatus": obj.get("acStatus"),
            "customerId": obj.get("customerId"),
            "dcStatus": obj.get("dcStatus"),
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "elementStatusCode": obj.get("elementStatusCode"),
            "enclosureId": obj.get("enclosureId"),
            "enclosureName": obj.get("enclosureName"),
            "enclosurePowerId": obj.get("enclosurePowerId"),
            "enclosurePowerSupplyId": obj.get("enclosurePowerSupplyId"),
            "enclosureType": obj.get("enclosureType"),
            "enclosureUid": obj.get("enclosureUid"),
            "failIndicator": obj.get("failIndicator"),
            "failInput": obj.get("failInput"),
            "failOutput": obj.get("failOutput"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "locateEnabled": obj.get("locateEnabled"),
            "manufacturing": DeviceType4ManufacturingSingle.from_dict(obj["manufacturing"]) if obj.get("manufacturing") is not None else None,
            "modelReadOnly": obj.get("modelReadOnly"),
            "name": obj.get("name"),
            "resourceUri": obj.get("resourceUri"),
            "safeToRemove": obj.get("safeToRemove"),
            "state": DeviceType4State.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "systemId": obj.get("systemId"),
            "type": obj.get("type")
        })
        return _obj


