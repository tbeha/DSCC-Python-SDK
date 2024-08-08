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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from dscc.models.device_type4_protection_policy_remote_input_schema import DeviceType4ProtectionPolicyRemoteInputSchema
from dscc.models.device_type4_protection_policy_secondary_remote_input_schema import DeviceType4ProtectionPolicySecondaryRemoteInputSchema
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4ProtectionPolicyInputSchema(BaseModel):
    """
    Protection policy details
    """ # noqa: E501
    auto_recover: Optional[StrictBool] = Field(default=None, description="Specifies that if the protected volume set is stopped as a result of the Remote Copy links going down, the protected volume set is restarted automatically after the links come back up.  If this policy is enabled for a volume set while the volume set is stopped after link failures, it will only be started when the links come up for the failed target.  If the links are already up at the time the policy is set, then the protected volume set will not be restarted at that time.", alias="autoRecover")
    auto_synchronize: Optional[Any] = Field(default=None, description="This property ensures that the Remote Copy system automatically recovers and synchronizes all volumes in the protected volume set after a system failover, for either automatic or manual failover scenarios.  Synchronization occurs after system recovery completes and the Remote Copy links recover. This policy also allows the failover command to be used when synchronous volume sets are started and are online.  It is no longer necessary to stop the synchronous volume sets before initiating a failover command to the secondary system.", alias="autoSynchronize")
    no_automatic_synchronization: Optional[StrictBool] = Field(default=None, description="Enabling this option results in no synchronization happening between the source and target application sets. This is applicable only in case of periodic replication, and is disabled by default.", alias="noAutomaticSynchronization")
    over_period_alert: Optional[StrictBool] = Field(default=None, description="If synchronization of an asynchronous periodic protection takes longer to complete than its synchronization period, an alert is generated. This property is not valid and hence cannot be enabled in case of synchronous replication.", alias="overPeriodAlert")
    remote: DeviceType4ProtectionPolicyRemoteInputSchema = Field(description="Replication partner details for remote protection")
    rpo_secs: Optional[StrictInt] = Field(default=None, description="Specifies recovery point objective in seconds for asynchronous periodic protection. Range: 30 - 63072000, and should be an even number. For Synchronous replication, the value defaults to zero even if it is specified. For Asynchronous replication, if rpoSecs is not specified then it would be considered under the no-automatic-synchronization option, and no synchronization happens.", alias="rpoSecs")
    secondary_remote: Optional[DeviceType4ProtectionPolicySecondaryRemoteInputSchema] = Field(default=None, description="Replication partner details for Async partner in Synchronous Long Distance mode and for 3DC Peer Persistence mode", alias="secondaryRemote")
    zero_rto_config: Optional[StrictStr] = Field(default=None, description="Zero RTO configuration to be used. Supported config is Active Peer Persistence. Classic Peer Persistence is not supported by HPE Alletra Storage MP. If this is not specified, the configuration will be Plain Synchronous Configuration. ", alias="zeroRtoConfig")
    __properties: ClassVar[List[str]] = ["autoRecover", "autoSynchronize", "noAutomaticSynchronization", "overPeriodAlert", "remote", "rpoSecs", "secondaryRemote", "zeroRtoConfig"]

    @field_validator('zero_rto_config')
    def zero_rto_config_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['APP']):
            raise ValueError("must be one of enum values ('APP')")
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
        """Create an instance of DeviceType4ProtectionPolicyInputSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of remote
        if self.remote:
            _dict['remote'] = self.remote.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secondary_remote
        if self.secondary_remote:
            _dict['secondaryRemote'] = self.secondary_remote.to_dict()
        # set to None if auto_synchronize (nullable) is None
        # and model_fields_set contains the field
        if self.auto_synchronize is None and "auto_synchronize" in self.model_fields_set:
            _dict['autoSynchronize'] = None

        # set to None if no_automatic_synchronization (nullable) is None
        # and model_fields_set contains the field
        if self.no_automatic_synchronization is None and "no_automatic_synchronization" in self.model_fields_set:
            _dict['noAutomaticSynchronization'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4ProtectionPolicyInputSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "autoRecover": obj.get("autoRecover"),
            "autoSynchronize": obj.get("autoSynchronize"),
            "noAutomaticSynchronization": obj.get("noAutomaticSynchronization"),
            "overPeriodAlert": obj.get("overPeriodAlert"),
            "remote": DeviceType4ProtectionPolicyRemoteInputSchema.from_dict(obj["remote"]) if obj.get("remote") is not None else None,
            "rpoSecs": obj.get("rpoSecs"),
            "secondaryRemote": DeviceType4ProtectionPolicySecondaryRemoteInputSchema.from_dict(obj["secondaryRemote"]) if obj.get("secondaryRemote") is not None else None,
            "zeroRtoConfig": obj.get("zeroRtoConfig")
        })
        return _obj


