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
from dscc.models.dc4data import Dc4data
from dscc.models.device_type4errors_inner import DeviceType4errorsInner
from dscc.models.enc_dcsdata import EncDcsdata
from dscc.models.enclosure_type_single import EnclosureTypeSingle
from dscc.models.manufacturing_single import ManufacturingSingle
from dscc.models.primera_common_resource_attributes import PrimeraCommonResourceAttributes
from dscc.models.state import State
from typing import Optional, Set
from typing_extensions import Self

class EnclosuresDetails(BaseModel):
    """
    EnclosuresDetails
    """ # noqa: E501
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    chain_pos_loop_a: Optional[StrictInt] = Field(default=None, alias="chainPosLoopA")
    chain_pos_loop_b: Optional[StrictInt] = Field(default=None, alias="chainPosLoopB")
    common_resource_attributes: Optional[PrimeraCommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    dc4data: Optional[Dc4data] = None
    dcsdata: Optional[EncDcsdata] = None
    detailed_state: Optional[StrictStr] = Field(default=None, alias="detailedState")
    displayname: Optional[StrictStr] = Field(default=None, description="Enclosure Display name")
    domain: Optional[StrictStr] = Field(default=None, description="Domain that the resource belongs to")
    enclosure_id: Optional[StrictInt] = Field(default=None, description="Numeric ID of the resource", alias="enclosureId")
    enclosure_type: Optional[EnclosureTypeSingle] = Field(default=None, alias="enclosureType")
    errors: Optional[List[Optional[DeviceType4errorsInner]]] = Field(default=None, description="Errors occurred in enclosure")
    fail_indicator: Optional[StrictBool] = Field(default=None, alias="failIndicator")
    fail_requested: Optional[StrictBool] = Field(default=None, alias="failRequested")
    form_factor: Optional[StrictStr] = Field(default=None, alias="formFactor")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the resource.")
    locate_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if the locate beacon is enabled or not", alias="locateEnabled")
    location: Optional[StrictStr] = Field(default=None, description="Location of the resource")
    loop_split: Optional[StrictBool] = Field(default=None, alias="loopSplit")
    manufacturing: Optional[ManufacturingSingle] = None
    name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Name of the resource.")
    node_wwn: Optional[StrictStr] = Field(default=None, description="WWn of the node resource", alias="nodeWwn")
    request_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed enclosure object", alias="requestUri")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed enclosure object", alias="resourceUri")
    state: Optional[State] = None
    sub_type: Optional[StrictStr] = Field(default=None, description="Enclosure sub type", alias="subType")
    system_id: Optional[StrictStr] = Field(default=None, description="SystemUid/Serial Number  of the array.", alias="systemId")
    type: Optional[StrictStr] = Field(default=None, description="type")
    warn_indicator: Optional[StrictBool] = Field(default=None, alias="warnIndicator")
    warn_requested: Optional[StrictBool] = Field(default=None, alias="warnRequested")
    __properties: ClassVar[List[str]] = ["associatedLinks", "chainPosLoopA", "chainPosLoopB", "commonResourceAttributes", "consoleUri", "customerId", "dc4data", "dcsdata", "detailedState", "displayname", "domain", "enclosureId", "enclosureType", "errors", "failIndicator", "failRequested", "formFactor", "generation", "id", "locateEnabled", "location", "loopSplit", "manufacturing", "name", "nodeWwn", "requestUri", "resourceUri", "state", "subType", "systemId", "type", "warnIndicator", "warnRequested"]

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
        """Create an instance of EnclosuresDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dc4data
        if self.dc4data:
            _dict['dc4data'] = self.dc4data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dcsdata
        if self.dcsdata:
            _dict['dcsdata'] = self.dcsdata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        # override the default output from pydantic by calling `to_dict()` of manufacturing
        if self.manufacturing:
            _dict['manufacturing'] = self.manufacturing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # set to None if chain_pos_loop_a (nullable) is None
        # and model_fields_set contains the field
        if self.chain_pos_loop_a is None and "chain_pos_loop_a" in self.model_fields_set:
            _dict['chainPosLoopA'] = None

        # set to None if chain_pos_loop_b (nullable) is None
        # and model_fields_set contains the field
        if self.chain_pos_loop_b is None and "chain_pos_loop_b" in self.model_fields_set:
            _dict['chainPosLoopB'] = None

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

        # set to None if dc4data (nullable) is None
        # and model_fields_set contains the field
        if self.dc4data is None and "dc4data" in self.model_fields_set:
            _dict['dc4data'] = None

        # set to None if dcsdata (nullable) is None
        # and model_fields_set contains the field
        if self.dcsdata is None and "dcsdata" in self.model_fields_set:
            _dict['dcsdata'] = None

        # set to None if detailed_state (nullable) is None
        # and model_fields_set contains the field
        if self.detailed_state is None and "detailed_state" in self.model_fields_set:
            _dict['detailedState'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if enclosure_id (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_id is None and "enclosure_id" in self.model_fields_set:
            _dict['enclosureId'] = None

        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        # set to None if fail_indicator (nullable) is None
        # and model_fields_set contains the field
        if self.fail_indicator is None and "fail_indicator" in self.model_fields_set:
            _dict['failIndicator'] = None

        # set to None if fail_requested (nullable) is None
        # and model_fields_set contains the field
        if self.fail_requested is None and "fail_requested" in self.model_fields_set:
            _dict['failRequested'] = None

        # set to None if form_factor (nullable) is None
        # and model_fields_set contains the field
        if self.form_factor is None and "form_factor" in self.model_fields_set:
            _dict['formFactor'] = None

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

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if loop_split (nullable) is None
        # and model_fields_set contains the field
        if self.loop_split is None and "loop_split" in self.model_fields_set:
            _dict['loopSplit'] = None

        # set to None if manufacturing (nullable) is None
        # and model_fields_set contains the field
        if self.manufacturing is None and "manufacturing" in self.model_fields_set:
            _dict['manufacturing'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if node_wwn (nullable) is None
        # and model_fields_set contains the field
        if self.node_wwn is None and "node_wwn" in self.model_fields_set:
            _dict['nodeWwn'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestUri'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if sub_type (nullable) is None
        # and model_fields_set contains the field
        if self.sub_type is None and "sub_type" in self.model_fields_set:
            _dict['subType'] = None

        # set to None if system_id (nullable) is None
        # and model_fields_set contains the field
        if self.system_id is None and "system_id" in self.model_fields_set:
            _dict['systemId'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if warn_indicator (nullable) is None
        # and model_fields_set contains the field
        if self.warn_indicator is None and "warn_indicator" in self.model_fields_set:
            _dict['warnIndicator'] = None

        # set to None if warn_requested (nullable) is None
        # and model_fields_set contains the field
        if self.warn_requested is None and "warn_requested" in self.model_fields_set:
            _dict['warnRequested'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EnclosuresDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedLinks": [AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "chainPosLoopA": obj.get("chainPosLoopA"),
            "chainPosLoopB": obj.get("chainPosLoopB"),
            "commonResourceAttributes": PrimeraCommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "dc4data": Dc4data.from_dict(obj["dc4data"]) if obj.get("dc4data") is not None else None,
            "dcsdata": EncDcsdata.from_dict(obj["dcsdata"]) if obj.get("dcsdata") is not None else None,
            "detailedState": obj.get("detailedState"),
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "enclosureId": obj.get("enclosureId"),
            "enclosureType": obj.get("enclosureType"),
            "errors": [DeviceType4errorsInner.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "failIndicator": obj.get("failIndicator"),
            "failRequested": obj.get("failRequested"),
            "formFactor": obj.get("formFactor"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "locateEnabled": obj.get("locateEnabled"),
            "location": obj.get("location"),
            "loopSplit": obj.get("loopSplit"),
            "manufacturing": ManufacturingSingle.from_dict(obj["manufacturing"]) if obj.get("manufacturing") is not None else None,
            "name": obj.get("name"),
            "nodeWwn": obj.get("nodeWwn"),
            "requestUri": obj.get("requestUri"),
            "resourceUri": obj.get("resourceUri"),
            "state": State.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "subType": obj.get("subType"),
            "systemId": obj.get("systemId"),
            "type": obj.get("type"),
            "warnIndicator": obj.get("warnIndicator"),
            "warnRequested": obj.get("warnRequested")
        })
        return _obj


