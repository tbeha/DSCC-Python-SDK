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

class NimbleVCollectionFieldsWithSortKey(BaseModel):
    """
    NimbleVCollectionFieldsWithSortKey
    """ # noqa: E501
    app_cluster_name: Optional[StrictStr] = Field(default=None, description="If the application is running within a Windows cluster environment, this is the cluster name. `Filter, Sort`")
    app_id: Optional[StrictStr] = Field(default=None, description="Application ID running on the server. Application ID can only be specified if application synchronization is \\\\\"vss\\\\\". `Filter, Sort` Possible values: 'exchange_dag', 'sql2012', 'inval', 'sql2014', 'sql2005', 'sql2016', 'exchange', 'sql2017', 'sql2018', 'hyperv'.")
    app_server: Optional[StrictStr] = Field(default=None, description="Application server hostname. `Filter, Sort`")
    app_service_name: Optional[StrictStr] = Field(default=None, description="If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment. `Filter, Sort`")
    id: Optional[StrictStr] = Field(default=None, description="Identifier of the Volume-Collection. `Filter`")
    name: Optional[StrictStr] = Field(default=None, description="Name of volume collection. `Filter, Sort`")
    prottmpl_id: Optional[StrictStr] = Field(default=None, description="Identifier of the protection template whose attributes will be used to create this volume collection. This attribute is only used for input when creating a volume collection and is not outputed. `Filter, Sort`")
    replication_type: Optional[StrictStr] = Field(default=None, description="Type of replication configured for the volume collection. Possible values: 'synchronous', 'periodic_snapshot'. `Filter, Sort`")
    synchronous_replication_state: Optional[StrictStr] = Field(default=None, description="State of synchronous replication on the volume collection. Possible values: 'in_sync', 'not_applicable', 'out_of_sync', 'unknown'. `Filter, Sort`")
    synchronous_replication_type: Optional[StrictStr] = Field(default=None, description="Type of synchronous replication configured for the volume collection. Possible values: 'soft_available', 'not_applicable'. `Filter, Sort`")
    __properties: ClassVar[List[str]] = ["app_cluster_name", "app_id", "app_server", "app_service_name", "id", "name", "prottmpl_id", "replication_type", "synchronous_replication_state", "synchronous_replication_type"]

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
        """Create an instance of NimbleVCollectionFieldsWithSortKey from a JSON string"""
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

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if prottmpl_id (nullable) is None
        # and model_fields_set contains the field
        if self.prottmpl_id is None and "prottmpl_id" in self.model_fields_set:
            _dict['prottmpl_id'] = None

        # set to None if replication_type (nullable) is None
        # and model_fields_set contains the field
        if self.replication_type is None and "replication_type" in self.model_fields_set:
            _dict['replication_type'] = None

        # set to None if synchronous_replication_state (nullable) is None
        # and model_fields_set contains the field
        if self.synchronous_replication_state is None and "synchronous_replication_state" in self.model_fields_set:
            _dict['synchronous_replication_state'] = None

        # set to None if synchronous_replication_type (nullable) is None
        # and model_fields_set contains the field
        if self.synchronous_replication_type is None and "synchronous_replication_type" in self.model_fields_set:
            _dict['synchronous_replication_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleVCollectionFieldsWithSortKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_cluster_name": obj.get("app_cluster_name"),
            "app_id": obj.get("app_id"),
            "app_server": obj.get("app_server"),
            "app_service_name": obj.get("app_service_name"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "prottmpl_id": obj.get("prottmpl_id"),
            "replication_type": obj.get("replication_type"),
            "synchronous_replication_state": obj.get("synchronous_replication_state"),
            "synchronous_replication_type": obj.get("synchronous_replication_type")
        })
        return _obj


