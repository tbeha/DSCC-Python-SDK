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

class NimbleProtectionTemplateFieldsWithoutSortKey(BaseModel):
    """
    NimbleProtectionTemplateFieldsWithoutSortKey
    """ # noqa: E501
    agent_hostname: Optional[StrictStr] = Field(default=None, description="Generic Backup agent hostname. Custom port number can be specified with agent hostname using \\\\\":\\\\\".")
    app_cluster_name: Optional[StrictStr] = Field(default=None, description="If the application is running within a Windows cluster environment then this is the cluster name.")
    app_id: Optional[StrictStr] = Field(default=None, description="Application ID running on the server. Application ID can only be specified if application synchronization is VSS.  Possible values:'exchange_dag', 'sql2012', 'sql2014', 'inval', 'sql2005', 'sql2016', 'exchange', 'sql2017', 'sql2018', 'hyperv'.")
    app_server: Optional[StrictStr] = Field(default=None, description="Application server hostname.")
    app_service_name: Optional[StrictStr] = Field(default=None, description="If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment.")
    app_sync: Optional[StrictStr] = Field(default=None, description="Application synchronization ({none|vss|vmware|generic}). Possible values:'vss', 'vmware', 'none', 'generic'.")
    creation_time: Optional[StrictInt] = Field(default=None, description="Time when this protection template was created.")
    id: Optional[StrictStr] = Field(default=None, description="Identifier for protection template.")
    last_modified: Optional[StrictInt] = Field(default=None, description="Time when this protection template was last modified.")
    name: Optional[StrictStr] = Field(default=None, description="Fully qualified name of protection template.")
    vcenter_hostname: Optional[StrictStr] = Field(default=None, description="VMware vCenter hostname. Custom port number can be specified with vCenter hostname.")
    __properties: ClassVar[List[str]] = ["agent_hostname", "app_cluster_name", "app_id", "app_server", "app_service_name", "app_sync", "creation_time", "id", "last_modified", "name", "vcenter_hostname"]

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
        """Create an instance of NimbleProtectionTemplateFieldsWithoutSortKey from a JSON string"""
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

        # set to None if creation_time (nullable) is None
        # and model_fields_set contains the field
        if self.creation_time is None and "creation_time" in self.model_fields_set:
            _dict['creation_time'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if last_modified (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified is None and "last_modified" in self.model_fields_set:
            _dict['last_modified'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if vcenter_hostname (nullable) is None
        # and model_fields_set contains the field
        if self.vcenter_hostname is None and "vcenter_hostname" in self.model_fields_set:
            _dict['vcenter_hostname'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleProtectionTemplateFieldsWithoutSortKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agent_hostname": obj.get("agent_hostname"),
            "app_cluster_name": obj.get("app_cluster_name"),
            "app_id": obj.get("app_id"),
            "app_server": obj.get("app_server"),
            "app_service_name": obj.get("app_service_name"),
            "app_sync": obj.get("app_sync"),
            "creation_time": obj.get("creation_time"),
            "id": obj.get("id"),
            "last_modified": obj.get("last_modified"),
            "name": obj.get("name"),
            "vcenter_hostname": obj.get("vcenter_hostname")
        })
        return _obj


