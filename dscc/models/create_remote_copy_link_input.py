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
from typing import Any, ClassVar, Dict, List
from dscc.models.create_remote_copy_link_input_port_pos import CreateRemoteCopyLinkInputPortPos
from typing import Optional, Set
from typing_extensions import Self

class CreateRemoteCopyLinkInput(BaseModel):
    """
    Request body for creating remote copy links
    """ # noqa: E501
    address: StrictStr = Field(description="IP Address or WWN of Remote Copy target for this link, depending on the link type IP or FC")
    port_pos: CreateRemoteCopyLinkInputPortPos = Field(alias="portPos")
    target_name: StrictStr = Field(description="Remote Copy target with which the link is affiliated", alias="targetName")
    type: StrictInt = Field(description="Remote Copy link type. 1 for IP and 2 for FC")
    __properties: ClassVar[List[str]] = ["address", "portPos", "targetName", "type"]

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
        """Create an instance of CreateRemoteCopyLinkInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of port_pos
        if self.port_pos:
            _dict['portPos'] = self.port_pos.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateRemoteCopyLinkInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "portPos": CreateRemoteCopyLinkInputPortPos.from_dict(obj["portPos"]) if obj.get("portPos") is not None else None,
            "targetName": obj.get("targetName"),
            "type": obj.get("type")
        })
        return _obj


