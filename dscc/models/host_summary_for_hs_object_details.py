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
from dscc.models.initiator_object_details import InitiatorObjectDetails
from typing import Optional, Set
from typing_extensions import Self

class HostSummaryForHSObjectDetails(BaseModel):
    """
    HostSummaryForHSObjectDetails
    """ # noqa: E501
    associated_systems: Optional[List[Optional[StrictStr]]] = Field(default=None, description="system IDs to which the host belongs to.", alias="associatedSystems")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="The customer application identifier", alias="customerId")
    generation: Optional[StrictInt] = Field(default=None, description="A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.")
    id: Optional[StrictStr] = Field(default=None, description="Identifier for host.")
    initiators: Optional[List[Optional[InitiatorObjectDetails]]] = Field(default=None, description="Initiator to which the host belongs to.")
    ip_address: Optional[StrictStr] = Field(default=None, description="IP address of the host.", alias="ipAddress")
    is_mergable: Optional[StrictBool] = Field(default=None, description="Indicates whether host group has a duplicate. This field is applicable only when isMergable `Filter` is set to true on the GET All else will be set to false always.", alias="isMergable")
    is_vvol_host: Optional[StrictBool] = Field(default=None, description="Indicates if this host is used to export VASA vVol over NVMe Protocol.", alias="isVvolHost")
    marked_for_delete: Optional[StrictBool] = Field(default=None, description="Indicates whether host is marked for deletion or not", alias="markedForDelete")
    name: Optional[StrictStr] = Field(default=None, description="Name of the host.")
    systems: Optional[List[Optional[StrictStr]]] = Field(default=None, description="system IDs to which the host belongs to. (This field is deprecated)")
    type: Optional[StrictStr] = Field(default=None, description="The type of resource.")
    user_created: Optional[StrictBool] = Field(default=None, description="Indicates whether user created host or discovered host. (This field is deprecated)", alias="userCreated")
    __properties: ClassVar[List[str]] = ["associatedSystems", "consoleUri", "customerId", "generation", "id", "initiators", "ipAddress", "isMergable", "isVvolHost", "markedForDelete", "name", "systems", "type", "userCreated"]

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
        """Create an instance of HostSummaryForHSObjectDetails from a JSON string"""
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

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if initiators (nullable) is None
        # and model_fields_set contains the field
        if self.initiators is None and "initiators" in self.model_fields_set:
            _dict['initiators'] = None

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

        # set to None if marked_for_delete (nullable) is None
        # and model_fields_set contains the field
        if self.marked_for_delete is None and "marked_for_delete" in self.model_fields_set:
            _dict['markedForDelete'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

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
        """Create an instance of HostSummaryForHSObjectDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedSystems": obj.get("associatedSystems"),
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "initiators": [InitiatorObjectDetails.from_dict(_item) for _item in obj["initiators"]] if obj.get("initiators") is not None else None,
            "ipAddress": obj.get("ipAddress"),
            "isMergable": obj.get("isMergable"),
            "isVvolHost": obj.get("isVvolHost"),
            "markedForDelete": obj.get("markedForDelete"),
            "name": obj.get("name"),
            "systems": obj.get("systems"),
            "type": obj.get("type"),
            "userCreated": obj.get("userCreated")
        })
        return _obj


