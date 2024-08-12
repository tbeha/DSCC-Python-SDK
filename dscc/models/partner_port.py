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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dscc.models.partner_port_position import PartnerPortPosition
from typing import Optional, Set
from typing_extensions import Self

class PartnerPort(BaseModel):
    """
    PartnerPort
    """ # noqa: E501
    node_wwn_or_name: Optional[StrictStr] = Field(default=None, description="Node WWN (for FC) or iSCSI name (for iSCSI)", alias="nodeWwnOrName")
    port_wwn_or_ip: Optional[StrictStr] = Field(default=None, description="Port WWN (for FC) or IP address (for iSCSI)", alias="portWwnOrIp")
    position: Optional[PartnerPortPosition] = None
    __properties: ClassVar[List[str]] = ["nodeWwnOrName", "portWwnOrIp", "position"]

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
        """Create an instance of PartnerPort from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of position
        if self.position:
            _dict['position'] = self.position.to_dict()
        # set to None if node_wwn_or_name (nullable) is None
        # and model_fields_set contains the field
        if self.node_wwn_or_name is None and "node_wwn_or_name" in self.model_fields_set:
            _dict['nodeWwnOrName'] = None

        # set to None if port_wwn_or_ip (nullable) is None
        # and model_fields_set contains the field
        if self.port_wwn_or_ip is None and "port_wwn_or_ip" in self.model_fields_set:
            _dict['portWwnOrIp'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PartnerPort from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nodeWwnOrName": obj.get("nodeWwnOrName"),
            "portWwnOrIp": obj.get("portWwnOrIp"),
            "position": PartnerPortPosition.from_dict(obj["position"]) if obj.get("position") is not None else None
        })
        return _obj


