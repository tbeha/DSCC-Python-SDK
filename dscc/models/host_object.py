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
from dscc.models.host_group_summary_object import HostGroupSummaryObject
from dscc.models.initiator_summary import InitiatorSummary
from dscc.models.sc_associated_links_inner import ScAssociatedLinksInner
from typing import Optional, Set
from typing_extensions import Self

class HostObject(BaseModel):
    """
    HostObject
    """ # noqa: E501
    associated_links: Optional[List[Optional[ScAssociatedLinksInner]]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    associated_systems: Optional[List[StrictStr]] = Field(default=None, description="system IDs to which the host belongs to.", alias="associatedSystems")
    comment: Optional[StrictStr] = Field(default=None, description="Comment")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    contact: Optional[StrictStr] = Field(default=None, description="Contact information")
    customer_id: Optional[StrictStr] = Field(default=None, description="The customer application identifier", alias="customerId")
    edit_status: Optional[StrictStr] = Field(default=None, description="Host Update or Delete progress status. Possible status are: Update_In_Progress,Update_Success,Update_Failed,Delete_In_Progress,Delete_Failed,Not_Applicable,Merge_Success,Merge_In_Progress,Merge_Failed,Convert_In_Progress,Convert_Failed,Convert_Success. `Filter`", alias="editStatus")
    fqdn: Optional[StrictStr] = Field(default=None, description="Fully qualified domain name of the host.")
    generation: Optional[StrictInt] = Field(default=None, description="A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.")
    host_groups: Optional[List[Optional[HostGroupSummaryObject]]] = Field(default=None, description="Host group to which the host belongs to. `Filter` by hostGroupId.", alias="hostGroups")
    id: Optional[StrictStr] = Field(default=None, description="Identifier for host. `Filter`")
    initiators: Optional[List[Optional[InitiatorSummary]]] = Field(default=None, description="Host initiator list this host is associated with. `Filter` by initiatorId.")
    ip_address: Optional[StrictStr] = Field(default=None, description="IP address of the host.", alias="ipAddress")
    is_mergable: Optional[StrictBool] = Field(default=None, description="Indicates whether host has a duplicate. This field is applicable only when isMergable `Filter` is set to true on the GET All else will be set to false always.", alias="isMergable")
    is_vvol_host: Optional[StrictBool] = Field(default=None, description="Indicates if this host is created with NVMe initiator to be used by VASA vvol or not", alias="isVvolHost")
    location: Optional[StrictStr] = Field(default=None, description="location.")
    marked_for_delete: Optional[StrictBool] = Field(default=None, description="Indicates whether host is marked for deletion or not", alias="markedForDelete")
    model: Optional[StrictStr] = Field(default=None, description="Model")
    name: Optional[StrictStr] = Field(default=None, description="Name of the host. `Filter, Sort`")
    operating_system: Optional[StrictStr] = Field(default=None, description="Host operating system. `Filter`", alias="operatingSystem")
    persona: Optional[StrictStr] = Field(default=None, description="Host persona details.")
    protocol: Optional[StrictStr] = Field(default=None, description="protocol supported are : FC ,iSCSI or NVMe")
    subnet: Optional[StrictStr] = Field(default=None, description="subnet.")
    systems: Optional[List[StrictStr]] = Field(default=None, description="system IDs to which the host belongs to. `Filter`")
    type: Optional[StrictStr] = Field(default=None, description="The type of resource.")
    user_created: Optional[StrictBool] = Field(default=None, description="Indicates whether user created host or discovered host", alias="userCreated")
    __properties: ClassVar[List[str]] = ["associatedLinks", "associatedSystems", "comment", "consoleUri", "contact", "customerId", "editStatus", "fqdn", "generation", "hostGroups", "id", "initiators", "ipAddress", "isMergable", "isVvolHost", "location", "markedForDelete", "model", "name", "operatingSystem", "persona", "protocol", "subnet", "systems", "type", "userCreated"]

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
        """Create an instance of HostObject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in host_groups (list)
        _items = []
        if self.host_groups:
            for _item in self.host_groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['hostGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in initiators (list)
        _items = []
        if self.initiators:
            for _item in self.initiators:
                if _item:
                    _items.append(_item.to_dict())
            _dict['initiators'] = _items
        # set to None if associated_systems (nullable) is None
        # and model_fields_set contains the field
        if self.associated_systems is None and "associated_systems" in self.model_fields_set:
            _dict['associatedSystems'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if contact (nullable) is None
        # and model_fields_set contains the field
        if self.contact is None and "contact" in self.model_fields_set:
            _dict['contact'] = None

        # set to None if edit_status (nullable) is None
        # and model_fields_set contains the field
        if self.edit_status is None and "edit_status" in self.model_fields_set:
            _dict['editStatus'] = None

        # set to None if fqdn (nullable) is None
        # and model_fields_set contains the field
        if self.fqdn is None and "fqdn" in self.model_fields_set:
            _dict['fqdn'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if ip_address (nullable) is None
        # and model_fields_set contains the field
        if self.ip_address is None and "ip_address" in self.model_fields_set:
            _dict['ipAddress'] = None

        # set to None if is_mergable (nullable) is None
        # and model_fields_set contains the field
        if self.is_mergable is None and "is_mergable" in self.model_fields_set:
            _dict['isMergable'] = None

        # set to None if is_vvol_host (nullable) is None
        # and model_fields_set contains the field
        if self.is_vvol_host is None and "is_vvol_host" in self.model_fields_set:
            _dict['isVvolHost'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if marked_for_delete (nullable) is None
        # and model_fields_set contains the field
        if self.marked_for_delete is None and "marked_for_delete" in self.model_fields_set:
            _dict['markedForDelete'] = None

        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if operating_system (nullable) is None
        # and model_fields_set contains the field
        if self.operating_system is None and "operating_system" in self.model_fields_set:
            _dict['operatingSystem'] = None

        # set to None if persona (nullable) is None
        # and model_fields_set contains the field
        if self.persona is None and "persona" in self.model_fields_set:
            _dict['persona'] = None

        # set to None if protocol (nullable) is None
        # and model_fields_set contains the field
        if self.protocol is None and "protocol" in self.model_fields_set:
            _dict['protocol'] = None

        # set to None if subnet (nullable) is None
        # and model_fields_set contains the field
        if self.subnet is None and "subnet" in self.model_fields_set:
            _dict['subnet'] = None

        # set to None if systems (nullable) is None
        # and model_fields_set contains the field
        if self.systems is None and "systems" in self.model_fields_set:
            _dict['systems'] = None

        # set to None if user_created (nullable) is None
        # and model_fields_set contains the field
        if self.user_created is None and "user_created" in self.model_fields_set:
            _dict['userCreated'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HostObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedLinks": [ScAssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "associatedSystems": obj.get("associatedSystems"),
            "comment": obj.get("comment"),
            "consoleUri": obj.get("consoleUri"),
            "contact": obj.get("contact"),
            "customerId": obj.get("customerId"),
            "editStatus": obj.get("editStatus"),
            "fqdn": obj.get("fqdn"),
            "generation": obj.get("generation"),
            "hostGroups": [HostGroupSummaryObject.from_dict(_item) for _item in obj["hostGroups"]] if obj.get("hostGroups") is not None else None,
            "id": obj.get("id"),
            "initiators": [InitiatorSummary.from_dict(_item) for _item in obj["initiators"]] if obj.get("initiators") is not None else None,
            "ipAddress": obj.get("ipAddress"),
            "isMergable": obj.get("isMergable"),
            "isVvolHost": obj.get("isVvolHost"),
            "location": obj.get("location"),
            "markedForDelete": obj.get("markedForDelete"),
            "model": obj.get("model"),
            "name": obj.get("name"),
            "operatingSystem": obj.get("operatingSystem"),
            "persona": obj.get("persona"),
            "protocol": obj.get("protocol"),
            "subnet": obj.get("subnet"),
            "systems": obj.get("systems"),
            "type": obj.get("type"),
            "userCreated": obj.get("userCreated")
        })
        return _obj


