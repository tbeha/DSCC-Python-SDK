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
from dscc.models.cert_mgmt import CertMgmt
from dscc.models.vasa_uri_info import VasaUriInfo
from typing import Optional, Set
from typing_extensions import Self

class Vasa(BaseModel):
    """
    Vasa service details for a device
    """ # noqa: E501
    cert_mgmt: Optional[CertMgmt] = Field(default=None, alias="certMgmt")
    cert_subject: Optional[StrictStr] = Field(default=None, description="Certificate subject of the VASA Provider", alias="certSubject")
    cert_thumbprint: Optional[StrictStr] = Field(default=None, description="Certificate thumbprint of the VASA Provider", alias="certThumbprint")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="The customer application identifier", alias="customerId")
    enabled: Optional[StrictBool] = Field(default=None, description="Indicates if the service status is enabled or not")
    generation: Optional[StrictInt] = Field(default=None, description="A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.")
    https_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if the vasa https state is enabled or not", alias="httpsEnabled")
    https_port: Optional[StrictInt] = Field(default=None, description="Vasa https port number", alias="httpsPort")
    id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the resource")
    mem_usage_mi_b: Optional[StrictInt] = Field(default=None, description="Memory usage of the VASA provider", alias="memUsageMiB")
    more_uris: Optional[List[Optional[VasaUriInfo]]] = Field(default=None, description="List of VASA Service URLs ", alias="moreUris")
    server_name: Optional[StrictStr] = Field(default=None, description="Name of the vasa server", alias="serverName")
    system_id: Optional[StrictStr] = Field(default=None, description="SystemId of the storage system", alias="systemId")
    system_wwn: Optional[StrictStr] = Field(default=None, description="WWN of the array", alias="systemWWN")
    type: Optional[StrictStr] = Field(default=None, description="The type of resource.")
    version: Optional[StrictStr] = Field(default=None, description="Version of the VASA provider")
    __properties: ClassVar[List[str]] = ["certMgmt", "certSubject", "certThumbprint", "consoleUri", "customerId", "enabled", "generation", "httpsEnabled", "httpsPort", "id", "memUsageMiB", "moreUris", "serverName", "systemId", "systemWWN", "type", "version"]

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
        """Create an instance of Vasa from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cert_mgmt
        if self.cert_mgmt:
            _dict['certMgmt'] = self.cert_mgmt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in more_uris (list)
        _items = []
        if self.more_uris:
            for _item in self.more_uris:
                if _item:
                    _items.append(_item.to_dict())
            _dict['moreUris'] = _items
        # set to None if cert_mgmt (nullable) is None
        # and model_fields_set contains the field
        if self.cert_mgmt is None and "cert_mgmt" in self.model_fields_set:
            _dict['certMgmt'] = None

        # set to None if cert_subject (nullable) is None
        # and model_fields_set contains the field
        if self.cert_subject is None and "cert_subject" in self.model_fields_set:
            _dict['certSubject'] = None

        # set to None if cert_thumbprint (nullable) is None
        # and model_fields_set contains the field
        if self.cert_thumbprint is None and "cert_thumbprint" in self.model_fields_set:
            _dict['certThumbprint'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if enabled (nullable) is None
        # and model_fields_set contains the field
        if self.enabled is None and "enabled" in self.model_fields_set:
            _dict['enabled'] = None

        # set to None if https_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.https_enabled is None and "https_enabled" in self.model_fields_set:
            _dict['httpsEnabled'] = None

        # set to None if https_port (nullable) is None
        # and model_fields_set contains the field
        if self.https_port is None and "https_port" in self.model_fields_set:
            _dict['httpsPort'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if mem_usage_mi_b (nullable) is None
        # and model_fields_set contains the field
        if self.mem_usage_mi_b is None and "mem_usage_mi_b" in self.model_fields_set:
            _dict['memUsageMiB'] = None

        # set to None if more_uris (nullable) is None
        # and model_fields_set contains the field
        if self.more_uris is None and "more_uris" in self.model_fields_set:
            _dict['moreUris'] = None

        # set to None if server_name (nullable) is None
        # and model_fields_set contains the field
        if self.server_name is None and "server_name" in self.model_fields_set:
            _dict['serverName'] = None

        # set to None if system_id (nullable) is None
        # and model_fields_set contains the field
        if self.system_id is None and "system_id" in self.model_fields_set:
            _dict['systemId'] = None

        # set to None if system_wwn (nullable) is None
        # and model_fields_set contains the field
        if self.system_wwn is None and "system_wwn" in self.model_fields_set:
            _dict['systemWWN'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Vasa from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "certMgmt": CertMgmt.from_dict(obj["certMgmt"]) if obj.get("certMgmt") is not None else None,
            "certSubject": obj.get("certSubject"),
            "certThumbprint": obj.get("certThumbprint"),
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "enabled": obj.get("enabled"),
            "generation": obj.get("generation"),
            "httpsEnabled": obj.get("httpsEnabled"),
            "httpsPort": obj.get("httpsPort"),
            "id": obj.get("id"),
            "memUsageMiB": obj.get("memUsageMiB"),
            "moreUris": [VasaUriInfo.from_dict(_item) for _item in obj["moreUris"]] if obj.get("moreUris") is not None else None,
            "serverName": obj.get("serverName"),
            "systemId": obj.get("systemId"),
            "systemWWN": obj.get("systemWWN"),
            "type": obj.get("type"),
            "version": obj.get("version")
        })
        return _obj


