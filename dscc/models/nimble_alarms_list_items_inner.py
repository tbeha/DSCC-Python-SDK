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
from dscc.models.associated_links_inner import AssociatedLinksInner
from dscc.models.nimble_common_resource_attributes import NimbleCommonResourceAttributes
from typing import Optional, Set
from typing_extensions import Self

class NimbleAlarmsListItemsInner(BaseModel):
    """
    NimbleAlarmsListItemsInner
    """ # noqa: E501
    ack_time: Optional[StrictInt] = Field(default=None, description="Time when this alarm was acknowledged. Seconds since last epoch i.e. 00:00 January 1, 1970. `Filter, Sort`")
    activity: Optional[StrictStr] = Field(default=None, description="Description of the alarms. String of 1-1476 printable characters.")
    array: Optional[StrictStr] = Field(default=None, description="The array name where the alarm is generated.  Possible values: array serial number, or '-'. `Filter, Sort`")
    category: Optional[StrictStr] = Field(default=None, description="Category of the alarm. Possible values: 'unknown', 'hardware', 'service', 'replication', 'volume', 'update', 'configuration', 'test', 'security', 'array_upgrade',cloud_console `Filter, Sort`")
    curr_onset_event_id: Optional[StrictStr] = Field(default=None, description="Identifier for the current onset event. A 42 digit hexadecimal number. `Filter, Sort`")
    id: Optional[StrictStr] = Field(default=None, description="Identifier for the alarm record. A 42 digit hexadecimal number. `Filter, Sort`")
    next_notification_time: Optional[StrictInt] = Field(default=None, description="Time when next reminder for the alarm will be sent. Signed 64-bit integer. `Filter, Sort`")
    object_id: Optional[StrictStr] = Field(default=None, description="Identifier of object operated upon. A 42 digit hexadecimal number.  `Filter, Sort`")
    object_name: Optional[StrictStr] = Field(default=None, description="Name of object operated upon. String of up to 400 alphanumeric characters, - and . and : and \" \" are allowed after first character.  `Filter, Sort`")
    object_type: Optional[StrictStr] = Field(default=None, description="Type of the object being operated upon. Possible values: 'active_directory', 'group', 'chapuser', 'initiatorgrp', 'perfpolicy', 'snapshot', 'snapcoll', 'vol', 'volcoll', 'partner', 'array', 'pool', 'initiator', 'protsched', 'volacl', 'throttle', 'sshkey', 'user', 'protpol', 'prottmpl', 'branch', 'route', 'role', 'privilege', 'netconfig', 'events', 'session', 'subnet', 'array_netconfig', 'nic', 'initiatorgrp_subnet', 'fc_initiator_alias', 'fc_port', 'fc_interface_collection', 'fc', 'event_dipatcher', 'fc_target_port_group', 'encrypt_key', 'encrypt_config', 'snapshot_lun', 'syslog', 'async_job', 'application_server', 'audit_log', 'ip address', 'disk', 'shelf', 'protocol_endpoint', 'folder', 'pe_acl', 'vvol', 'vvol_acl', 'alarm' ,'folset','hc_cluster_config','user group', 'user_policy', 'witness', 'support', 'keymanager', 'trusted_oauth_issuer', 'client_credential'. `Filter, Sort`")
    onset_time: Optional[StrictInt] = Field(default=None, description="Time when this alarm was triggered. Seconds since last epoch i.e. 00:00 January 1, 1970. `Filter, Sort`")
    remind_every: Optional[StrictInt] = Field(default=None, description="Frequency of notification. This number and the remind_every_unit define how frequent one alarm notification is sent. `Filter, Sort`")
    remind_every_unit: Optional[StrictStr] = Field(default=None, description="Time unit over which to send the number of notification specified in 'remind_every'. For example, a value of 'days' with a 'remind_every' of '1' results in one notification every day. Possible values: 'minutes', 'hours', 'days', 'weeks'. `Filter, Sort`")
    severity: Optional[StrictStr] = Field(default=None, description="Severity level of the event. Possible values: 'warning', 'critical'. `Filter, Sort`")
    status: Optional[StrictStr] = Field(default=None, description="Status of the operation -- open or acknowledged. Possible values: 'open', 'acknowledged'. `Filter, Sort`")
    user_full_name: Optional[StrictStr] = Field(default=None, description="Full name of the user who acknowledged the alarm. Alphanumeric string of up to 64 chars, starts with letter, can include space, apostrophe('), hyphen(-). `Filter, Sort`")
    user_id: Optional[StrictStr] = Field(default=None, description="Identifier of the user who acknowledged the alarm. A 42 digit hexadecimal number.  `Filter, Sort`")
    user_name: Optional[StrictStr] = Field(default=None, description="Username of the user who acknowledged the alarm. String of up to 80 alphanumeric characters, beginning with a letter. For Active Directory users, it can include backslash (\\), dash (-), period (.), underscore (_) and space.  `Filter, Sort`")
    alarm_type: Optional[StrictInt] = Field(default=None, description="Identifier for type of alarm. Non-negative integer in range [0,2147483647].")
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details")
    common_resource_attributes: Optional[NimbleCommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    resource_uri: Optional[StrictStr] = Field(default=None, description="Link to the object URI", alias="resourceUri")
    summary: Optional[StrictStr] = Field(default=None, description="Summary of the alarm. Plain string.")
    type: Optional[StrictStr] = Field(default=None, description="type")
    __properties: ClassVar[List[str]] = ["ack_time", "activity", "array", "category", "curr_onset_event_id", "id", "next_notification_time", "object_id", "object_name", "object_type", "onset_time", "remind_every", "remind_every_unit", "severity", "status", "user_full_name", "user_id", "user_name", "alarm_type", "associated_links", "commonResourceAttributes", "consoleUri", "customerId", "generation", "resourceUri", "summary", "type"]

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
        """Create an instance of NimbleAlarmsListItemsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in associated_links (list)
        _items = []
        if self.associated_links:
            for _item in self.associated_links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['associated_links'] = _items
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # set to None if ack_time (nullable) is None
        # and model_fields_set contains the field
        if self.ack_time is None and "ack_time" in self.model_fields_set:
            _dict['ack_time'] = None

        # set to None if activity (nullable) is None
        # and model_fields_set contains the field
        if self.activity is None and "activity" in self.model_fields_set:
            _dict['activity'] = None

        # set to None if array (nullable) is None
        # and model_fields_set contains the field
        if self.array is None and "array" in self.model_fields_set:
            _dict['array'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if curr_onset_event_id (nullable) is None
        # and model_fields_set contains the field
        if self.curr_onset_event_id is None and "curr_onset_event_id" in self.model_fields_set:
            _dict['curr_onset_event_id'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if next_notification_time (nullable) is None
        # and model_fields_set contains the field
        if self.next_notification_time is None and "next_notification_time" in self.model_fields_set:
            _dict['next_notification_time'] = None

        # set to None if object_id (nullable) is None
        # and model_fields_set contains the field
        if self.object_id is None and "object_id" in self.model_fields_set:
            _dict['object_id'] = None

        # set to None if object_name (nullable) is None
        # and model_fields_set contains the field
        if self.object_name is None and "object_name" in self.model_fields_set:
            _dict['object_name'] = None

        # set to None if object_type (nullable) is None
        # and model_fields_set contains the field
        if self.object_type is None and "object_type" in self.model_fields_set:
            _dict['object_type'] = None

        # set to None if onset_time (nullable) is None
        # and model_fields_set contains the field
        if self.onset_time is None and "onset_time" in self.model_fields_set:
            _dict['onset_time'] = None

        # set to None if remind_every (nullable) is None
        # and model_fields_set contains the field
        if self.remind_every is None and "remind_every" in self.model_fields_set:
            _dict['remind_every'] = None

        # set to None if remind_every_unit (nullable) is None
        # and model_fields_set contains the field
        if self.remind_every_unit is None and "remind_every_unit" in self.model_fields_set:
            _dict['remind_every_unit'] = None

        # set to None if severity (nullable) is None
        # and model_fields_set contains the field
        if self.severity is None and "severity" in self.model_fields_set:
            _dict['severity'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if user_full_name (nullable) is None
        # and model_fields_set contains the field
        if self.user_full_name is None and "user_full_name" in self.model_fields_set:
            _dict['user_full_name'] = None

        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['user_id'] = None

        # set to None if user_name (nullable) is None
        # and model_fields_set contains the field
        if self.user_name is None and "user_name" in self.model_fields_set:
            _dict['user_name'] = None

        # set to None if alarm_type (nullable) is None
        # and model_fields_set contains the field
        if self.alarm_type is None and "alarm_type" in self.model_fields_set:
            _dict['alarm_type'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if summary (nullable) is None
        # and model_fields_set contains the field
        if self.summary is None and "summary" in self.model_fields_set:
            _dict['summary'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleAlarmsListItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ack_time": obj.get("ack_time"),
            "activity": obj.get("activity"),
            "array": obj.get("array"),
            "category": obj.get("category"),
            "curr_onset_event_id": obj.get("curr_onset_event_id"),
            "id": obj.get("id"),
            "next_notification_time": obj.get("next_notification_time"),
            "object_id": obj.get("object_id"),
            "object_name": obj.get("object_name"),
            "object_type": obj.get("object_type"),
            "onset_time": obj.get("onset_time"),
            "remind_every": obj.get("remind_every"),
            "remind_every_unit": obj.get("remind_every_unit"),
            "severity": obj.get("severity"),
            "status": obj.get("status"),
            "user_full_name": obj.get("user_full_name"),
            "user_id": obj.get("user_id"),
            "user_name": obj.get("user_name"),
            "alarm_type": obj.get("alarm_type"),
            "associated_links": [AssociatedLinksInner.from_dict(_item) for _item in obj["associated_links"]] if obj.get("associated_links") is not None else None,
            "commonResourceAttributes": NimbleCommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "generation": obj.get("generation"),
            "resourceUri": obj.get("resourceUri"),
            "summary": obj.get("summary"),
            "type": obj.get("type")
        })
        return _obj


