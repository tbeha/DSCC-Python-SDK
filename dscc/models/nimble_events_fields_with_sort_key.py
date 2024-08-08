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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class NimbleEventsFieldsWithSortKey(BaseModel):
    """
    NimbleEventsFieldsWithSortKey
    """ # noqa: E501
    alarm_id: Optional[StrictStr] = Field(default=None, description="The alarm ID if the event is related to an alarm. A 42 digit hexadecimal number. `Filter, Sort`")
    category: Optional[StrictStr] = Field(default=None, description="Category of the event record. Possible values: 'unknown', 'hardware', 'service', 'replication', 'volume', 'update', 'configuration', 'test', 'security', 'array_upgrade'. `Filter, Sort`")
    event_type: Optional[StrictInt] = Field(default=None, description="FType of the event record. Non-negative integer in range [0,2147483647]. `Filter, Sort`")
    id: Optional[StrictStr] = Field(default=None, description="Identifier for the event record. A 42 digit hexadecimal number. `Filter, Sort`")
    scope: Optional[StrictStr] = Field(default=None, description="The array name for array level event. Possible values: array serial number, or '-'. `Filter, Sort`")
    severity: Optional[StrictStr] = Field(default=None, description="Severity level of the event. Possible values: 'info', 'notice', 'warning', 'critical'. `Filter, Sort`")
    target: Optional[StrictStr] = Field(default=None, description="Name of object upon which the event occurred. String of up to 400 alphanumeric characters, - and . and : and \" \" are allowed after first character. `Filter, Sort`")
    target_type: Optional[StrictStr] = Field(default=None, description="Target type of the event record. Possible values: 'anon', 'array', 'controller', 'disk', 'nic', 'temperature', 'service', 'volume', 'protection_set', 'nvram', 'fan', 'power_supply', 'partner', 'raid', 'test', 'iscsi', 'pool', 'group', 'shelf', 'ntb', 'fc', 'initiator_group'. `Filter, Sort`")
    timestamp: Optional[StrictInt] = Field(default=None, description="Time when this event happened. Seconds since last epoch i.e. 00:00 January 1, 1970. `Filter, Sort`")
    __properties: ClassVar[List[str]] = ["alarm_id", "category", "event_type", "id", "scope", "severity", "target", "target_type", "timestamp"]

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
        """Create an instance of NimbleEventsFieldsWithSortKey from a JSON string"""
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
        # set to None if alarm_id (nullable) is None
        # and model_fields_set contains the field
        if self.alarm_id is None and "alarm_id" in self.model_fields_set:
            _dict['alarm_id'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if event_type (nullable) is None
        # and model_fields_set contains the field
        if self.event_type is None and "event_type" in self.model_fields_set:
            _dict['event_type'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if scope (nullable) is None
        # and model_fields_set contains the field
        if self.scope is None and "scope" in self.model_fields_set:
            _dict['scope'] = None

        # set to None if severity (nullable) is None
        # and model_fields_set contains the field
        if self.severity is None and "severity" in self.model_fields_set:
            _dict['severity'] = None

        # set to None if target (nullable) is None
        # and model_fields_set contains the field
        if self.target is None and "target" in self.model_fields_set:
            _dict['target'] = None

        # set to None if target_type (nullable) is None
        # and model_fields_set contains the field
        if self.target_type is None and "target_type" in self.model_fields_set:
            _dict['target_type'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleEventsFieldsWithSortKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alarm_id": obj.get("alarm_id"),
            "category": obj.get("category"),
            "event_type": obj.get("event_type"),
            "id": obj.get("id"),
            "scope": obj.get("scope"),
            "severity": obj.get("severity"),
            "target": obj.get("target"),
            "target_type": obj.get("target_type"),
            "timestamp": obj.get("timestamp")
        })
        return _obj


