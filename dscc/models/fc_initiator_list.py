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

class FCInitiatorList(BaseModel):
    """
    FCInitiatorList
    """ # noqa: E501
    alias: Optional[StrictStr] = Field(default=None, description="Alias of the Fibre Channel initiator. Maximum alias length is 32 characters. Each initiator alias must have an associated WWPN specified using the 'wwpn' attribute.You can choose not to enter the WWPN for an initiator when using previously saved initiator alias.String of up to 32 alphanumeric characters, or one of $^-_.: cannot begin with non-alphanumeric character.")
    id: Optional[StrictStr] = Field(default=None, description="Identifier for the FC Initiator. A 42 digit hexadecimal number.")
    wwpn: Optional[StrictStr] = Field(default=None, description="WWPN (World Wide Port Name) of the Fibre Channel initiator. WWPN is required when creating a Fibre Channel initiator. Each initiator WWPN can have an associated alias specified using the 'alias' attribute. You can choose not to enter the alias for an initiator if you prefer not to assign an initiator alias. Eight bytes expressed in hex separated by colons.")
    __properties: ClassVar[List[str]] = ["alias", "id", "wwpn"]

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
        """Create an instance of FCInitiatorList from a JSON string"""
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
        # set to None if alias (nullable) is None
        # and model_fields_set contains the field
        if self.alias is None and "alias" in self.model_fields_set:
            _dict['alias'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if wwpn (nullable) is None
        # and model_fields_set contains the field
        if self.wwpn is None and "wwpn" in self.model_fields_set:
            _dict['wwpn'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FCInitiatorList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alias": obj.get("alias"),
            "id": obj.get("id"),
            "wwpn": obj.get("wwpn")
        })
        return _obj


