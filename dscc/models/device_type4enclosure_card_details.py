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
from dscc.models.device_type4ec_dcsdata import DeviceType4ecDcsdata
from dscc.models.device_type4enclosure_type_single import DeviceType4enclosureTypeSingle
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4enclosureCardDetails(BaseModel):
    """
    DeviceType4enclosureCardDetails
    """ # noqa: E501
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    dcsdata: Optional[DeviceType4ecDcsdata] = None
    displayname: Optional[StrictStr] = Field(default=None, description="Enclosure Display name")
    domain: Optional[StrictStr] = Field(default=None, description="Domain that the resource belongs to")
    element_status_code: Optional[StrictStr] = Field(default=None, description="Enclosure status code", alias="elementStatusCode")
    enclosure_card_id: Optional[StrictInt] = Field(default=None, description="ID of enclosure card.", alias="enclosureCardId")
    enclosure_id: Optional[StrictInt] = Field(default=None, alias="enclosureId")
    enclosure_name: Optional[StrictStr] = Field(default=None, description="Name of the enclosure.", alias="enclosureName")
    enclosure_type: Optional[DeviceType4enclosureTypeSingle] = Field(default=None, alias="enclosureType")
    enclosure_uid: Optional[StrictStr] = Field(default=None, description="Parent UID of the resource.", alias="enclosureUid")
    fail_indicator: Optional[StrictBool] = Field(default=None, alias="failIndicator")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the resource.")
    is_node_card: Optional[StrictBool] = Field(default=None, alias="isNodeCard")
    locate_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if the locate beacon is enabled or not", alias="locateEnabled")
    locate_seven_seg_display: Optional[StrictStr] = Field(default=None, description="Seven segment display on enclosure card when locate is on", alias="locateSevenSegDisplay")
    loop_a: Optional[StrictBool] = Field(default=None, alias="loopA")
    loop_b: Optional[StrictBool] = Field(default=None, alias="loopB")
    manufacturing: Optional[DeviceType4ManufacturingSingle] = None
    name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Name of the resource.")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed enclosure object", alias="resourceUri")
    safe_to_remove: Optional[StrictBool] = Field(default=None, alias="safeToRemove")
    seven_seg_display: Optional[StrictStr] = Field(default=None, description="Seven segment display", alias="sevenSegDisplay")
    state: Optional[DeviceType4State] = None
    system_id: Optional[StrictStr] = Field(default=None, description="SystemUid/Serial Number  of the array.", alias="systemId")
    type: Optional[StrictStr] = Field(default=None, description="type")
    __properties: ClassVar[List[str]] = ["customerId", "dcsdata", "displayname", "domain", "elementStatusCode", "enclosureCardId", "enclosureId", "enclosureName", "enclosureType", "enclosureUid", "failIndicator", "generation", "id", "isNodeCard", "locateEnabled", "locateSevenSegDisplay", "loopA", "loopB", "manufacturing", "name", "resourceUri", "safeToRemove", "sevenSegDisplay", "state", "systemId", "type"]

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
        """Create an instance of DeviceType4enclosureCardDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dcsdata
        if self.dcsdata:
            _dict['dcsdata'] = self.dcsdata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manufacturing
        if self.manufacturing:
            _dict['manufacturing'] = self.manufacturing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if dcsdata (nullable) is None
        # and model_fields_set contains the field
        if self.dcsdata is None and "dcsdata" in self.model_fields_set:
            _dict['dcsdata'] = None

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

        # set to None if enclosure_uid (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_uid is None and "enclosure_uid" in self.model_fields_set:
            _dict['enclosureUid'] = None

        # set to None if fail_indicator (nullable) is None
        # and model_fields_set contains the field
        if self.fail_indicator is None and "fail_indicator" in self.model_fields_set:
            _dict['failIndicator'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if is_node_card (nullable) is None
        # and model_fields_set contains the field
        if self.is_node_card is None and "is_node_card" in self.model_fields_set:
            _dict['isNodeCard'] = None

        # set to None if locate_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.locate_enabled is None and "locate_enabled" in self.model_fields_set:
            _dict['locateEnabled'] = None

        # set to None if locate_seven_seg_display (nullable) is None
        # and model_fields_set contains the field
        if self.locate_seven_seg_display is None and "locate_seven_seg_display" in self.model_fields_set:
            _dict['locateSevenSegDisplay'] = None

        # set to None if loop_a (nullable) is None
        # and model_fields_set contains the field
        if self.loop_a is None and "loop_a" in self.model_fields_set:
            _dict['loopA'] = None

        # set to None if loop_b (nullable) is None
        # and model_fields_set contains the field
        if self.loop_b is None and "loop_b" in self.model_fields_set:
            _dict['loopB'] = None

        # set to None if manufacturing (nullable) is None
        # and model_fields_set contains the field
        if self.manufacturing is None and "manufacturing" in self.model_fields_set:
            _dict['manufacturing'] = None

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

        # set to None if seven_seg_display (nullable) is None
        # and model_fields_set contains the field
        if self.seven_seg_display is None and "seven_seg_display" in self.model_fields_set:
            _dict['sevenSegDisplay'] = None

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
        """Create an instance of DeviceType4enclosureCardDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customerId": obj.get("customerId"),
            "dcsdata": DeviceType4ecDcsdata.from_dict(obj["dcsdata"]) if obj.get("dcsdata") is not None else None,
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "elementStatusCode": obj.get("elementStatusCode"),
            "enclosureCardId": obj.get("enclosureCardId"),
            "enclosureId": obj.get("enclosureId"),
            "enclosureName": obj.get("enclosureName"),
            "enclosureType": obj.get("enclosureType"),
            "enclosureUid": obj.get("enclosureUid"),
            "failIndicator": obj.get("failIndicator"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "isNodeCard": obj.get("isNodeCard"),
            "locateEnabled": obj.get("locateEnabled"),
            "locateSevenSegDisplay": obj.get("locateSevenSegDisplay"),
            "loopA": obj.get("loopA"),
            "loopB": obj.get("loopB"),
            "manufacturing": DeviceType4ManufacturingSingle.from_dict(obj["manufacturing"]) if obj.get("manufacturing") is not None else None,
            "name": obj.get("name"),
            "resourceUri": obj.get("resourceUri"),
            "safeToRemove": obj.get("safeToRemove"),
            "sevenSegDisplay": obj.get("sevenSegDisplay"),
            "state": DeviceType4State.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "systemId": obj.get("systemId"),
            "type": obj.get("type")
        })
        return _obj


