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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class EncryptionSettings(BaseModel):
    """
    How encryption is configured for this group. Group encryption settings.
    """ # noqa: E501
    cipher: Optional[StrictStr] = Field(default=None, description="Type of encryption cipher used. Possible values: 'aes_256_xts', 'none'.")
    encryption_active: Optional[StrictBool] = Field(default=None, description="Is encryption active (output only).")
    encryption_key_manager: Optional[StrictStr] = Field(default=None, description="Is the master key on local or external key manager (output only). Possible values: 'external', 'local'.")
    master_key_set: Optional[StrictBool] = Field(default=None, description="Is the master key set (output only).")
    mode: Optional[StrictStr] = Field(default=None, description="Mode of encryption. Possible values: 'available', 'none', 'secure'.")
    scope: Optional[StrictStr] = Field(default=None, description="Encryption scope. Possible values: 'volume', 'pool', 'none', 'group'.")
    __properties: ClassVar[List[str]] = ["cipher", "encryption_active", "encryption_key_manager", "master_key_set", "mode", "scope"]

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
        """Create an instance of EncryptionSettings from a JSON string"""
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
        # set to None if cipher (nullable) is None
        # and model_fields_set contains the field
        if self.cipher is None and "cipher" in self.model_fields_set:
            _dict['cipher'] = None

        # set to None if encryption_active (nullable) is None
        # and model_fields_set contains the field
        if self.encryption_active is None and "encryption_active" in self.model_fields_set:
            _dict['encryption_active'] = None

        # set to None if encryption_key_manager (nullable) is None
        # and model_fields_set contains the field
        if self.encryption_key_manager is None and "encryption_key_manager" in self.model_fields_set:
            _dict['encryption_key_manager'] = None

        # set to None if master_key_set (nullable) is None
        # and model_fields_set contains the field
        if self.master_key_set is None and "master_key_set" in self.model_fields_set:
            _dict['master_key_set'] = None

        # set to None if mode (nullable) is None
        # and model_fields_set contains the field
        if self.mode is None and "mode" in self.model_fields_set:
            _dict['mode'] = None

        # set to None if scope (nullable) is None
        # and model_fields_set contains the field
        if self.scope is None and "scope" in self.model_fields_set:
            _dict['scope'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EncryptionSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cipher": obj.get("cipher"),
            "encryption_active": obj.get("encryption_active"),
            "encryption_key_manager": obj.get("encryption_key_manager"),
            "master_key_set": obj.get("master_key_set"),
            "mode": obj.get("mode"),
            "scope": obj.get("scope")
        })
        return _obj


