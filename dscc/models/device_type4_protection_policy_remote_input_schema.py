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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4ProtectionPolicyRemoteInputSchema(BaseModel):
    """
    DeviceType4ProtectionPolicyRemoteInputSchema
    """ # noqa: E501
    partner_id: StrictStr = Field(description="Remote partner ID", alias="partnerId")
    partner_name: StrictStr = Field(description="Remote partner name", alias="partnerName")
    replication_partner_snapshot_cpg: Optional[StrictStr] = Field(default=None, description="Replication Partner Snapshot CPG. Applicable only if the target system is Primera or Alletra 9K. Currently, not supported due to OS limitation. This field will be supported in future release.", alias="replicationPartnerSnapshotCpg")
    replication_partner_user_cpg: Optional[StrictStr] = Field(default=None, description="User CPG in which the target volumes would get created in the replication partner system.", alias="replicationPartnerUserCpg")
    replication_type: StrictStr = Field(description="Replication type. Synchronous replication/protection policy provides protection from array or site failures with zero RPO. Using this policy, you can also configure zero RTO policy like Active Peer Persistence. Periodic replication (Asynchronous protection policy) provides protection from array or site failure with the user defined RPO.", alias="replicationType")
    __properties: ClassVar[List[str]] = ["partnerId", "partnerName", "replicationPartnerSnapshotCpg", "replicationPartnerUserCpg", "replicationType"]

    @field_validator('replication_type')
    def replication_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['sync', 'periodic']):
            raise ValueError("must be one of enum values ('sync', 'periodic')")
        return value

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
        """Create an instance of DeviceType4ProtectionPolicyRemoteInputSchema from a JSON string"""
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
        # set to None if replication_partner_snapshot_cpg (nullable) is None
        # and model_fields_set contains the field
        if self.replication_partner_snapshot_cpg is None and "replication_partner_snapshot_cpg" in self.model_fields_set:
            _dict['replicationPartnerSnapshotCpg'] = None

        # set to None if replication_partner_user_cpg (nullable) is None
        # and model_fields_set contains the field
        if self.replication_partner_user_cpg is None and "replication_partner_user_cpg" in self.model_fields_set:
            _dict['replicationPartnerUserCpg'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4ProtectionPolicyRemoteInputSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "partnerId": obj.get("partnerId"),
            "partnerName": obj.get("partnerName"),
            "replicationPartnerSnapshotCpg": obj.get("replicationPartnerSnapshotCpg"),
            "replicationPartnerUserCpg": obj.get("replicationPartnerUserCpg"),
            "replicationType": obj.get("replicationType")
        })
        return _obj


