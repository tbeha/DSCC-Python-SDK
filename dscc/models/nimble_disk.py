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
from dscc.models.associated_links_inner import AssociatedLinksInner
from dscc.models.nimble_common_resource_attributes import NimbleCommonResourceAttributes
from dscc.models.nimble_disk_smart_attributes import NimbleDiskSmartAttributes
from typing import Optional, Set
from typing_extensions import Self

class NimbleDisk(BaseModel):
    """
    NimbleDisk
    """ # noqa: E501
    array_id: Optional[StrictStr] = Field(default=None, description="ID of array the disk belongs to. A 42 digit hexadecimal number. `Filter, Sort`")
    array_name: Optional[StrictStr] = Field(default=None, description="Name of array the disk belongs to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  `Filter, Sort`")
    device_type: Optional[StrictStr] = Field(default=None, description="Type of disk (HDD, SSD, N/A). Disk type. Possible values: 'hdd', 'ssd'. `Filter, Sort`")
    id: Optional[StrictStr] = Field(default=None, description="Identifier of disk. A 42 digit hexadecimal number. `Filter`")
    model: Optional[StrictStr] = Field(default=None, description="Disk model name. `Filter, Sort`")
    serial: Optional[StrictStr] = Field(default=None, description="Disk serial number(N/A if empty). `Filter, Sort`")
    shelf_id: Optional[StrictStr] = Field(default=None, description="Identifies the physical shelf the disk belongs to. A 42 digit hexadecimal number. `Filter, Sort`")
    shelf_serial: Optional[StrictStr] = Field(default=None, description="Serial number of the shelf the disk is attached to. `Filter, Sort`")
    state: Optional[StrictStr] = Field(default=None, description="Disk hardware state. Disk state. Possible values: 'valid', 'in use', 'failed', absent', 'removed', 'void', 't_fail', 'foreign'. `Filter, Sort`")
    associated_links: Optional[List[Optional[AssociatedLinksInner]]] = Field(default=None, description="Associated Links Details")
    bank: Optional[StrictInt] = Field(default=None, description="Disk bank number.")
    block_type: Optional[StrictStr] = Field(default=None, description="Native block type of the disk. Possible values: 'block_512e', 'block_4Kn', 'block_none', 'block_512n'.")
    common_resource_attributes: Optional[NimbleCommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    disk_internal_stat1: Optional[StrictStr] = Field(default=None, description="Internal disk statistic 1.")
    disk_op: Optional[StrictStr] = Field(default=None, description="The intended operation to be performed on the specified disk.")
    disk_type: Optional[StrictStr] = Field(default=None, description="Type of disk. Possible values: 'hdd', 'ssd'.")
    firmware_version: Optional[StrictStr] = Field(default=None, description="Firmware version on the disk.")
    force: Optional[StrictBool] = Field(default=None, description="Forcibly add a disk.")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    hba: Optional[StrictInt] = Field(default=None, description="HBA ID the disk is connected to.")
    is_dfc: Optional[StrictBool] = Field(default=None, description="Is disk part of dual flash carrier.")
    partial_response_ok: Optional[StrictBool] = Field(default=None, description="Whether response is partial or not.")
    path: Optional[StrictStr] = Field(default=None, description="Disk SCSI device path.")
    port: Optional[StrictInt] = Field(default=None, description="HBA port number the disk is connected to.")
    raid_id: Optional[StrictInt] = Field(default=None, description="Raid ID.")
    raid_resync_average_speed: Optional[StrictInt] = Field(default=None, description="Average RAID rebuild speed (bytes/sec).")
    raid_resync_current_speed: Optional[StrictInt] = Field(default=None, description="Current RAID rebuild speed (bytes/sec).")
    raid_resync_percent: Optional[StrictInt] = Field(default=None, description="Percentage RAID rebuild completed on this disk.")
    raid_state: Optional[StrictStr] = Field(default=None, description="RAID status for the disk (N/A, okay, resynchronizing, spare, faulty). Disk RAID state. Possible values: 'N/A', 'okay', 'resynchronizing', 'spare', 'faulty'.")
    resource_uri: Optional[StrictStr] = Field(default=None, description="Link to the object URI", alias="resourceUri")
    shelf_location: Optional[StrictStr] = Field(default=None, description="Identifies the controller, port, and chain position of the shelf the disk belongs to.")
    shelf_location_id: Optional[StrictInt] = Field(default=None, description="Identifies the position shelf the disk belongs to, as coded integer.")
    size: Optional[StrictInt] = Field(default=None, description="Disk size in bytes.")
    slot: Optional[StrictInt] = Field(default=None, description="Disk slot number.")
    smart_attribute_list: Optional[List[Optional[NimbleDiskSmartAttributes]]] = Field(default=None, description="S.M.A.R.T. attributes for the disk. List of Smart attributes.")
    type: Optional[StrictStr] = Field(default=None, description="type")
    vendor: Optional[StrictStr] = Field(default=None, description="Vendor name of the disk manufacturer.")
    vshelf_id: Optional[StrictInt] = Field(default=None, description="Identifies the local shelf id the disk belongs to.")
    __properties: ClassVar[List[str]] = ["array_id", "array_name", "device_type", "id", "model", "serial", "shelf_id", "shelf_serial", "state", "associated_links", "bank", "block_type", "commonResourceAttributes", "consoleUri", "customerId", "disk_internal_stat1", "disk_op", "disk_type", "firmware_version", "force", "generation", "hba", "is_dfc", "partial_response_ok", "path", "port", "raid_id", "raid_resync_average_speed", "raid_resync_current_speed", "raid_resync_percent", "raid_state", "resourceUri", "shelf_location", "shelf_location_id", "size", "slot", "smart_attribute_list", "type", "vendor", "vshelf_id"]

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
        """Create an instance of NimbleDisk from a JSON string"""
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
            _dict['associated_links'] = _items
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in smart_attribute_list (list)
        _items = []
        if self.smart_attribute_list:
            for _item in self.smart_attribute_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['smart_attribute_list'] = _items
        # set to None if array_id (nullable) is None
        # and model_fields_set contains the field
        if self.array_id is None and "array_id" in self.model_fields_set:
            _dict['array_id'] = None

        # set to None if array_name (nullable) is None
        # and model_fields_set contains the field
        if self.array_name is None and "array_name" in self.model_fields_set:
            _dict['array_name'] = None

        # set to None if device_type (nullable) is None
        # and model_fields_set contains the field
        if self.device_type is None and "device_type" in self.model_fields_set:
            _dict['device_type'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        # set to None if serial (nullable) is None
        # and model_fields_set contains the field
        if self.serial is None and "serial" in self.model_fields_set:
            _dict['serial'] = None

        # set to None if shelf_id (nullable) is None
        # and model_fields_set contains the field
        if self.shelf_id is None and "shelf_id" in self.model_fields_set:
            _dict['shelf_id'] = None

        # set to None if shelf_serial (nullable) is None
        # and model_fields_set contains the field
        if self.shelf_serial is None and "shelf_serial" in self.model_fields_set:
            _dict['shelf_serial'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if bank (nullable) is None
        # and model_fields_set contains the field
        if self.bank is None and "bank" in self.model_fields_set:
            _dict['bank'] = None

        # set to None if block_type (nullable) is None
        # and model_fields_set contains the field
        if self.block_type is None and "block_type" in self.model_fields_set:
            _dict['block_type'] = None

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

        # set to None if disk_internal_stat1 (nullable) is None
        # and model_fields_set contains the field
        if self.disk_internal_stat1 is None and "disk_internal_stat1" in self.model_fields_set:
            _dict['disk_internal_stat1'] = None

        # set to None if disk_op (nullable) is None
        # and model_fields_set contains the field
        if self.disk_op is None and "disk_op" in self.model_fields_set:
            _dict['disk_op'] = None

        # set to None if disk_type (nullable) is None
        # and model_fields_set contains the field
        if self.disk_type is None and "disk_type" in self.model_fields_set:
            _dict['disk_type'] = None

        # set to None if firmware_version (nullable) is None
        # and model_fields_set contains the field
        if self.firmware_version is None and "firmware_version" in self.model_fields_set:
            _dict['firmware_version'] = None

        # set to None if force (nullable) is None
        # and model_fields_set contains the field
        if self.force is None and "force" in self.model_fields_set:
            _dict['force'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if hba (nullable) is None
        # and model_fields_set contains the field
        if self.hba is None and "hba" in self.model_fields_set:
            _dict['hba'] = None

        # set to None if is_dfc (nullable) is None
        # and model_fields_set contains the field
        if self.is_dfc is None and "is_dfc" in self.model_fields_set:
            _dict['is_dfc'] = None

        # set to None if partial_response_ok (nullable) is None
        # and model_fields_set contains the field
        if self.partial_response_ok is None and "partial_response_ok" in self.model_fields_set:
            _dict['partial_response_ok'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if port (nullable) is None
        # and model_fields_set contains the field
        if self.port is None and "port" in self.model_fields_set:
            _dict['port'] = None

        # set to None if raid_id (nullable) is None
        # and model_fields_set contains the field
        if self.raid_id is None and "raid_id" in self.model_fields_set:
            _dict['raid_id'] = None

        # set to None if raid_resync_average_speed (nullable) is None
        # and model_fields_set contains the field
        if self.raid_resync_average_speed is None and "raid_resync_average_speed" in self.model_fields_set:
            _dict['raid_resync_average_speed'] = None

        # set to None if raid_resync_current_speed (nullable) is None
        # and model_fields_set contains the field
        if self.raid_resync_current_speed is None and "raid_resync_current_speed" in self.model_fields_set:
            _dict['raid_resync_current_speed'] = None

        # set to None if raid_resync_percent (nullable) is None
        # and model_fields_set contains the field
        if self.raid_resync_percent is None and "raid_resync_percent" in self.model_fields_set:
            _dict['raid_resync_percent'] = None

        # set to None if raid_state (nullable) is None
        # and model_fields_set contains the field
        if self.raid_state is None and "raid_state" in self.model_fields_set:
            _dict['raid_state'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if shelf_location (nullable) is None
        # and model_fields_set contains the field
        if self.shelf_location is None and "shelf_location" in self.model_fields_set:
            _dict['shelf_location'] = None

        # set to None if shelf_location_id (nullable) is None
        # and model_fields_set contains the field
        if self.shelf_location_id is None and "shelf_location_id" in self.model_fields_set:
            _dict['shelf_location_id'] = None

        # set to None if size (nullable) is None
        # and model_fields_set contains the field
        if self.size is None and "size" in self.model_fields_set:
            _dict['size'] = None

        # set to None if slot (nullable) is None
        # and model_fields_set contains the field
        if self.slot is None and "slot" in self.model_fields_set:
            _dict['slot'] = None

        # set to None if smart_attribute_list (nullable) is None
        # and model_fields_set contains the field
        if self.smart_attribute_list is None and "smart_attribute_list" in self.model_fields_set:
            _dict['smart_attribute_list'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if vendor (nullable) is None
        # and model_fields_set contains the field
        if self.vendor is None and "vendor" in self.model_fields_set:
            _dict['vendor'] = None

        # set to None if vshelf_id (nullable) is None
        # and model_fields_set contains the field
        if self.vshelf_id is None and "vshelf_id" in self.model_fields_set:
            _dict['vshelf_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleDisk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "array_id": obj.get("array_id"),
            "array_name": obj.get("array_name"),
            "device_type": obj.get("device_type"),
            "id": obj.get("id"),
            "model": obj.get("model"),
            "serial": obj.get("serial"),
            "shelf_id": obj.get("shelf_id"),
            "shelf_serial": obj.get("shelf_serial"),
            "state": obj.get("state"),
            "associated_links": [AssociatedLinksInner.from_dict(_item) for _item in obj["associated_links"]] if obj.get("associated_links") is not None else None,
            "bank": obj.get("bank"),
            "block_type": obj.get("block_type"),
            "commonResourceAttributes": NimbleCommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "disk_internal_stat1": obj.get("disk_internal_stat1"),
            "disk_op": obj.get("disk_op"),
            "disk_type": obj.get("disk_type"),
            "firmware_version": obj.get("firmware_version"),
            "force": obj.get("force"),
            "generation": obj.get("generation"),
            "hba": obj.get("hba"),
            "is_dfc": obj.get("is_dfc"),
            "partial_response_ok": obj.get("partial_response_ok"),
            "path": obj.get("path"),
            "port": obj.get("port"),
            "raid_id": obj.get("raid_id"),
            "raid_resync_average_speed": obj.get("raid_resync_average_speed"),
            "raid_resync_current_speed": obj.get("raid_resync_current_speed"),
            "raid_resync_percent": obj.get("raid_resync_percent"),
            "raid_state": obj.get("raid_state"),
            "resourceUri": obj.get("resourceUri"),
            "shelf_location": obj.get("shelf_location"),
            "shelf_location_id": obj.get("shelf_location_id"),
            "size": obj.get("size"),
            "slot": obj.get("slot"),
            "smart_attribute_list": [NimbleDiskSmartAttributes.from_dict(_item) for _item in obj["smart_attribute_list"]] if obj.get("smart_attribute_list") is not None else None,
            "type": obj.get("type"),
            "vendor": obj.get("vendor"),
            "vshelf_id": obj.get("vshelf_id")
        })
        return _obj


