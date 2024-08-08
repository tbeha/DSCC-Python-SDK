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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class NimbleFcInterfaceList(BaseModel):
    """
    NimbleFcInterfaceList
    """ # noqa: E501
    bus_location: Optional[StrictStr] = Field(default=None, description="Bus location for the array.String of up to 64 alphanumeric characters")
    name: Optional[StrictStr] = Field(default=None, description="Name of the fibre channel config. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.")
    online: Optional[StrictBool] = Field(default=None, description="Online state of fibre channel config.")
    port: Optional[StrictInt] = Field(default=None, description="Port number for this interface.Unsigned 64-bit integer.")
    slot: Optional[StrictInt] = Field(default=None, description="Slot number for this fibre channel config. Unsigned 64-bit integer.")
    wwnn: Optional[StrictStr] = Field(default=None, description="WWNN (World Wide Node Name) of the Fibre Channel port.")
    wwpn: Optional[StrictStr] = Field(default=None, description="WWPN (World Wide Port Name) of the Fibre Channel target port.")
    __properties: ClassVar[List[str]] = ["bus_location", "name", "online", "port", "slot", "wwnn", "wwpn"]

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
        """Create an instance of NimbleFcInterfaceList from a JSON string"""
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
        # set to None if bus_location (nullable) is None
        # and model_fields_set contains the field
        if self.bus_location is None and "bus_location" in self.model_fields_set:
            _dict['bus_location'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if online (nullable) is None
        # and model_fields_set contains the field
        if self.online is None and "online" in self.model_fields_set:
            _dict['online'] = None

        # set to None if port (nullable) is None
        # and model_fields_set contains the field
        if self.port is None and "port" in self.model_fields_set:
            _dict['port'] = None

        # set to None if slot (nullable) is None
        # and model_fields_set contains the field
        if self.slot is None and "slot" in self.model_fields_set:
            _dict['slot'] = None

        # set to None if wwnn (nullable) is None
        # and model_fields_set contains the field
        if self.wwnn is None and "wwnn" in self.model_fields_set:
            _dict['wwnn'] = None

        # set to None if wwpn (nullable) is None
        # and model_fields_set contains the field
        if self.wwpn is None and "wwpn" in self.model_fields_set:
            _dict['wwpn'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleFcInterfaceList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bus_location": obj.get("bus_location"),
            "name": obj.get("name"),
            "online": obj.get("online"),
            "port": obj.get("port"),
            "slot": obj.get("slot"),
            "wwnn": obj.get("wwnn"),
            "wwpn": obj.get("wwpn")
        })
        return _obj


