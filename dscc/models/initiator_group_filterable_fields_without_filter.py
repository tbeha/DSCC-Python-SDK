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

class InitiatorGroupFilterableFieldsWithoutFilter(BaseModel):
    """
    InitiatorGroupFilterableFieldsWithoutFilter
    """ # noqa: E501
    access_protocol: Optional[StrictStr] = Field(default=None, description="Initiator group access protocol. Possible values: 'iscsi', 'fc'.")
    app_uuid: Optional[StrictStr] = Field(default=None, description="Application identifier of initiator group. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed")
    host_type: Optional[StrictStr] = Field(default=None, description="Initiator group host type. Available options are auto and hpux. The default option is auto. This attribute will be applied to all the initiators in the initiator group. Initiators with different host OSes should not be kept in the same initiator group having a non-default host type attribute. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.")
    id: Optional[StrictStr] = Field(default=None, description="Identifier for initiator group. A 42 digit hexadecimal number.")
    name: Optional[StrictStr] = Field(default=None, description="Name of initiator group. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.")
    __properties: ClassVar[List[str]] = ["access_protocol", "app_uuid", "host_type", "id", "name"]

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
        """Create an instance of InitiatorGroupFilterableFieldsWithoutFilter from a JSON string"""
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
        # set to None if access_protocol (nullable) is None
        # and model_fields_set contains the field
        if self.access_protocol is None and "access_protocol" in self.model_fields_set:
            _dict['access_protocol'] = None

        # set to None if app_uuid (nullable) is None
        # and model_fields_set contains the field
        if self.app_uuid is None and "app_uuid" in self.model_fields_set:
            _dict['app_uuid'] = None

        # set to None if host_type (nullable) is None
        # and model_fields_set contains the field
        if self.host_type is None and "host_type" in self.model_fields_set:
            _dict['host_type'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InitiatorGroupFilterableFieldsWithoutFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access_protocol": obj.get("access_protocol"),
            "app_uuid": obj.get("app_uuid"),
            "host_type": obj.get("host_type"),
            "id": obj.get("id"),
            "name": obj.get("name")
        })
        return _obj


