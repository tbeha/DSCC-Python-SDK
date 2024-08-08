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

class DeviceType4portFC(BaseModel):
    """
    DeviceType4portFC
    """ # noqa: E501
    node_wwn: Optional[StrictStr] = Field(default=None, description="nodeWWN of the FC port", alias="nodeWWN")
    port_wwn: Optional[StrictStr] = Field(default=None, description="portWWN of the FC port", alias="portWWN")
    __properties: ClassVar[List[str]] = ["nodeWWN", "portWWN"]

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
        """Create an instance of DeviceType4portFC from a JSON string"""
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
        # set to None if node_wwn (nullable) is None
        # and model_fields_set contains the field
        if self.node_wwn is None and "node_wwn" in self.model_fields_set:
            _dict['nodeWWN'] = None

        # set to None if port_wwn (nullable) is None
        # and model_fields_set contains the field
        if self.port_wwn is None and "port_wwn" in self.model_fields_set:
            _dict['portWWN'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4portFC from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nodeWWN": obj.get("nodeWWN"),
            "portWWN": obj.get("portWWN")
        })
        return _obj


