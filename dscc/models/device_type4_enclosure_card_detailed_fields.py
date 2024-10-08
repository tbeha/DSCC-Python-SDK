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
from typing_extensions import Annotated
from dscc.models.associated_links_inner import AssociatedLinksInner
from dscc.models.common_resource_attributes import CommonResourceAttributes
from dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_boot_drives import DeviceType4EnclosureCardDetailedFieldsEnclosureCardBootDrives
from dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_cpu import DeviceType4EnclosureCardDetailedFieldsEnclosureCardCpu
from dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_fan import DeviceType4EnclosureCardDetailedFieldsEnclosureCardFan
from dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_mem import DeviceType4EnclosureCardDetailedFieldsEnclosureCardMem
from dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_pci import DeviceType4EnclosureCardDetailedFieldsEnclosureCardPci
from dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_tpm import DeviceType4EnclosureCardDetailedFieldsEnclosureCardTpm
from dscc.models.device_type4_manufacturing_single import DeviceType4ManufacturingSingle
from dscc.models.device_type4_state import DeviceType4State
from dscc.models.device_type4ec_dcsdata import DeviceType4ecDcsdata
from dscc.models.device_type4enclosure_type_single import DeviceType4enclosureTypeSingle
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4EnclosureCardDetailedFields(BaseModel):
    """
    DeviceType4EnclosureCardDetailedFields
    """ # noqa: E501
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    common_resource_attributes: Optional[CommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    dcsdata: Optional[DeviceType4ecDcsdata] = None
    displayname: Optional[StrictStr] = Field(default=None, description="Enclosure Display name")
    domain: Optional[StrictStr] = Field(default=None, description="Domain that the resource belongs to")
    element_status_code: Optional[StrictStr] = Field(default=None, description="Enclosure status code", alias="elementStatusCode")
    enclosure_card_boot_drives: Optional[DeviceType4EnclosureCardDetailedFieldsEnclosureCardBootDrives] = Field(default=None, alias="enclosureCardBootDrives")
    enclosure_card_cpu: Optional[DeviceType4EnclosureCardDetailedFieldsEnclosureCardCpu] = Field(default=None, alias="enclosureCardCpu")
    enclosure_card_fan: Optional[DeviceType4EnclosureCardDetailedFieldsEnclosureCardFan] = Field(default=None, alias="enclosureCardFan")
    enclosure_card_id: Optional[StrictInt] = Field(default=None, description="ID of enclosure card.", alias="enclosureCardId")
    enclosure_card_mem: Optional[DeviceType4EnclosureCardDetailedFieldsEnclosureCardMem] = Field(default=None, alias="enclosureCardMem")
    enclosure_card_pci: Optional[DeviceType4EnclosureCardDetailedFieldsEnclosureCardPci] = Field(default=None, alias="enclosureCardPci")
    enclosure_card_tpm: Optional[DeviceType4EnclosureCardDetailedFieldsEnclosureCardTpm] = Field(default=None, alias="enclosureCardTpm")
    enclosure_id: Optional[StrictInt] = Field(default=None, alias="enclosureId")
    enclosure_name: Optional[StrictStr] = Field(default=None, description="Name of the enclosure.", alias="enclosureName")
    enclosure_type: Optional[DeviceType4enclosureTypeSingle] = Field(default=None, alias="enclosureType")
    enclosure_uid: Optional[StrictStr] = Field(default=None, description="Parent UID of the resource.", alias="enclosureUid")
    fail_indicator: Optional[StrictBool] = Field(default=None, alias="failIndicator")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the resource.")
    is_node_card: Optional[StrictBool] = Field(default=None, alias="isNodeCard")
    locate_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if the locate beacon is enabled or not", alias="locateEnabled")
    locate_seven_seg_display: Optional[StrictStr] = Field(default=None, description="Seven segment display on enclosure card when locate is on", alias="locateSevenSegDisplay")
    loop_a: Optional[StrictBool] = Field(default=None, alias="loopA")
    loop_b: Optional[StrictBool] = Field(default=None, alias="loopB")
    manufacturing: Optional[DeviceType4ManufacturingSingle] = None
    name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Name of the resource.")
    request_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed enclosure object", alias="requestUri")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed enclosure object", alias="resourceUri")
    safe_to_remove: Optional[StrictBool] = Field(default=None, alias="safeToRemove")
    seven_seg_display: Optional[StrictStr] = Field(default=None, description="Seven segment display", alias="sevenSegDisplay")
    state: Optional[DeviceType4State] = None
    system_id: Optional[StrictStr] = Field(default=None, description="SystemUid/Serial Number  of the array.", alias="systemId")
    type: Optional[StrictStr] = Field(default=None, description="type")
    __properties: ClassVar[List[str]] = ["associatedLinks", "commonResourceAttributes", "consoleUri", "customerId", "dcsdata", "displayname", "domain", "elementStatusCode", "enclosureCardBootDrives", "enclosureCardCpu", "enclosureCardFan", "enclosureCardId", "enclosureCardMem", "enclosureCardPci", "enclosureCardTpm", "enclosureId", "enclosureName", "enclosureType", "enclosureUid", "failIndicator", "generation", "id", "isNodeCard", "locateEnabled", "locateSevenSegDisplay", "loopA", "loopB", "manufacturing", "name", "requestUri", "resourceUri", "safeToRemove", "sevenSegDisplay", "state", "systemId", "type"]

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
        """Create an instance of DeviceType4EnclosureCardDetailedFields from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dcsdata
        if self.dcsdata:
            _dict['dcsdata'] = self.dcsdata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of enclosure_card_boot_drives
        if self.enclosure_card_boot_drives:
            _dict['enclosureCardBootDrives'] = self.enclosure_card_boot_drives.to_dict()
        # override the default output from pydantic by calling `to_dict()` of enclosure_card_cpu
        if self.enclosure_card_cpu:
            _dict['enclosureCardCpu'] = self.enclosure_card_cpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of enclosure_card_fan
        if self.enclosure_card_fan:
            _dict['enclosureCardFan'] = self.enclosure_card_fan.to_dict()
        # override the default output from pydantic by calling `to_dict()` of enclosure_card_mem
        if self.enclosure_card_mem:
            _dict['enclosureCardMem'] = self.enclosure_card_mem.to_dict()
        # override the default output from pydantic by calling `to_dict()` of enclosure_card_pci
        if self.enclosure_card_pci:
            _dict['enclosureCardPci'] = self.enclosure_card_pci.to_dict()
        # override the default output from pydantic by calling `to_dict()` of enclosure_card_tpm
        if self.enclosure_card_tpm:
            _dict['enclosureCardTpm'] = self.enclosure_card_tpm.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manufacturing
        if self.manufacturing:
            _dict['manufacturing'] = self.manufacturing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # set to None if associated_links (nullable) is None
        # and model_fields_set contains the field
        if self.associated_links is None and "associated_links" in self.model_fields_set:
            _dict['associatedLinks'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if dcsdata (nullable) is None
        # and model_fields_set contains the field
        if self.dcsdata is None and "dcsdata" in self.model_fields_set:
            _dict['dcsdata'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if element_status_code (nullable) is None
        # and model_fields_set contains the field
        if self.element_status_code is None and "element_status_code" in self.model_fields_set:
            _dict['elementStatusCode'] = None

        # set to None if enclosure_card_boot_drives (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_card_boot_drives is None and "enclosure_card_boot_drives" in self.model_fields_set:
            _dict['enclosureCardBootDrives'] = None

        # set to None if enclosure_card_cpu (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_card_cpu is None and "enclosure_card_cpu" in self.model_fields_set:
            _dict['enclosureCardCpu'] = None

        # set to None if enclosure_card_fan (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_card_fan is None and "enclosure_card_fan" in self.model_fields_set:
            _dict['enclosureCardFan'] = None

        # set to None if enclosure_card_mem (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_card_mem is None and "enclosure_card_mem" in self.model_fields_set:
            _dict['enclosureCardMem'] = None

        # set to None if enclosure_card_pci (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_card_pci is None and "enclosure_card_pci" in self.model_fields_set:
            _dict['enclosureCardPci'] = None

        # set to None if enclosure_card_tpm (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_card_tpm is None and "enclosure_card_tpm" in self.model_fields_set:
            _dict['enclosureCardTpm'] = None

        # set to None if enclosure_id (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_id is None and "enclosure_id" in self.model_fields_set:
            _dict['enclosureId'] = None

        # set to None if enclosure_name (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_name is None and "enclosure_name" in self.model_fields_set:
            _dict['enclosureName'] = None

        # set to None if enclosure_uid (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_uid is None and "enclosure_uid" in self.model_fields_set:
            _dict['enclosureUid'] = None

        # set to None if fail_indicator (nullable) is None
        # and model_fields_set contains the field
        if self.fail_indicator is None and "fail_indicator" in self.model_fields_set:
            _dict['failIndicator'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if is_node_card (nullable) is None
        # and model_fields_set contains the field
        if self.is_node_card is None and "is_node_card" in self.model_fields_set:
            _dict['isNodeCard'] = None

        # set to None if locate_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.locate_enabled is None and "locate_enabled" in self.model_fields_set:
            _dict['locateEnabled'] = None

        # set to None if locate_seven_seg_display (nullable) is None
        # and model_fields_set contains the field
        if self.locate_seven_seg_display is None and "locate_seven_seg_display" in self.model_fields_set:
            _dict['locateSevenSegDisplay'] = None

        # set to None if loop_a (nullable) is None
        # and model_fields_set contains the field
        if self.loop_a is None and "loop_a" in self.model_fields_set:
            _dict['loopA'] = None

        # set to None if loop_b (nullable) is None
        # and model_fields_set contains the field
        if self.loop_b is None and "loop_b" in self.model_fields_set:
            _dict['loopB'] = None

        # set to None if manufacturing (nullable) is None
        # and model_fields_set contains the field
        if self.manufacturing is None and "manufacturing" in self.model_fields_set:
            _dict['manufacturing'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestUri'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if safe_to_remove (nullable) is None
        # and model_fields_set contains the field
        if self.safe_to_remove is None and "safe_to_remove" in self.model_fields_set:
            _dict['safeToRemove'] = None

        # set to None if seven_seg_display (nullable) is None
        # and model_fields_set contains the field
        if self.seven_seg_display is None and "seven_seg_display" in self.model_fields_set:
            _dict['sevenSegDisplay'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

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
        """Create an instance of DeviceType4EnclosureCardDetailedFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedLinks": [AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "commonResourceAttributes": CommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "dcsdata": DeviceType4ecDcsdata.from_dict(obj["dcsdata"]) if obj.get("dcsdata") is not None else None,
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "elementStatusCode": obj.get("elementStatusCode"),
            "enclosureCardBootDrives": DeviceType4EnclosureCardDetailedFieldsEnclosureCardBootDrives.from_dict(obj["enclosureCardBootDrives"]) if obj.get("enclosureCardBootDrives") is not None else None,
            "enclosureCardCpu": DeviceType4EnclosureCardDetailedFieldsEnclosureCardCpu.from_dict(obj["enclosureCardCpu"]) if obj.get("enclosureCardCpu") is not None else None,
            "enclosureCardFan": DeviceType4EnclosureCardDetailedFieldsEnclosureCardFan.from_dict(obj["enclosureCardFan"]) if obj.get("enclosureCardFan") is not None else None,
            "enclosureCardId": obj.get("enclosureCardId"),
            "enclosureCardMem": DeviceType4EnclosureCardDetailedFieldsEnclosureCardMem.from_dict(obj["enclosureCardMem"]) if obj.get("enclosureCardMem") is not None else None,
            "enclosureCardPci": DeviceType4EnclosureCardDetailedFieldsEnclosureCardPci.from_dict(obj["enclosureCardPci"]) if obj.get("enclosureCardPci") is not None else None,
            "enclosureCardTpm": DeviceType4EnclosureCardDetailedFieldsEnclosureCardTpm.from_dict(obj["enclosureCardTpm"]) if obj.get("enclosureCardTpm") is not None else None,
            "enclosureId": obj.get("enclosureId"),
            "enclosureName": obj.get("enclosureName"),
            "enclosureType": obj.get("enclosureType"),
            "enclosureUid": obj.get("enclosureUid"),
            "failIndicator": obj.get("failIndicator"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "isNodeCard": obj.get("isNodeCard"),
            "locateEnabled": obj.get("locateEnabled"),
            "locateSevenSegDisplay": obj.get("locateSevenSegDisplay"),
            "loopA": obj.get("loopA"),
            "loopB": obj.get("loopB"),
            "manufacturing": DeviceType4ManufacturingSingle.from_dict(obj["manufacturing"]) if obj.get("manufacturing") is not None else None,
            "name": obj.get("name"),
            "requestUri": obj.get("requestUri"),
            "resourceUri": obj.get("resourceUri"),
            "safeToRemove": obj.get("safeToRemove"),
            "sevenSegDisplay": obj.get("sevenSegDisplay"),
            "state": DeviceType4State.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "systemId": obj.get("systemId"),
            "type": obj.get("type")
        })
        return _obj


