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
from dscc.models.device_type4_create_remote_copy_target_input import DeviceType4CreateRemoteCopyTargetInput
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4ReplicationPartnerInput(BaseModel):
    """
    Source and Target replication partner input details
    """ # noqa: E501
    replication_partner_system_id: StrictStr = Field(description="SystemId of target array", alias="replicationPartnerSystemId")
    source: Optional[DeviceType4CreateRemoteCopyTargetInput]
    target: Optional[DeviceType4CreateRemoteCopyTargetInput]
    __properties: ClassVar[List[str]] = ["replicationPartnerSystemId", "source", "target"]

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
        """Create an instance of DeviceType4ReplicationPartnerInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['source'] = None

        # set to None if target (nullable) is None
        # and model_fields_set contains the field
        if self.target is None and "target" in self.model_fields_set:
            _dict['target'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4ReplicationPartnerInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "replicationPartnerSystemId": obj.get("replicationPartnerSystemId"),
            "source": DeviceType4CreateRemoteCopyTargetInput.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "target": DeviceType4CreateRemoteCopyTargetInput.from_dict(obj["target"]) if obj.get("target") is not None else None
        })
        return _obj


