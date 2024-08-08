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
from dscc.models.friendly_cert import FriendlyCert
from dscc.models.primera_common_resource_attributes import PrimeraCommonResourceAttributes
from dscc.models.vcenter_status import VcenterStatus
from typing import Optional, Set
from typing_extensions import Self

class VcenterSettingDetailList(BaseModel):
    """
    Vcenter settings for the system
    """ # noqa: E501
    common_resource_attributes: Optional[PrimeraCommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="The customer application identifier", alias="customerId")
    description: Optional[StrictStr] = Field(default=None, description="Vcenter description")
    friendly_cert: Optional[FriendlyCert] = Field(default=None, alias="friendlyCert")
    generation: Optional[StrictInt] = Field(default=None, description="A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.")
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the vcenter settings.")
    inetaddress: Optional[StrictStr] = Field(default=None, description="Address of the vcenter.")
    name: Optional[StrictStr] = Field(default=None, description="Name of vcenter.")
    port: Optional[StrictInt] = Field(default=None, description="port number of vcenter.")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed vcenter setting object", alias="resourceUri")
    status: Optional[VcenterStatus] = None
    system_id: Optional[StrictStr] = Field(default=None, description="SystemID of the array", alias="systemId")
    type: Optional[StrictStr] = Field(default=None, description="The type of resource.")
    username: Optional[StrictStr] = Field(default=None, description="User of the vcenter configured")
    vm_manager_type: Optional[StrictStr] = Field(default=None, description="Type of the vmmanager settings.", alias="vmManagerType")
    __properties: ClassVar[List[str]] = ["commonResourceAttributes", "consoleUri", "customerId", "description", "friendlyCert", "generation", "id", "inetaddress", "name", "port", "resourceUri", "status", "systemId", "type", "username", "vmManagerType"]

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
        """Create an instance of VcenterSettingDetailList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of friendly_cert
        if self.friendly_cert:
            _dict['friendlyCert'] = self.friendly_cert.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if friendly_cert (nullable) is None
        # and model_fields_set contains the field
        if self.friendly_cert is None and "friendly_cert" in self.model_fields_set:
            _dict['friendlyCert'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if inetaddress (nullable) is None
        # and model_fields_set contains the field
        if self.inetaddress is None and "inetaddress" in self.model_fields_set:
            _dict['inetaddress'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if port (nullable) is None
        # and model_fields_set contains the field
        if self.port is None and "port" in self.model_fields_set:
            _dict['port'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        # set to None if vm_manager_type (nullable) is None
        # and model_fields_set contains the field
        if self.vm_manager_type is None and "vm_manager_type" in self.model_fields_set:
            _dict['vmManagerType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VcenterSettingDetailList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "commonResourceAttributes": PrimeraCommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "description": obj.get("description"),
            "friendlyCert": FriendlyCert.from_dict(obj["friendlyCert"]) if obj.get("friendlyCert") is not None else None,
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "inetaddress": obj.get("inetaddress"),
            "name": obj.get("name"),
            "port": obj.get("port"),
            "resourceUri": obj.get("resourceUri"),
            "status": VcenterStatus.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "systemId": obj.get("systemId"),
            "type": obj.get("type"),
            "username": obj.get("username"),
            "vmManagerType": obj.get("vmManagerType")
        })
        return _obj


