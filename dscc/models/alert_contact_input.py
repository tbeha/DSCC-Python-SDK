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

class AlertContactInput(BaseModel):
    """
    AlertContactInput
    """ # noqa: E501
    company: Optional[StrictStr] = Field(default=None, description="Company")
    company_code: Optional[StrictStr] = Field(default=None, description="Company code", alias="companyCode")
    country: Optional[StrictStr] = Field(default=None, description="Country")
    fax: Optional[StrictStr] = Field(default=None, description="Fax number")
    first_name: Optional[StrictStr] = Field(default=None, description="First name", alias="firstName")
    include_svc_alerts: Optional[StrictBool] = Field(default=None, description="Email sent to contact shall include service alert", alias="includeSvcAlerts")
    last_name: Optional[StrictStr] = Field(default=None, description="Last name", alias="lastName")
    notification_severities: Optional[List[StrictInt]] = Field(default=None, description="Severities of notifications the contact will be notificated. An array of number: 0 - Fatal, 1 - Critical, 2 - Major, 3 - Minor, 4 - Degraded, 5 - Info, 6 - Debug", alias="notificationSeverities")
    preferred_language: Optional[StrictStr] = Field(default=None, description="Preferred language when being contacted or emailed", alias="preferredLanguage")
    primary_email: Optional[StrictStr] = Field(default=None, description="Primary email address", alias="primaryEmail")
    primary_phone: Optional[StrictStr] = Field(default=None, description="Primary phone", alias="primaryPhone")
    receive_email: Optional[StrictBool] = Field(default=None, description="Contact will receive email notifications. This is a deprecated field and will always pass true to be inline with UI.", alias="receiveEmail")
    receive_grouped: Optional[StrictBool] = Field(default=None, description="Contact will receive grouped low urgency email notifications", alias="receiveGrouped")
    secondary_email: Optional[StrictStr] = Field(default=None, description="Secondary email address", alias="secondaryEmail")
    secondary_phone: Optional[StrictStr] = Field(default=None, description="Secondary phone", alias="secondaryPhone")
    __properties: ClassVar[List[str]] = ["company", "companyCode", "country", "fax", "firstName", "includeSvcAlerts", "lastName", "notificationSeverities", "preferredLanguage", "primaryEmail", "primaryPhone", "receiveEmail", "receiveGrouped", "secondaryEmail", "secondaryPhone"]

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
        """Create an instance of AlertContactInput from a JSON string"""
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
        # set to None if company (nullable) is None
        # and model_fields_set contains the field
        if self.company is None and "company" in self.model_fields_set:
            _dict['company'] = None

        # set to None if company_code (nullable) is None
        # and model_fields_set contains the field
        if self.company_code is None and "company_code" in self.model_fields_set:
            _dict['companyCode'] = None

        # set to None if country (nullable) is None
        # and model_fields_set contains the field
        if self.country is None and "country" in self.model_fields_set:
            _dict['country'] = None

        # set to None if fax (nullable) is None
        # and model_fields_set contains the field
        if self.fax is None and "fax" in self.model_fields_set:
            _dict['fax'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['firstName'] = None

        # set to None if include_svc_alerts (nullable) is None
        # and model_fields_set contains the field
        if self.include_svc_alerts is None and "include_svc_alerts" in self.model_fields_set:
            _dict['includeSvcAlerts'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['lastName'] = None

        # set to None if notification_severities (nullable) is None
        # and model_fields_set contains the field
        if self.notification_severities is None and "notification_severities" in self.model_fields_set:
            _dict['notificationSeverities'] = None

        # set to None if preferred_language (nullable) is None
        # and model_fields_set contains the field
        if self.preferred_language is None and "preferred_language" in self.model_fields_set:
            _dict['preferredLanguage'] = None

        # set to None if primary_email (nullable) is None
        # and model_fields_set contains the field
        if self.primary_email is None and "primary_email" in self.model_fields_set:
            _dict['primaryEmail'] = None

        # set to None if primary_phone (nullable) is None
        # and model_fields_set contains the field
        if self.primary_phone is None and "primary_phone" in self.model_fields_set:
            _dict['primaryPhone'] = None

        # set to None if receive_email (nullable) is None
        # and model_fields_set contains the field
        if self.receive_email is None and "receive_email" in self.model_fields_set:
            _dict['receiveEmail'] = None

        # set to None if receive_grouped (nullable) is None
        # and model_fields_set contains the field
        if self.receive_grouped is None and "receive_grouped" in self.model_fields_set:
            _dict['receiveGrouped'] = None

        # set to None if secondary_email (nullable) is None
        # and model_fields_set contains the field
        if self.secondary_email is None and "secondary_email" in self.model_fields_set:
            _dict['secondaryEmail'] = None

        # set to None if secondary_phone (nullable) is None
        # and model_fields_set contains the field
        if self.secondary_phone is None and "secondary_phone" in self.model_fields_set:
            _dict['secondaryPhone'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlertContactInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "company": obj.get("company"),
            "companyCode": obj.get("companyCode"),
            "country": obj.get("country"),
            "fax": obj.get("fax"),
            "firstName": obj.get("firstName"),
            "includeSvcAlerts": obj.get("includeSvcAlerts"),
            "lastName": obj.get("lastName"),
            "notificationSeverities": obj.get("notificationSeverities"),
            "preferredLanguage": obj.get("preferredLanguage"),
            "primaryEmail": obj.get("primaryEmail"),
            "primaryPhone": obj.get("primaryPhone"),
            "receiveEmail": obj.get("receiveEmail"),
            "receiveGrouped": obj.get("receiveGrouped"),
            "secondaryEmail": obj.get("secondaryEmail"),
            "secondaryPhone": obj.get("secondaryPhone")
        })
        return _obj


