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

class NICDetails(BaseModel):
    """
    NICDetails
    """ # noqa: E501
    data_ip: Optional[StrictStr] = Field(default=None, description="Data IP address.")
    name: Optional[StrictStr] = Field(default=None, description="Name of NIC.")
    subnet_label: Optional[StrictStr] = Field(default=None, description="Subnet label for this NIC.")
    tagged: Optional[StrictBool] = Field(default=None, description="Identify whether the NIC is tagged.")
    __properties: ClassVar[List[str]] = ["data_ip", "name", "subnet_label", "tagged"]

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
        """Create an instance of NICDetails from a JSON string"""
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
        # set to None if data_ip (nullable) is None
        # and model_fields_set contains the field
        if self.data_ip is None and "data_ip" in self.model_fields_set:
            _dict['data_ip'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if subnet_label (nullable) is None
        # and model_fields_set contains the field
        if self.subnet_label is None and "subnet_label" in self.model_fields_set:
            _dict['subnet_label'] = None

        # set to None if tagged (nullable) is None
        # and model_fields_set contains the field
        if self.tagged is None and "tagged" in self.model_fields_set:
            _dict['tagged'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NICDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data_ip": obj.get("data_ip"),
            "name": obj.get("name"),
            "subnet_label": obj.get("subnet_label"),
            "tagged": obj.get("tagged")
        })
        return _obj


