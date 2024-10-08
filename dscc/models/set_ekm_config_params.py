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
from typing import Optional, Set
from typing_extensions import Self

class SetEKMConfigParams(BaseModel):
    """
    SetEKMConfigParams
    """ # noqa: E501
    ekmpassword: Optional[StrictStr] = Field(default=None, description="Password for External Key Manager.")
    ekmuser: Optional[StrictStr] = Field(default=None, description="Username on External Key Manager.")
    kmipprotocols: Optional[List[StrictStr]] = Field(default=None, description="KMIP protocol.")
    port: Optional[StrictStr] = Field(default=None, description="Connection port number for External Key Managers.")
    serverlist: Optional[List[StrictStr]] = Field(default=None, description="List of External Key Management servers.")
    __properties: ClassVar[List[str]] = ["ekmpassword", "ekmuser", "kmipprotocols", "port", "serverlist"]

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
        """Create an instance of SetEKMConfigParams from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SetEKMConfigParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ekmpassword": obj.get("ekmpassword"),
            "ekmuser": obj.get("ekmuser"),
            "kmipprotocols": obj.get("kmipprotocols"),
            "port": obj.get("port"),
            "serverlist": obj.get("serverlist")
        })
        return _obj


