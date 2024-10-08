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
from dscc.models.device_type4_contacts_edit_details import DeviceType4ContactsEditDetails
from dscc.models.device_type4_system_config_params_edit_input_auth_mode import DeviceType4SystemConfigParamsEditInputAuthMode
from dscc.models.device_type4_system_config_params_edit_input_installation_sites import DeviceType4SystemConfigParamsEditInputInstallationSites
from dscc.models.device_type4_system_config_params_edit_input_remote_syslog_settings import DeviceType4SystemConfigParamsEditInputRemoteSyslogSettings
from dscc.models.device_type4_system_config_params_edit_input_srinfo import DeviceType4SystemConfigParamsEditInputSrinfo
from dscc.models.device_type4_system_config_params_edit_input_system_parameters import DeviceType4SystemConfigParamsEditInputSystemParameters
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4SystemConfigParamsEditInput(BaseModel):
    """
    DeviceType4SystemConfigParamsEditInput
    """ # noqa: E501
    auth_mode: Optional[DeviceType4SystemConfigParamsEditInputAuthMode] = Field(default=None, alias="authMode")
    date_time: Optional[StrictStr] = Field(default=None, description="system date time. timezone is mandatory to configure this parameter.", alias="dateTime")
    installation_sites: Optional[DeviceType4SystemConfigParamsEditInputInstallationSites] = Field(default=None, alias="installationSites")
    name: Optional[StrictStr] = Field(default=None, description="system name")
    ntp_addresses: Optional[List[Optional[StrictStr]]] = Field(default=None, description="system ntp addresses. timezone is mandatory to configure this parameter.", alias="ntpAddresses")
    remote_syslog_settings: Optional[DeviceType4SystemConfigParamsEditInputRemoteSyslogSettings] = Field(default=None, alias="remoteSyslogSettings")
    srinfo: Optional[DeviceType4SystemConfigParamsEditInputSrinfo] = None
    support_contact: Optional[DeviceType4ContactsEditDetails] = Field(default=None, alias="supportContact")
    system_parameters: Optional[DeviceType4SystemConfigParamsEditInputSystemParameters] = Field(default=None, alias="systemParameters")
    timezone: Optional[StrictStr] = Field(default=None, description="system time zone")
    __properties: ClassVar[List[str]] = ["authMode", "dateTime", "installationSites", "name", "ntpAddresses", "remoteSyslogSettings", "srinfo", "supportContact", "systemParameters", "timezone"]

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
        """Create an instance of DeviceType4SystemConfigParamsEditInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auth_mode
        if self.auth_mode:
            _dict['authMode'] = self.auth_mode.to_dict()
        # override the default output from pydantic by calling `to_dict()` of installation_sites
        if self.installation_sites:
            _dict['installationSites'] = self.installation_sites.to_dict()
        # override the default output from pydantic by calling `to_dict()` of remote_syslog_settings
        if self.remote_syslog_settings:
            _dict['remoteSyslogSettings'] = self.remote_syslog_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of srinfo
        if self.srinfo:
            _dict['srinfo'] = self.srinfo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of support_contact
        if self.support_contact:
            _dict['supportContact'] = self.support_contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of system_parameters
        if self.system_parameters:
            _dict['systemParameters'] = self.system_parameters.to_dict()
        # set to None if auth_mode (nullable) is None
        # and model_fields_set contains the field
        if self.auth_mode is None and "auth_mode" in self.model_fields_set:
            _dict['authMode'] = None

        # set to None if date_time (nullable) is None
        # and model_fields_set contains the field
        if self.date_time is None and "date_time" in self.model_fields_set:
            _dict['dateTime'] = None

        # set to None if installation_sites (nullable) is None
        # and model_fields_set contains the field
        if self.installation_sites is None and "installation_sites" in self.model_fields_set:
            _dict['installationSites'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if ntp_addresses (nullable) is None
        # and model_fields_set contains the field
        if self.ntp_addresses is None and "ntp_addresses" in self.model_fields_set:
            _dict['ntpAddresses'] = None

        # set to None if remote_syslog_settings (nullable) is None
        # and model_fields_set contains the field
        if self.remote_syslog_settings is None and "remote_syslog_settings" in self.model_fields_set:
            _dict['remoteSyslogSettings'] = None

        # set to None if srinfo (nullable) is None
        # and model_fields_set contains the field
        if self.srinfo is None and "srinfo" in self.model_fields_set:
            _dict['srinfo'] = None

        # set to None if support_contact (nullable) is None
        # and model_fields_set contains the field
        if self.support_contact is None and "support_contact" in self.model_fields_set:
            _dict['supportContact'] = None

        # set to None if system_parameters (nullable) is None
        # and model_fields_set contains the field
        if self.system_parameters is None and "system_parameters" in self.model_fields_set:
            _dict['systemParameters'] = None

        # set to None if timezone (nullable) is None
        # and model_fields_set contains the field
        if self.timezone is None and "timezone" in self.model_fields_set:
            _dict['timezone'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4SystemConfigParamsEditInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authMode": DeviceType4SystemConfigParamsEditInputAuthMode.from_dict(obj["authMode"]) if obj.get("authMode") is not None else None,
            "dateTime": obj.get("dateTime"),
            "installationSites": DeviceType4SystemConfigParamsEditInputInstallationSites.from_dict(obj["installationSites"]) if obj.get("installationSites") is not None else None,
            "name": obj.get("name"),
            "ntpAddresses": obj.get("ntpAddresses"),
            "remoteSyslogSettings": DeviceType4SystemConfigParamsEditInputRemoteSyslogSettings.from_dict(obj["remoteSyslogSettings"]) if obj.get("remoteSyslogSettings") is not None else None,
            "srinfo": DeviceType4SystemConfigParamsEditInputSrinfo.from_dict(obj["srinfo"]) if obj.get("srinfo") is not None else None,
            "supportContact": DeviceType4ContactsEditDetails.from_dict(obj["supportContact"]) if obj.get("supportContact") is not None else None,
            "systemParameters": DeviceType4SystemConfigParamsEditInputSystemParameters.from_dict(obj["systemParameters"]) if obj.get("systemParameters") is not None else None,
            "timezone": obj.get("timezone")
        })
        return _obj


