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
from dscc.models.edit_app_set_qos_config_input import EditAppSetQosConfigInput
from dscc.models.volume_set_application_type import VolumeSetApplicationType
from dscc.models.volume_set_importance import VolumeSetImportance
from typing import Optional, Set
from typing_extensions import Self

class VolumeSetPut(BaseModel):
    """
    VolumeSetPut
    """ # noqa: E501
    add_members: Optional[List[Optional[StrictStr]]] = Field(default=None, description="Members to add to application set", alias="addMembers")
    app_set_business_unit: Optional[StrictStr] = Field(default=None, description="App set business unit", alias="appSetBusinessUnit")
    app_set_comments: Optional[StrictStr] = Field(default=None, description="App set comments", alias="appSetComments")
    app_set_importance: Optional[VolumeSetImportance] = Field(default=None, alias="appSetImportance")
    app_set_name: Optional[StrictStr] = Field(default=None, description="App set name", alias="appSetName")
    app_set_type: Optional[VolumeSetApplicationType] = Field(default=None, alias="appSetType")
    custom_app_type: Optional[StrictStr] = Field(default=None, description="App set name for Custom workloads when appSetType=CUSTOM", alias="customAppType")
    edit_app_set_qos_config_input: Optional[EditAppSetQosConfigInput] = Field(default=None, alias="editAppSetQosConfigInput")
    remove_members: Optional[List[Optional[StrictStr]]] = Field(default=None, description="Members to remove from application set", alias="removeMembers")
    __properties: ClassVar[List[str]] = ["addMembers", "appSetBusinessUnit", "appSetComments", "appSetImportance", "appSetName", "appSetType", "customAppType", "editAppSetQosConfigInput", "removeMembers"]

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
        """Create an instance of VolumeSetPut from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of edit_app_set_qos_config_input
        if self.edit_app_set_qos_config_input:
            _dict['editAppSetQosConfigInput'] = self.edit_app_set_qos_config_input.to_dict()
        # set to None if add_members (nullable) is None
        # and model_fields_set contains the field
        if self.add_members is None and "add_members" in self.model_fields_set:
            _dict['addMembers'] = None

        # set to None if app_set_business_unit (nullable) is None
        # and model_fields_set contains the field
        if self.app_set_business_unit is None and "app_set_business_unit" in self.model_fields_set:
            _dict['appSetBusinessUnit'] = None

        # set to None if app_set_comments (nullable) is None
        # and model_fields_set contains the field
        if self.app_set_comments is None and "app_set_comments" in self.model_fields_set:
            _dict['appSetComments'] = None

        # set to None if app_set_importance (nullable) is None
        # and model_fields_set contains the field
        if self.app_set_importance is None and "app_set_importance" in self.model_fields_set:
            _dict['appSetImportance'] = None

        # set to None if app_set_name (nullable) is None
        # and model_fields_set contains the field
        if self.app_set_name is None and "app_set_name" in self.model_fields_set:
            _dict['appSetName'] = None

        # set to None if app_set_type (nullable) is None
        # and model_fields_set contains the field
        if self.app_set_type is None and "app_set_type" in self.model_fields_set:
            _dict['appSetType'] = None

        # set to None if custom_app_type (nullable) is None
        # and model_fields_set contains the field
        if self.custom_app_type is None and "custom_app_type" in self.model_fields_set:
            _dict['customAppType'] = None

        # set to None if edit_app_set_qos_config_input (nullable) is None
        # and model_fields_set contains the field
        if self.edit_app_set_qos_config_input is None and "edit_app_set_qos_config_input" in self.model_fields_set:
            _dict['editAppSetQosConfigInput'] = None

        # set to None if remove_members (nullable) is None
        # and model_fields_set contains the field
        if self.remove_members is None and "remove_members" in self.model_fields_set:
            _dict['removeMembers'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VolumeSetPut from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addMembers": obj.get("addMembers"),
            "appSetBusinessUnit": obj.get("appSetBusinessUnit"),
            "appSetComments": obj.get("appSetComments"),
            "appSetImportance": obj.get("appSetImportance"),
            "appSetName": obj.get("appSetName"),
            "appSetType": obj.get("appSetType"),
            "customAppType": obj.get("customAppType"),
            "editAppSetQosConfigInput": EditAppSetQosConfigInput.from_dict(obj["editAppSetQosConfigInput"]) if obj.get("editAppSetQosConfigInput") is not None else None,
            "removeMembers": obj.get("removeMembers")
        })
        return _obj


