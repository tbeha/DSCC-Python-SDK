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
from dscc.models.nimble_nic import NimbleNIC
from typing import Optional, Set
from typing_extensions import Self

class NimbleArrayNet(BaseModel):
    """
    NimbleArrayNet
    """ # noqa: E501
    ctrlr_a_support_ip: Optional[StrictStr] = Field(default=None, description="IP address of controller A.")
    ctrlr_b_support_ip: Optional[StrictStr] = Field(default=None, description="IP address of controller B.")
    member_gid: Optional[StrictInt] = Field(default=None, description="GID of member.")
    name: Optional[StrictStr] = Field(default=None, description="Name of the array.")
    nic_list: Optional[List[Optional[NimbleNIC]]] = Field(default=None, description="List of NICs.")
    __properties: ClassVar[List[str]] = ["ctrlr_a_support_ip", "ctrlr_b_support_ip", "member_gid", "name", "nic_list"]

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
        """Create an instance of NimbleArrayNet from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in nic_list (list)
        _items = []
        if self.nic_list:
            for _item in self.nic_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nic_list'] = _items
        # set to None if ctrlr_a_support_ip (nullable) is None
        # and model_fields_set contains the field
        if self.ctrlr_a_support_ip is None and "ctrlr_a_support_ip" in self.model_fields_set:
            _dict['ctrlr_a_support_ip'] = None

        # set to None if ctrlr_b_support_ip (nullable) is None
        # and model_fields_set contains the field
        if self.ctrlr_b_support_ip is None and "ctrlr_b_support_ip" in self.model_fields_set:
            _dict['ctrlr_b_support_ip'] = None

        # set to None if member_gid (nullable) is None
        # and model_fields_set contains the field
        if self.member_gid is None and "member_gid" in self.model_fields_set:
            _dict['member_gid'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if nic_list (nullable) is None
        # and model_fields_set contains the field
        if self.nic_list is None and "nic_list" in self.model_fields_set:
            _dict['nic_list'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleArrayNet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ctrlr_a_support_ip": obj.get("ctrlr_a_support_ip"),
            "ctrlr_b_support_ip": obj.get("ctrlr_b_support_ip"),
            "member_gid": obj.get("member_gid"),
            "name": obj.get("name"),
            "nic_list": [NimbleNIC.from_dict(_item) for _item in obj["nic_list"]] if obj.get("nic_list") is not None else None
        })
        return _obj


