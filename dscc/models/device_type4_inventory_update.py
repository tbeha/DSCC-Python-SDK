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
from dscc.models.device_type4_inventory_update_change import DeviceType4InventoryUpdateChange
from dscc.models.device_type4_inventory_update_parent_detail import DeviceType4InventoryUpdateParentDetail
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4InventoryUpdate(BaseModel):
    """
    HPE Alletra Storage MP InventoryUpdate details
    """ # noqa: E501
    changes: Optional[List[Optional[DeviceType4InventoryUpdateChange]]] = Field(default=None, description="List of inventory changes for the component")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    displayname: Optional[StrictStr] = Field(default=None, description="Name to be used for display purposes")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    last_modified_epoch: Optional[StrictInt] = Field(default=None, description="last modified epoch", alias="lastModifiedEpoch")
    parent: Optional[DeviceType4InventoryUpdateParentDetail] = None
    sub_component: Optional[StrictStr] = Field(default=None, description="Sub component", alias="subComponent")
    system_id: Optional[StrictStr] = Field(default=None, description="systemId", alias="systemId")
    system_wwn: Optional[StrictStr] = Field(default=None, description="System wwn ", alias="systemWWN")
    type: Optional[StrictStr] = Field(default=None, description="type")
    uid: Optional[StrictStr] = Field(default=None, description="UID of the update")
    uri: Optional[StrictStr] = Field(default=None, description="Uri")
    __properties: ClassVar[List[str]] = ["changes", "customerId", "displayname", "generation", "lastModifiedEpoch", "parent", "subComponent", "systemId", "systemWWN", "type", "uid", "uri"]

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
        """Create an instance of DeviceType4InventoryUpdate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in changes (list)
        _items = []
        if self.changes:
            for _item in self.changes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['changes'] = _items
        # override the default output from pydantic by calling `to_dict()` of parent
        if self.parent:
            _dict['parent'] = self.parent.to_dict()
        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if last_modified_epoch (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified_epoch is None and "last_modified_epoch" in self.model_fields_set:
            _dict['lastModifiedEpoch'] = None

        # set to None if parent (nullable) is None
        # and model_fields_set contains the field
        if self.parent is None and "parent" in self.model_fields_set:
            _dict['parent'] = None

        # set to None if system_wwn (nullable) is None
        # and model_fields_set contains the field
        if self.system_wwn is None and "system_wwn" in self.model_fields_set:
            _dict['systemWWN'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if uri (nullable) is None
        # and model_fields_set contains the field
        if self.uri is None and "uri" in self.model_fields_set:
            _dict['uri'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4InventoryUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "changes": [DeviceType4InventoryUpdateChange.from_dict(_item) for _item in obj["changes"]] if obj.get("changes") is not None else None,
            "customerId": obj.get("customerId"),
            "displayname": obj.get("displayname"),
            "generation": obj.get("generation"),
            "lastModifiedEpoch": obj.get("lastModifiedEpoch"),
            "parent": DeviceType4InventoryUpdateParentDetail.from_dict(obj["parent"]) if obj.get("parent") is not None else None,
            "subComponent": obj.get("subComponent"),
            "systemId": obj.get("systemId"),
            "systemWWN": obj.get("systemWWN"),
            "type": obj.get("type"),
            "uid": obj.get("uid"),
            "uri": obj.get("uri")
        })
        return _obj


