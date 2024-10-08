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
from typing import Optional, Set
from typing_extensions import Self

class PortISCSIEdit(BaseModel):
    """
    PortISCSIEdit
    """ # noqa: E501
    gateway_address: Optional[StrictStr] = Field(default=None, description="Gateway address to edit to", alias="gatewayAddress")
    ip_address: Optional[StrictStr] = Field(default=None, description="IP address to edit to", alias="ipAddress")
    label: Optional[StrictStr] = Field(default=None, description="label of the port to edit to")
    mtu: Optional[StrictStr] = Field(default=None, description="MTU to edit to. Possible Values: \"1500\", \"9000\"")
    net_mask: Optional[StrictStr] = Field(default=None, description="NetMask address to edit to", alias="netMask")
    send_target_group_tag: Optional[StrictInt] = Field(default=None, alias="sendTargetGroupTag")
    __properties: ClassVar[List[str]] = ["gatewayAddress", "ipAddress", "label", "mtu", "netMask", "sendTargetGroupTag"]

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
        """Create an instance of PortISCSIEdit from a JSON string"""
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
        # set to None if gateway_address (nullable) is None
        # and model_fields_set contains the field
        if self.gateway_address is None and "gateway_address" in self.model_fields_set:
            _dict['gatewayAddress'] = None

        # set to None if label (nullable) is None
        # and model_fields_set contains the field
        if self.label is None and "label" in self.model_fields_set:
            _dict['label'] = None

        # set to None if send_target_group_tag (nullable) is None
        # and model_fields_set contains the field
        if self.send_target_group_tag is None and "send_target_group_tag" in self.model_fields_set:
            _dict['sendTargetGroupTag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PortISCSIEdit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gatewayAddress": obj.get("gatewayAddress"),
            "ipAddress": obj.get("ipAddress"),
            "label": obj.get("label"),
            "mtu": obj.get("mtu"),
            "netMask": obj.get("netMask"),
            "sendTargetGroupTag": obj.get("sendTargetGroupTag")
        })
        return _obj


