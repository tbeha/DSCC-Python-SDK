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
from dscc.models.common_resource_attributes import CommonResourceAttributes
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4servicePorts(BaseModel):
    """
    DeviceType4servicePorts
    """ # noqa: E501
    common_resource_attributes: Optional[CommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    domain: Optional[StrictStr] = Field(default=None, description="domain of the service port object")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    id: Optional[StrictStr] = Field(default=None, description="uid (Unique identifier) for the service port object")
    ipv4address: Optional[StrictStr] = Field(default=None, description="ipv4address of the service port object `Filter`")
    ipv4netmask: Optional[StrictStr] = Field(default=None, description="ipv4 net mask of the service port object")
    ipv6address: Optional[StrictStr] = Field(default=None, description="ipv6address of the service port object `Filter`")
    ipv6vnetmask: Optional[StrictStr] = Field(default=None, description="ipv6 net mask for the service port objectt")
    mode: Optional[StrictStr] = Field(default=None, description="mode for the service port object")
    name: Optional[StrictStr] = Field(default=None, description="display name of the service port object")
    node: Optional[StrictStr] = Field(default=None, description="node for the service port object")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed service ports object", alias="resourceUri")
    system_id: Optional[StrictStr] = Field(default=None, description="SystemUid/serialNumber of the array.", alias="systemId")
    type: Optional[StrictStr] = Field(default=None, description="type")
    __properties: ClassVar[List[str]] = ["commonResourceAttributes", "customerId", "domain", "generation", "id", "ipv4address", "ipv4netmask", "ipv6address", "ipv6vnetmask", "mode", "name", "node", "resourceUri", "systemId", "type"]

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
        """Create an instance of DeviceType4servicePorts from a JSON string"""
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
        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if ipv4address (nullable) is None
        # and model_fields_set contains the field
        if self.ipv4address is None and "ipv4address" in self.model_fields_set:
            _dict['ipv4address'] = None

        # set to None if ipv4netmask (nullable) is None
        # and model_fields_set contains the field
        if self.ipv4netmask is None and "ipv4netmask" in self.model_fields_set:
            _dict['ipv4netmask'] = None

        # set to None if ipv6address (nullable) is None
        # and model_fields_set contains the field
        if self.ipv6address is None and "ipv6address" in self.model_fields_set:
            _dict['ipv6address'] = None

        # set to None if ipv6vnetmask (nullable) is None
        # and model_fields_set contains the field
        if self.ipv6vnetmask is None and "ipv6vnetmask" in self.model_fields_set:
            _dict['ipv6vnetmask'] = None

        # set to None if mode (nullable) is None
        # and model_fields_set contains the field
        if self.mode is None and "mode" in self.model_fields_set:
            _dict['mode'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if node (nullable) is None
        # and model_fields_set contains the field
        if self.node is None and "node" in self.model_fields_set:
            _dict['node'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if system_id (nullable) is None
        # and model_fields_set contains the field
        if self.system_id is None and "system_id" in self.model_fields_set:
            _dict['systemId'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4servicePorts from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "commonResourceAttributes": CommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "customerId": obj.get("customerId"),
            "domain": obj.get("domain"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "ipv4address": obj.get("ipv4address"),
            "ipv4netmask": obj.get("ipv4netmask"),
            "ipv6address": obj.get("ipv6address"),
            "ipv6vnetmask": obj.get("ipv6vnetmask"),
            "mode": obj.get("mode"),
            "name": obj.get("name"),
            "node": obj.get("node"),
            "resourceUri": obj.get("resourceUri"),
            "systemId": obj.get("systemId"),
            "type": obj.get("type")
        })
        return _obj


