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
from dscc.models.common_resource_attributes_device_type4_host_set import CommonResourceAttributesDeviceType4HostSet
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4HostSetListObj(BaseModel):
    """
    Host Sets details
    """ # noqa: E501
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    comment: Optional[StrictStr] = Field(default=None, description="Comment on the Host Set")
    common_resource_attributes: Optional[CommonResourceAttributesDeviceType4HostSet] = Field(default=None, alias="commonResourceAttributes")
    displayname: Optional[StrictStr] = Field(default=None, description="Name to be used for display purposes")
    domain: Optional[StrictStr] = Field(default=None, description="Domain name of the Host Set")
    generation: Optional[StrictInt] = Field(default=None, description="Generation Time of the Resource `Filter, Sort`")
    host_set_id: Optional[StrictInt] = Field(default=None, description="Numeric ID of the resource", alias="hostSetId")
    id: Optional[StrictStr] = Field(default=None, description="HostSet Resource UID `Filter`")
    members: Optional[List[Optional[StrictStr]]] = Field(default=None, description="system ntp addresses `Filter, Sort`")
    name: Optional[StrictStr] = Field(default=None, description="Host Set Name `Filter, Sort`")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed hostset object", alias="resourceUri")
    sc_host_group_id: Optional[StrictStr] = Field(default=None, description="Host Service HostGroup Id `Filter`", alias="sc_HostGroupId")
    system_uid: Optional[StrictStr] = Field(default=None, description="Serail Number of the system `Filter`", alias="systemUid")
    system_wwn: Optional[StrictStr] = Field(default=None, description="System wwn `Filter, Sort`", alias="systemWWN")
    uri: Optional[StrictStr] = Field(default=None, description="Uri")
    uuid: Optional[StrictStr] = Field(default=None, description="HostSet Resource UUID")
    __properties: ClassVar[List[str]] = ["associatedLinks", "comment", "commonResourceAttributes", "displayname", "domain", "generation", "hostSetId", "id", "members", "name", "resourceUri", "sc_HostGroupId", "systemUid", "systemWWN", "uri", "uuid"]

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
        """Create an instance of DeviceType4HostSetListObj from a JSON string"""
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
            _dict['associatedLinks'] = _items
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if host_set_id (nullable) is None
        # and model_fields_set contains the field
        if self.host_set_id is None and "host_set_id" in self.model_fields_set:
            _dict['hostSetId'] = None

        # set to None if members (nullable) is None
        # and model_fields_set contains the field
        if self.members is None and "members" in self.model_fields_set:
            _dict['members'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if sc_host_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.sc_host_group_id is None and "sc_host_group_id" in self.model_fields_set:
            _dict['sc_HostGroupId'] = None

        # set to None if uri (nullable) is None
        # and model_fields_set contains the field
        if self.uri is None and "uri" in self.model_fields_set:
            _dict['uri'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4HostSetListObj from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedLinks": [AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "comment": obj.get("comment"),
            "commonResourceAttributes": CommonResourceAttributesDeviceType4HostSet.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "generation": obj.get("generation"),
            "hostSetId": obj.get("hostSetId"),
            "id": obj.get("id"),
            "members": obj.get("members"),
            "name": obj.get("name"),
            "resourceUri": obj.get("resourceUri"),
            "sc_HostGroupId": obj.get("sc_HostGroupId"),
            "systemUid": obj.get("systemUid"),
            "systemWWN": obj.get("systemWWN"),
            "uri": obj.get("uri"),
            "uuid": obj.get("uuid")
        })
        return _obj


