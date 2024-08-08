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
from dscc.models.device_type4validity import DeviceType4validity
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4friendlyCert(BaseModel):
    """
    Certificate detail in readable format
    """ # noqa: E501
    valid_from: Optional[DeviceType4validity] = Field(default=None, alias="ValidFrom")
    valid_until: Optional[DeviceType4validity] = Field(default=None, alias="ValidUntil")
    issued_to: Optional[StrictStr] = Field(default=None, description="Name of the certificate issued to", alias="issuedTo")
    issuer: Optional[StrictStr] = Field(default=None, description="Name of Certificate issued to")
    __properties: ClassVar[List[str]] = ["ValidFrom", "ValidUntil", "issuedTo", "issuer"]

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
        """Create an instance of DeviceType4friendlyCert from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of valid_from
        if self.valid_from:
            _dict['ValidFrom'] = self.valid_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of valid_until
        if self.valid_until:
            _dict['ValidUntil'] = self.valid_until.to_dict()
        # set to None if valid_from (nullable) is None
        # and model_fields_set contains the field
        if self.valid_from is None and "valid_from" in self.model_fields_set:
            _dict['ValidFrom'] = None

        # set to None if valid_until (nullable) is None
        # and model_fields_set contains the field
        if self.valid_until is None and "valid_until" in self.model_fields_set:
            _dict['ValidUntil'] = None

        # set to None if issued_to (nullable) is None
        # and model_fields_set contains the field
        if self.issued_to is None and "issued_to" in self.model_fields_set:
            _dict['issuedTo'] = None

        # set to None if issuer (nullable) is None
        # and model_fields_set contains the field
        if self.issuer is None and "issuer" in self.model_fields_set:
            _dict['issuer'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4friendlyCert from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ValidFrom": DeviceType4validity.from_dict(obj["ValidFrom"]) if obj.get("ValidFrom") is not None else None,
            "ValidUntil": DeviceType4validity.from_dict(obj["ValidUntil"]) if obj.get("ValidUntil") is not None else None,
            "issuedTo": obj.get("issuedTo"),
            "issuer": obj.get("issuer")
        })
        return _obj


