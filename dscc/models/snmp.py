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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Snmp(BaseModel):
    """
    SNMP manager details for a device
    """ # noqa: E501
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="The customer application identifier", alias="customerId")
    generation: Optional[StrictInt] = Field(default=None, description="A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.")
    id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the resource")
    manager_ip: Optional[StrictStr] = Field(default=None, description="Specify the IP address of the host from which the manager runs", alias="managerIP")
    notify: Optional[StrictStr] = Field(default=None, description="Indicates the trap notification types defined by the HPE deviceType1 MIB")
    port: Optional[StrictInt] = Field(default=None, description="Specify the port number where the SNMP manager receives traps")
    system_id: Optional[StrictStr] = Field(default=None, description="SystemId of the storage system", alias="systemId")
    system_wwn: Optional[StrictStr] = Field(default=None, description="WWN of the array", alias="systemWWN")
    type: Optional[StrictStr] = Field(default=None, description="The type of resource.")
    user: Optional[StrictStr] = Field(default=None, description="Specify the SNMPv3 user name")
    version: Optional[StrictInt] = Field(default=None, description="Specify the SNMP version supported")
    __properties: ClassVar[List[str]] = ["consoleUri", "customerId", "generation", "id", "managerIP", "notify", "port", "systemId", "systemWWN", "type", "user", "version"]

    @field_validator('notify')
    def notify_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ALL', 'NODUP', 'STANDARD']):
            raise ValueError("must be one of enum values ('ALL', 'NODUP', 'STANDARD')")
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
        """Create an instance of Snmp from a JSON string"""
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
        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if manager_ip (nullable) is None
        # and model_fields_set contains the field
        if self.manager_ip is None and "manager_ip" in self.model_fields_set:
            _dict['managerIP'] = None

        # set to None if notify (nullable) is None
        # and model_fields_set contains the field
        if self.notify is None and "notify" in self.model_fields_set:
            _dict['notify'] = None

        # set to None if port (nullable) is None
        # and model_fields_set contains the field
        if self.port is None and "port" in self.model_fields_set:
            _dict['port'] = None

        # set to None if system_id (nullable) is None
        # and model_fields_set contains the field
        if self.system_id is None and "system_id" in self.model_fields_set:
            _dict['systemId'] = None

        # set to None if system_wwn (nullable) is None
        # and model_fields_set contains the field
        if self.system_wwn is None and "system_wwn" in self.model_fields_set:
            _dict['systemWWN'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Snmp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "managerIP": obj.get("managerIP"),
            "notify": obj.get("notify"),
            "port": obj.get("port"),
            "systemId": obj.get("systemId"),
            "systemWWN": obj.get("systemWWN"),
            "type": obj.get("type"),
            "user": obj.get("user"),
            "version": obj.get("version")
        })
        return _obj


