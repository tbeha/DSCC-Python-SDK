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
from typing import Optional, Set
from typing_extensions import Self

class NimbleEditVolumeCollectionInput(BaseModel):
    """
    Edit Nimble volume-collection input.
    """ # noqa: E501
    agent_hostname: Optional[StrictStr] = Field(default=None, description="Generic backup agent hostname. Custom port number can be specified with agent hostname using \\\\\":\\\\\". String of up to 64 alphanumeric characters, - and . and : are allowed after first character.")
    agent_username: Optional[StrictStr] = Field(default=None, description="Generic backup agent username. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.")
    app_cluster_name: Optional[StrictStr] = Field(default=None, description="If the application is running within a Windows cluster environment, this is the cluster name. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.")
    app_id: Optional[StrictStr] = Field(default=None, description="Application ID running on the server. Application ID can only be specified if application synchronization is \\\\\"vss\\\\\". Possible values: 'inval', 'exchange', 'exchange_dag', 'hyperv', 'sql2005', 'sql2008', 'sql2012', 'sql2014', 'sql2016', 'sql2017'.")
    app_server: Optional[StrictStr] = Field(default=None, description="Application server hostname. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.")
    app_service_name: Optional[StrictStr] = Field(default=None, description="If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.")
    app_sync: Optional[StrictStr] = Field(default=None, description="Application Synchronization. Possible values: 'none', 'vss', 'vmware', 'generic'.")
    description: Optional[StrictStr] = Field(default=None, description="Text description of volume collection. String of up to 255 printable ASCII characters.")
    name: Optional[StrictStr] = Field(default=None, description="Name of volume collection. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.")
    vcenter_hostname: Optional[StrictStr] = Field(default=None, description="VMware vCenter hostname. Custom port number can be specified with vCenter hostname using \\\\\":\\\\\". String of up to 64 alphanumeric characters, - and . and : are allowed after first character.")
    vcenter_username: Optional[StrictStr] = Field(default=None, description="Application VMware vCenter username. String of up to 80 alphanumeric characters, beginning with a letter. It can include ampersand (@), backslash (\\), dash (-), period (.), and underscore (_).")
    __properties: ClassVar[List[str]] = ["agent_hostname", "agent_username", "app_cluster_name", "app_id", "app_server", "app_service_name", "app_sync", "description", "name", "vcenter_hostname", "vcenter_username"]

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
        """Create an instance of NimbleEditVolumeCollectionInput from a JSON string"""
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
        # set to None if agent_hostname (nullable) is None
        # and model_fields_set contains the field
        if self.agent_hostname is None and "agent_hostname" in self.model_fields_set:
            _dict['agent_hostname'] = None

        # set to None if agent_username (nullable) is None
        # and model_fields_set contains the field
        if self.agent_username is None and "agent_username" in self.model_fields_set:
            _dict['agent_username'] = None

        # set to None if app_cluster_name (nullable) is None
        # and model_fields_set contains the field
        if self.app_cluster_name is None and "app_cluster_name" in self.model_fields_set:
            _dict['app_cluster_name'] = None

        # set to None if app_id (nullable) is None
        # and model_fields_set contains the field
        if self.app_id is None and "app_id" in self.model_fields_set:
            _dict['app_id'] = None

        # set to None if app_server (nullable) is None
        # and model_fields_set contains the field
        if self.app_server is None and "app_server" in self.model_fields_set:
            _dict['app_server'] = None

        # set to None if app_service_name (nullable) is None
        # and model_fields_set contains the field
        if self.app_service_name is None and "app_service_name" in self.model_fields_set:
            _dict['app_service_name'] = None

        # set to None if app_sync (nullable) is None
        # and model_fields_set contains the field
        if self.app_sync is None and "app_sync" in self.model_fields_set:
            _dict['app_sync'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if vcenter_hostname (nullable) is None
        # and model_fields_set contains the field
        if self.vcenter_hostname is None and "vcenter_hostname" in self.model_fields_set:
            _dict['vcenter_hostname'] = None

        # set to None if vcenter_username (nullable) is None
        # and model_fields_set contains the field
        if self.vcenter_username is None and "vcenter_username" in self.model_fields_set:
            _dict['vcenter_username'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleEditVolumeCollectionInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agent_hostname": obj.get("agent_hostname"),
            "agent_username": obj.get("agent_username"),
            "app_cluster_name": obj.get("app_cluster_name"),
            "app_id": obj.get("app_id"),
            "app_server": obj.get("app_server"),
            "app_service_name": obj.get("app_service_name"),
            "app_sync": obj.get("app_sync"),
            "description": obj.get("description"),
            "name": obj.get("name"),
            "vcenter_hostname": obj.get("vcenter_hostname"),
            "vcenter_username": obj.get("vcenter_username")
        })
        return _obj


