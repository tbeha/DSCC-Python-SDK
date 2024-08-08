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
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4ModifyProtectionScheduleInputSchema(BaseModel):
    """
    Protection schedule details
    """ # noqa: E501
    at_time: Optional[StrictInt] = Field(default=None, description="Time of the day when snapshot should be taken. Possible values: 0-23 If more than one snapshots in a day then untilTime specifies until what time snapshots should be taken.", alias="atTime")
    day_of_month: Optional[StrictInt] = Field(default=None, description="Day of month on which snapshot has to be taken for Monthly schedule. Possible values: 1-28", alias="dayOfMonth")
    days: Optional[StrictStr] = Field(default=None, description="Days on which snapshots should be taken. comma separated. Possible values: sunday,monday,tuesday,wednesday,thursday,friday,saturday")
    id: StrictStr = Field(description="schedule id")
    is_remote: StrictBool = Field(description="Specifies that this schedule is remote protection schedule", alias="isRemote")
    name: StrictStr = Field(description="Name of the Schedule")
    period: Optional[StrictInt] = Field(default=None, description="Time interval for snapshots. Possible values:   - hours: 1,2,3,4,6,8,12   - minutes: 15,20,30   - days & months: 1")
    period_unit: Optional[StrictStr] = Field(default=None, description="Unit of time for the interval specified in period.", alias="periodUnit")
    until_time: Optional[StrictInt] = Field(default=None, description="Time of the day to stop taking snapshots. Must be an incremental value by the factor specified in Period, starting from atTime. Applicable only when more than one snapshots should be taken in a day.", alias="untilTime")
    __properties: ClassVar[List[str]] = ["atTime", "dayOfMonth", "days", "id", "isRemote", "name", "period", "periodUnit", "untilTime"]

    @field_validator('period_unit')
    def period_unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['minutes', 'hours', 'days', 'months']):
            raise ValueError("must be one of enum values ('minutes', 'hours', 'days', 'months')")
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
        """Create an instance of DeviceType4ModifyProtectionScheduleInputSchema from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4ModifyProtectionScheduleInputSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "atTime": obj.get("atTime"),
            "dayOfMonth": obj.get("dayOfMonth"),
            "days": obj.get("days"),
            "id": obj.get("id"),
            "isRemote": obj.get("isRemote"),
            "name": obj.get("name"),
            "period": obj.get("period"),
            "periodUnit": obj.get("periodUnit"),
            "untilTime": obj.get("untilTime")
        })
        return _obj


