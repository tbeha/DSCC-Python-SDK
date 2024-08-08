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
from dscc.models.nimble_common_resource_attributes import NimbleCommonResourceAttributes
from dscc.models.nimble_fc_initiator_info import NimbleFCInitiatorInfo
from dscc.models.nimble_fc_target_info import NimbleFCTargetInfo
from typing import Optional, Set
from typing_extensions import Self

class NimbleFCSessionDetails(BaseModel):
    """
    NimbleFCSessionDetails
    """ # noqa: E501
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details")
    common_resource_attributes: Optional[NimbleCommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the Fibre Channel session. A 42 digit hexadecimal number.")
    initiator_info: Optional[NimbleFCInitiatorInfo] = None
    resource_uri: Optional[StrictStr] = Field(default=None, description="Link to the object URI", alias="resourceUri")
    sc_host_initiator_id: Optional[StrictStr] = Field(default=None, description="Host Service Initiator Id", alias="sc_HostInitiatorId")
    target_info: Optional[NimbleFCTargetInfo] = None
    type: Optional[StrictStr] = Field(default=None, description="type")
    __properties: ClassVar[List[str]] = ["associated_links", "commonResourceAttributes", "consoleUri", "customerId", "generation", "id", "initiator_info", "resourceUri", "sc_HostInitiatorId", "target_info", "type"]

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
        """Create an instance of NimbleFCSessionDetails from a JSON string"""
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
            _dict['associated_links'] = _items
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of initiator_info
        if self.initiator_info:
            _dict['initiator_info'] = self.initiator_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_info
        if self.target_info:
            _dict['target_info'] = self.target_info.to_dict()
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

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if initiator_info (nullable) is None
        # and model_fields_set contains the field
        if self.initiator_info is None and "initiator_info" in self.model_fields_set:
            _dict['initiator_info'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if sc_host_initiator_id (nullable) is None
        # and model_fields_set contains the field
        if self.sc_host_initiator_id is None and "sc_host_initiator_id" in self.model_fields_set:
            _dict['sc_HostInitiatorId'] = None

        # set to None if target_info (nullable) is None
        # and model_fields_set contains the field
        if self.target_info is None and "target_info" in self.model_fields_set:
            _dict['target_info'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleFCSessionDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associated_links": [AssociatedLinksInner.from_dict(_item) for _item in obj["associated_links"]] if obj.get("associated_links") is not None else None,
            "commonResourceAttributes": NimbleCommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "initiator_info": NimbleFCInitiatorInfo.from_dict(obj["initiator_info"]) if obj.get("initiator_info") is not None else None,
            "resourceUri": obj.get("resourceUri"),
            "sc_HostInitiatorId": obj.get("sc_HostInitiatorId"),
            "target_info": NimbleFCTargetInfo.from_dict(obj["target_info"]) if obj.get("target_info") is not None else None,
            "type": obj.get("type")
        })
        return _obj


