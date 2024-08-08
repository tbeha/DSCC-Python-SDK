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
from dscc.models.create_host_input import CreateHostInput
from typing import Optional, Set
from typing_extensions import Self

class CreateHostGroupInput(BaseModel):
    """
    CreateHostGroupInput
    """ # noqa: E501
    comment: Optional[StrictStr] = Field(default=None, description="Comment")
    host_ids: Optional[List[StrictStr]] = Field(default=None, description="List of host ids of existing hosts", alias="hostIds")
    hosts_to_create: Optional[List[CreateHostInput]] = Field(default=None, description="List of hosts to be created and added to this hostGroup", alias="hostsToCreate")
    name: Optional[StrictStr] = Field(description="Name of the host group")
    user_created: Optional[StrictBool] = Field(default=None, description="Indicates whether user created host group or discovered host group. value should always be set as \"true\". API will internally override the passed value to set it as \"true\".", alias="userCreated")
    __properties: ClassVar[List[str]] = ["comment", "hostIds", "hostsToCreate", "name", "userCreated"]

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
        """Create an instance of CreateHostGroupInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in hosts_to_create (list)
        _items = []
        if self.hosts_to_create:
            for _item in self.hosts_to_create:
                if _item:
                    _items.append(_item.to_dict())
            _dict['hostsToCreate'] = _items
        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if host_ids (nullable) is None
        # and model_fields_set contains the field
        if self.host_ids is None and "host_ids" in self.model_fields_set:
            _dict['hostIds'] = None

        # set to None if hosts_to_create (nullable) is None
        # and model_fields_set contains the field
        if self.hosts_to_create is None and "hosts_to_create" in self.model_fields_set:
            _dict['hostsToCreate'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if user_created (nullable) is None
        # and model_fields_set contains the field
        if self.user_created is None and "user_created" in self.model_fields_set:
            _dict['userCreated'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateHostGroupInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "comment": obj.get("comment"),
            "hostIds": obj.get("hostIds"),
            "hostsToCreate": [CreateHostInput.from_dict(_item) for _item in obj["hostsToCreate"]] if obj.get("hostsToCreate") is not None else None,
            "name": obj.get("name"),
            "userCreated": obj.get("userCreated")
        })
        return _obj


