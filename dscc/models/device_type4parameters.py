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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4parameters(BaseModel):
    """
    System parameters
    """ # noqa: E501
    service_processor_cookie: Optional[StrictStr] = Field(default=None, description="Service processor cookie", alias="ServiceProcessorCookie")
    allow_domain_users_affect_no_domain: Optional[StrictBool] = Field(default=None, alias="allowDomainUsersAffectNoDomain")
    allow_ssz: Optional[StrictBool] = Field(default=None, description="Enables or disables support for using the -ssz option during CPG creation", alias="allowSSZ")
    allow_wrtback_single_node: Optional[StrictInt] = Field(default=None, description="Allow writeback single node setting in days", alias="allowWrtbackSingleNode")
    allow_wrtback_upgrade: Optional[StrictInt] = Field(default=None, description="Allow the system to continue caching when in a single node state during an upgrade for up to the specified number of days", alias="allowWrtbackUpgrade")
    auto_admit_tune: Optional[StrictBool] = Field(default=None, description="Enables or disables automatic rebalancing when admithw detects new disks. Only applies to 2-node systems", alias="autoAdmitTune")
    auto_export_after_reboot: Optional[StrictBool] = Field(default=None, description="Enables or disables automatically exporting vluns after a reboot. If disabled, vluns and host ports will not become active after a reboot until \"setsysmgr export_vluns\" is issued.", alias="autoExportAfterReboot")
    compliance_officer_approval: Optional[StrictBool] = Field(default=None, description="Specifies whether to enable or disable the compliance officer approval mode.", alias="complianceOfficerApproval")
    disable_chunklet_init_unmap: Optional[StrictBool] = Field(default=None, description="Flag to know if the ChunkletInitUNMAP is disabled", alias="disableChunkletInitUNMAP")
    enable_aiqo_s: Optional[StrictStr] = Field(default=None, description="Enable or disable AI QoS feature, values are:yes or no", alias="enableAIQoS")
    event_log_num: Optional[StrictInt] = Field(default=None, description="The number of event log files", alias="eventLogNum")
    event_log_size: Optional[StrictStr] = Field(default=None, description="The size of the event log file", alias="eventLogSize")
    failover_matched_set: Optional[StrictBool] = Field(default=None, description="When using Matched Set VLUN templates for exports and Persistent Ports together, you must enable this parameter. The default for this setting is disabled", alias="failoverMatchedSet")
    fc_raw_space_alert: Optional[StrictInt] = Field(default=None, description="FC raw space alert setting in MiB", alias="fcRawSpaceAlert")
    host_dif: Optional[StrictStr] = Field(default=None, description="Host Data Integrity Field type are:yes or no", alias="hostDIF")
    host_dif_template: Optional[StrictStr] = Field(default=None, description="HostDIF Template", alias="hostDIFTemplate")
    max_volume_retention: Optional[StrictInt] = Field(default=None, description="Maximum global volume retention policy in seconds", alias="maxVolumeRetention")
    nl_raw_space_alert: Optional[StrictInt] = Field(default=None, description="NL raw space alert setting in MiB", alias="nlRawSpaceAlert")
    overprov_ratio_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Over provisioning ratio limit setting", alias="overprovRatioLimit")
    overprov_ratio_warning: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Over provisioning ratio warning setting", alias="overprovRatioWarning")
    persona_profile: Optional[StrictStr] = Field(default=None, description="If set to 'block-preferred' File persona is supported. The default is 'block-only'", alias="personaProfile")
    port_failover_enabled: Optional[StrictBool] = Field(default=None, description="Enables or disables the automatic failover of target ports to their designated partner ports", alias="portFailoverEnabled")
    r6_layout_version: Optional[StrictStr] = Field(default=None, description="RAID6 implementation version in use", alias="r6LayoutVersion")
    remote_copy_host_throttling: Optional[StrictBool] = Field(default=None, description="Enables or disables Remote Copy throttling policy for host IO replicated in asynchronous streaming mode", alias="remoteCopyHostThrottling")
    remote_sys_log: Optional[StrictInt] = Field(default=None, description="Remote Syslog Enabled/Disabled", alias="remoteSysLog")
    remote_sys_log_host: Optional[StrictStr] = Field(default=None, description="Host details for Remote Syslog", alias="remoteSysLogHost")
    remote_sys_log_security_host: Optional[StrictStr] = Field(default=None, description="Security Host details for Remote Syslog", alias="remoteSysLogSecurityHost")
    session_timeout: Optional[StrictInt] = Field(default=None, description="Idle session timeout for a CLI session", alias="sessionTimeout")
    single_lun_host: Optional[StrictBool] = Field(default=None, description="Enables or disables support to limit volume exports such that each volume can only be exported to a given host one time", alias="singleLunHost")
    ssd_raw_space_alert: Optional[StrictInt] = Field(default=None, description="SSD raw space alert setting in MiB", alias="ssdRawSpaceAlert")
    thermal_shutdown: Optional[StrictBool] = Field(default=None, description="Enables or disables a system shutdown when the temperature gets too hot", alias="thermalShutdown")
    __properties: ClassVar[List[str]] = ["ServiceProcessorCookie", "allowDomainUsersAffectNoDomain", "allowSSZ", "allowWrtbackSingleNode", "allowWrtbackUpgrade", "autoAdmitTune", "autoExportAfterReboot", "complianceOfficerApproval", "disableChunkletInitUNMAP", "enableAIQoS", "eventLogNum", "eventLogSize", "failoverMatchedSet", "fcRawSpaceAlert", "hostDIF", "hostDIFTemplate", "maxVolumeRetention", "nlRawSpaceAlert", "overprovRatioLimit", "overprovRatioWarning", "personaProfile", "portFailoverEnabled", "r6LayoutVersion", "remoteCopyHostThrottling", "remoteSysLog", "remoteSysLogHost", "remoteSysLogSecurityHost", "sessionTimeout", "singleLunHost", "ssdRawSpaceAlert", "thermalShutdown"]

    @field_validator('host_dif_template')
    def host_dif_template_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NO_HOST_DIF', 'THREEPAR_HOST_DIF', 'STD_HOST_DIF', 'HBA_HOST_DIF', 'null']):
            raise ValueError("must be one of enum values ('NO_HOST_DIF', 'THREEPAR_HOST_DIF', 'STD_HOST_DIF', 'HBA_HOST_DIF', 'null')")
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
        """Create an instance of DeviceType4parameters from a JSON string"""
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
        # set to None if service_processor_cookie (nullable) is None
        # and model_fields_set contains the field
        if self.service_processor_cookie is None and "service_processor_cookie" in self.model_fields_set:
            _dict['ServiceProcessorCookie'] = None

        # set to None if allow_domain_users_affect_no_domain (nullable) is None
        # and model_fields_set contains the field
        if self.allow_domain_users_affect_no_domain is None and "allow_domain_users_affect_no_domain" in self.model_fields_set:
            _dict['allowDomainUsersAffectNoDomain'] = None

        # set to None if allow_ssz (nullable) is None
        # and model_fields_set contains the field
        if self.allow_ssz is None and "allow_ssz" in self.model_fields_set:
            _dict['allowSSZ'] = None

        # set to None if allow_wrtback_single_node (nullable) is None
        # and model_fields_set contains the field
        if self.allow_wrtback_single_node is None and "allow_wrtback_single_node" in self.model_fields_set:
            _dict['allowWrtbackSingleNode'] = None

        # set to None if allow_wrtback_upgrade (nullable) is None
        # and model_fields_set contains the field
        if self.allow_wrtback_upgrade is None and "allow_wrtback_upgrade" in self.model_fields_set:
            _dict['allowWrtbackUpgrade'] = None

        # set to None if auto_admit_tune (nullable) is None
        # and model_fields_set contains the field
        if self.auto_admit_tune is None and "auto_admit_tune" in self.model_fields_set:
            _dict['autoAdmitTune'] = None

        # set to None if auto_export_after_reboot (nullable) is None
        # and model_fields_set contains the field
        if self.auto_export_after_reboot is None and "auto_export_after_reboot" in self.model_fields_set:
            _dict['autoExportAfterReboot'] = None

        # set to None if compliance_officer_approval (nullable) is None
        # and model_fields_set contains the field
        if self.compliance_officer_approval is None and "compliance_officer_approval" in self.model_fields_set:
            _dict['complianceOfficerApproval'] = None

        # set to None if disable_chunklet_init_unmap (nullable) is None
        # and model_fields_set contains the field
        if self.disable_chunklet_init_unmap is None and "disable_chunklet_init_unmap" in self.model_fields_set:
            _dict['disableChunkletInitUNMAP'] = None

        # set to None if enable_aiqo_s (nullable) is None
        # and model_fields_set contains the field
        if self.enable_aiqo_s is None and "enable_aiqo_s" in self.model_fields_set:
            _dict['enableAIQoS'] = None

        # set to None if event_log_num (nullable) is None
        # and model_fields_set contains the field
        if self.event_log_num is None and "event_log_num" in self.model_fields_set:
            _dict['eventLogNum'] = None

        # set to None if event_log_size (nullable) is None
        # and model_fields_set contains the field
        if self.event_log_size is None and "event_log_size" in self.model_fields_set:
            _dict['eventLogSize'] = None

        # set to None if failover_matched_set (nullable) is None
        # and model_fields_set contains the field
        if self.failover_matched_set is None and "failover_matched_set" in self.model_fields_set:
            _dict['failoverMatchedSet'] = None

        # set to None if fc_raw_space_alert (nullable) is None
        # and model_fields_set contains the field
        if self.fc_raw_space_alert is None and "fc_raw_space_alert" in self.model_fields_set:
            _dict['fcRawSpaceAlert'] = None

        # set to None if host_dif (nullable) is None
        # and model_fields_set contains the field
        if self.host_dif is None and "host_dif" in self.model_fields_set:
            _dict['hostDIF'] = None

        # set to None if host_dif_template (nullable) is None
        # and model_fields_set contains the field
        if self.host_dif_template is None and "host_dif_template" in self.model_fields_set:
            _dict['hostDIFTemplate'] = None

        # set to None if max_volume_retention (nullable) is None
        # and model_fields_set contains the field
        if self.max_volume_retention is None and "max_volume_retention" in self.model_fields_set:
            _dict['maxVolumeRetention'] = None

        # set to None if nl_raw_space_alert (nullable) is None
        # and model_fields_set contains the field
        if self.nl_raw_space_alert is None and "nl_raw_space_alert" in self.model_fields_set:
            _dict['nlRawSpaceAlert'] = None

        # set to None if overprov_ratio_limit (nullable) is None
        # and model_fields_set contains the field
        if self.overprov_ratio_limit is None and "overprov_ratio_limit" in self.model_fields_set:
            _dict['overprovRatioLimit'] = None

        # set to None if overprov_ratio_warning (nullable) is None
        # and model_fields_set contains the field
        if self.overprov_ratio_warning is None and "overprov_ratio_warning" in self.model_fields_set:
            _dict['overprovRatioWarning'] = None

        # set to None if persona_profile (nullable) is None
        # and model_fields_set contains the field
        if self.persona_profile is None and "persona_profile" in self.model_fields_set:
            _dict['personaProfile'] = None

        # set to None if port_failover_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.port_failover_enabled is None and "port_failover_enabled" in self.model_fields_set:
            _dict['portFailoverEnabled'] = None

        # set to None if r6_layout_version (nullable) is None
        # and model_fields_set contains the field
        if self.r6_layout_version is None and "r6_layout_version" in self.model_fields_set:
            _dict['r6LayoutVersion'] = None

        # set to None if remote_copy_host_throttling (nullable) is None
        # and model_fields_set contains the field
        if self.remote_copy_host_throttling is None and "remote_copy_host_throttling" in self.model_fields_set:
            _dict['remoteCopyHostThrottling'] = None

        # set to None if remote_sys_log (nullable) is None
        # and model_fields_set contains the field
        if self.remote_sys_log is None and "remote_sys_log" in self.model_fields_set:
            _dict['remoteSysLog'] = None

        # set to None if remote_sys_log_host (nullable) is None
        # and model_fields_set contains the field
        if self.remote_sys_log_host is None and "remote_sys_log_host" in self.model_fields_set:
            _dict['remoteSysLogHost'] = None

        # set to None if remote_sys_log_security_host (nullable) is None
        # and model_fields_set contains the field
        if self.remote_sys_log_security_host is None and "remote_sys_log_security_host" in self.model_fields_set:
            _dict['remoteSysLogSecurityHost'] = None

        # set to None if session_timeout (nullable) is None
        # and model_fields_set contains the field
        if self.session_timeout is None and "session_timeout" in self.model_fields_set:
            _dict['sessionTimeout'] = None

        # set to None if single_lun_host (nullable) is None
        # and model_fields_set contains the field
        if self.single_lun_host is None and "single_lun_host" in self.model_fields_set:
            _dict['singleLunHost'] = None

        # set to None if ssd_raw_space_alert (nullable) is None
        # and model_fields_set contains the field
        if self.ssd_raw_space_alert is None and "ssd_raw_space_alert" in self.model_fields_set:
            _dict['ssdRawSpaceAlert'] = None

        # set to None if thermal_shutdown (nullable) is None
        # and model_fields_set contains the field
        if self.thermal_shutdown is None and "thermal_shutdown" in self.model_fields_set:
            _dict['thermalShutdown'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4parameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ServiceProcessorCookie": obj.get("ServiceProcessorCookie"),
            "allowDomainUsersAffectNoDomain": obj.get("allowDomainUsersAffectNoDomain"),
            "allowSSZ": obj.get("allowSSZ"),
            "allowWrtbackSingleNode": obj.get("allowWrtbackSingleNode"),
            "allowWrtbackUpgrade": obj.get("allowWrtbackUpgrade"),
            "autoAdmitTune": obj.get("autoAdmitTune"),
            "autoExportAfterReboot": obj.get("autoExportAfterReboot"),
            "complianceOfficerApproval": obj.get("complianceOfficerApproval"),
            "disableChunkletInitUNMAP": obj.get("disableChunkletInitUNMAP"),
            "enableAIQoS": obj.get("enableAIQoS"),
            "eventLogNum": obj.get("eventLogNum"),
            "eventLogSize": obj.get("eventLogSize"),
            "failoverMatchedSet": obj.get("failoverMatchedSet"),
            "fcRawSpaceAlert": obj.get("fcRawSpaceAlert"),
            "hostDIF": obj.get("hostDIF"),
            "hostDIFTemplate": obj.get("hostDIFTemplate"),
            "maxVolumeRetention": obj.get("maxVolumeRetention"),
            "nlRawSpaceAlert": obj.get("nlRawSpaceAlert"),
            "overprovRatioLimit": obj.get("overprovRatioLimit"),
            "overprovRatioWarning": obj.get("overprovRatioWarning"),
            "personaProfile": obj.get("personaProfile"),
            "portFailoverEnabled": obj.get("portFailoverEnabled"),
            "r6LayoutVersion": obj.get("r6LayoutVersion"),
            "remoteCopyHostThrottling": obj.get("remoteCopyHostThrottling"),
            "remoteSysLog": obj.get("remoteSysLog"),
            "remoteSysLogHost": obj.get("remoteSysLogHost"),
            "remoteSysLogSecurityHost": obj.get("remoteSysLogSecurityHost"),
            "sessionTimeout": obj.get("sessionTimeout"),
            "singleLunHost": obj.get("singleLunHost"),
            "ssdRawSpaceAlert": obj.get("ssdRawSpaceAlert"),
            "thermalShutdown": obj.get("thermalShutdown")
        })
        return _obj


