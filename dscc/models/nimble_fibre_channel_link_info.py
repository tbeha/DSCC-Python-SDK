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

class NimbleFibreChannelLinkInfo(BaseModel):
    """
    NimbleFibreChannelLinkInfo
    """ # noqa: E501
    link_speed: Optional[StrictStr] = Field(default=None, description="Speed of the Fibre Channel link.")
    link_status: Optional[StrictStr] = Field(default=None, description="Status of the Fibre Channel link. Possible values: plat_fc_link_status_reset, plat_fc_link_status_down, plat_fc_link_status_up, plat_fc_link_status_error, plat_fc_link_status_unknown, plat_fc_link_status_not_connected")
    max_link_speed: Optional[StrictStr] = Field(default=None, description="Maximum speed of the Fibre Channel link.")
    operational_status: Optional[StrictStr] = Field(default=None, description="Operational status of the Fibre Channel link. Possible values: plat_fc_operational_status_admin_offline, plat_fc_operational_status_direct, plat_fc_operational_status_initializing, plat_fc_operational_status_configured, plat_fc_operational_status_fault, plat_fc_operational_status_operational, plat_fc_operational_status_unknown, plat_fc_operational_status_unconfigured")
    __properties: ClassVar[List[str]] = ["link_speed", "link_status", "max_link_speed", "operational_status"]

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
        """Create an instance of NimbleFibreChannelLinkInfo from a JSON string"""
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
        # set to None if link_speed (nullable) is None
        # and model_fields_set contains the field
        if self.link_speed is None and "link_speed" in self.model_fields_set:
            _dict['link_speed'] = None

        # set to None if link_status (nullable) is None
        # and model_fields_set contains the field
        if self.link_status is None and "link_status" in self.model_fields_set:
            _dict['link_status'] = None

        # set to None if max_link_speed (nullable) is None
        # and model_fields_set contains the field
        if self.max_link_speed is None and "max_link_speed" in self.model_fields_set:
            _dict['max_link_speed'] = None

        # set to None if operational_status (nullable) is None
        # and model_fields_set contains the field
        if self.operational_status is None and "operational_status" in self.model_fields_set:
            _dict['operational_status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleFibreChannelLinkInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "link_speed": obj.get("link_speed"),
            "link_status": obj.get("link_status"),
            "max_link_speed": obj.get("max_link_speed"),
            "operational_status": obj.get("operational_status")
        })
        return _obj


