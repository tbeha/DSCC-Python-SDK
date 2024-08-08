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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from dscc.models.common_resource_attributes import CommonResourceAttributes
from dscc.models.deprecated_device_type4calendar import DeprecatedDeviceType4calendar
from dscc.models.deprecated_device_type4user_allocation_settings_single import DeprecatedDeviceType4userAllocationSettingsSingle
from dscc.models.device_type4_application_set_details_initiators_inner import DeviceType4ApplicationSetDetailsInitiatorsInner
from dscc.models.device_type4_snapshot_capacity import DeviceType4SnapshotCapacity
from dscc.models.device_type4_snapshots_list_single_creation_time import DeviceType4SnapshotsListSingleCreationTime
from dscc.models.device_type4_state import DeviceType4State
from dscc.models.device_type4policy import DeviceType4policy
from dscc.models.device_type4user_allocation_settings_single import DeviceType4userAllocationSettingsSingle
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4snapshotsList(BaseModel):
    """
    DeviceType4snapshotsList
    """ # noqa: E501
    admin_allocation_settings: Optional[DeviceType4userAllocationSettingsSingle] = Field(default=None, alias="adminAllocationSettings")
    base_id: Optional[StrictInt] = Field(default=None, description="snapshot Tdvv Size", alias="baseId")
    comment: Optional[StrictStr] = Field(default=None, description="Comments")
    common_resource_attributes: Optional[CommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    compression_policy: Optional[StrictStr] = Field(default=None, description="compression policy", alias="compressionPolicy")
    conversion_type: Optional[StrictStr] = Field(default=None, description="Conversion Type of Volume", alias="conversionType")
    copy_of_id: Optional[StrictInt] = Field(default=None, description="Copy of ID", alias="copyOfID")
    creation_time: Optional[DeviceType4SnapshotsListSingleCreationTime] = Field(default=None, alias="creationTime")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    data_reduction: Optional[StrictStr] = Field(default=None, description="Data Reduction type", alias="dataReduction")
    dedup: Optional[StrictStr] = None
    dev_type: Optional[StrictStr] = Field(default=None, description="Device Type", alias="devType")
    displayname: Optional[StrictStr] = Field(default=None, description="Display name of the volume")
    domain: Optional[StrictStr] = Field(default=None, description="Domain of the volume")
    efficiency_update_time: Optional[DeprecatedDeviceType4calendar] = Field(default=None, alias="efficiencyUpdateTime")
    expiration_time: Optional[DeprecatedDeviceType4calendar] = Field(default=None, alias="expirationTime")
    fully_provisioned: Optional[StrictBool] = Field(default=None, alias="fullyProvisioned")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    heads_per_cylinder: Optional[StrictInt] = Field(default=None, description="Heads per Cylinder", alias="headsPerCylinder")
    health_state: Optional[StrictInt] = Field(default=None, description="Health status of the Volume.", alias="healthState")
    hidden: Optional[StrictBool] = Field(default=None, description="Flag to know if the Volume is hidden or not")
    id: Optional[StrictStr] = Field(default=None, description="UID of the snapshot. `Filter`")
    initiators: Optional[List[DeviceType4ApplicationSetDetailsInitiatorsInner]] = Field(default=None, description="Initiator details")
    name: Optional[StrictStr] = Field(default=None, description="A user friendly name to identify the storage system volume (resourceName).")
    parent_id: Optional[StrictInt] = Field(default=None, description="Parent Id", alias="parentID")
    phys_parent_id: Optional[StrictInt] = Field(default=None, description="physical Parent Id", alias="physParentID")
    physical_copy: Optional[StrictBool] = Field(default=None, alias="physicalCopy")
    policy: Optional[DeviceType4policy] = None
    prov_type: Optional[StrictStr] = Field(default=None, description="Provisioning type", alias="provType")
    raid: Optional[StrictStr] = Field(default=None, description="Raid")
    rcopy_status: Optional[StrictStr] = Field(default=None, description="RemoteCopy Status", alias="rcopyStatus")
    read_only: Optional[StrictBool] = Field(default=None, alias="readOnly")
    retention_time: Optional[DeprecatedDeviceType4calendar] = Field(default=None, alias="retentionTime")
    ro_child_id: Optional[StrictInt] = Field(default=None, description="RO child id", alias="roChildID")
    rw_child_id: Optional[StrictInt] = Field(default=None, alias="rwChildID")
    sectors_per_track: Optional[StrictInt] = Field(default=None, description="Sector per Track", alias="sectorsPerTrack")
    shared_parent_id: Optional[StrictInt] = Field(default=None, description="Shared Parent Id", alias="sharedParentId")
    snapshot_alloc_limit: Optional[StrictInt] = Field(default=None, description="Snapshot alloc limit. This field is deprecated.", alias="snapshotAllocLimit")
    snapshot_alloc_warning: Optional[StrictInt] = Field(default=None, description="Snapshot alloc Warning. This field is deprecated.", alias="snapshotAllocWarning")
    snapshot_allocation_settings: Optional[DeprecatedDeviceType4userAllocationSettingsSingle] = Field(default=None, alias="snapshotAllocationSettings")
    snapshot_capacity: Optional[DeviceType4SnapshotCapacity] = Field(default=None, alias="snapshotCapacity")
    snapshot_id: Optional[StrictInt] = Field(default=None, description="Numeric ID of the resource", alias="snapshotId")
    snapshot_type: Optional[StrictStr] = Field(default=None, alias="snapshotType")
    space_calculation_time: Optional[DeprecatedDeviceType4calendar] = Field(default=None, alias="spaceCalculationTime")
    started: Optional[StrictBool] = None
    state: Optional[DeviceType4State] = None
    system_id: Optional[StrictStr] = Field(default=None, description="SystemUid/serialNumber of the array.", alias="systemId")
    thin_provisioned: Optional[StrictBool] = Field(default=None, description="Thin provisioning details", alias="thinProvisioned")
    type: Optional[StrictStr] = Field(default=None, description="type")
    unref_space_freed_time: Optional[DeprecatedDeviceType4calendar] = Field(default=None, alias="unrefSpaceFreedTime")
    user_alloc_limit: Optional[StrictInt] = Field(default=None, description="User alloc limit", alias="userAllocLimit")
    user_alloc_warning: Optional[StrictInt] = Field(default=None, description="User alloc space limit warning", alias="userAllocWarning")
    user_allocation_settings: Optional[DeviceType4userAllocationSettingsSingle] = Field(default=None, alias="userAllocationSettings")
    user_cpg_id: Optional[StrictInt] = Field(default=None, description="User CPG Id", alias="userCpgID")
    user_cpg_name: Optional[StrictStr] = Field(default=None, description="User CPG Name", alias="userCpgName")
    vlun_sector_size: Optional[StrictInt] = Field(default=None, description="VLUN sector size", alias="vlunSectorSize")
    wwn: Optional[StrictStr] = Field(default=None, description="Volume wwn.")
    __properties: ClassVar[List[str]] = ["adminAllocationSettings", "baseId", "comment", "commonResourceAttributes", "compressionPolicy", "conversionType", "copyOfID", "creationTime", "customerId", "dataReduction", "dedup", "devType", "displayname", "domain", "efficiencyUpdateTime", "expirationTime", "fullyProvisioned", "generation", "headsPerCylinder", "healthState", "hidden", "id", "initiators", "name", "parentID", "physParentID", "physicalCopy", "policy", "provType", "raid", "rcopyStatus", "readOnly", "retentionTime", "roChildID", "rwChildID", "sectorsPerTrack", "sharedParentId", "snapshotAllocLimit", "snapshotAllocWarning", "snapshotAllocationSettings", "snapshotCapacity", "snapshotId", "snapshotType", "spaceCalculationTime", "started", "state", "systemId", "thinProvisioned", "type", "unrefSpaceFreedTime", "userAllocLimit", "userAllocWarning", "userAllocationSettings", "userCpgID", "userCpgName", "vlunSectorSize", "wwn"]

    @field_validator('conversion_type')
    def conversion_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CONVERSIONTYPE_THIN', 'CONVERSIONTYPE_DDS', 'CONVERSIONTYPE_V1', 'CONVERSIONTYPE_V2', 'null']):
            raise ValueError("must be one of enum values ('CONVERSIONTYPE_THIN', 'CONVERSIONTYPE_DDS', 'CONVERSIONTYPE_V1', 'CONVERSIONTYPE_V2', 'null')")
        return value

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
        """Create an instance of DeviceType4snapshotsList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of admin_allocation_settings
        if self.admin_allocation_settings:
            _dict['adminAllocationSettings'] = self.admin_allocation_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of creation_time
        if self.creation_time:
            _dict['creationTime'] = self.creation_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of efficiency_update_time
        if self.efficiency_update_time:
            _dict['efficiencyUpdateTime'] = self.efficiency_update_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expiration_time
        if self.expiration_time:
            _dict['expirationTime'] = self.expiration_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in initiators (list)
        _items = []
        if self.initiators:
            for _item in self.initiators:
                if _item:
                    _items.append(_item.to_dict())
            _dict['initiators'] = _items
        # override the default output from pydantic by calling `to_dict()` of policy
        if self.policy:
            _dict['policy'] = self.policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of retention_time
        if self.retention_time:
            _dict['retentionTime'] = self.retention_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of snapshot_allocation_settings
        if self.snapshot_allocation_settings:
            _dict['snapshotAllocationSettings'] = self.snapshot_allocation_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of snapshot_capacity
        if self.snapshot_capacity:
            _dict['snapshotCapacity'] = self.snapshot_capacity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of space_calculation_time
        if self.space_calculation_time:
            _dict['spaceCalculationTime'] = self.space_calculation_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unref_space_freed_time
        if self.unref_space_freed_time:
            _dict['unrefSpaceFreedTime'] = self.unref_space_freed_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_allocation_settings
        if self.user_allocation_settings:
            _dict['userAllocationSettings'] = self.user_allocation_settings.to_dict()
        # set to None if admin_allocation_settings (nullable) is None
        # and model_fields_set contains the field
        if self.admin_allocation_settings is None and "admin_allocation_settings" in self.model_fields_set:
            _dict['adminAllocationSettings'] = None

        # set to None if base_id (nullable) is None
        # and model_fields_set contains the field
        if self.base_id is None and "base_id" in self.model_fields_set:
            _dict['baseId'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if compression_policy (nullable) is None
        # and model_fields_set contains the field
        if self.compression_policy is None and "compression_policy" in self.model_fields_set:
            _dict['compressionPolicy'] = None

        # set to None if conversion_type (nullable) is None
        # and model_fields_set contains the field
        if self.conversion_type is None and "conversion_type" in self.model_fields_set:
            _dict['conversionType'] = None

        # set to None if copy_of_id (nullable) is None
        # and model_fields_set contains the field
        if self.copy_of_id is None and "copy_of_id" in self.model_fields_set:
            _dict['copyOfID'] = None

        # set to None if creation_time (nullable) is None
        # and model_fields_set contains the field
        if self.creation_time is None and "creation_time" in self.model_fields_set:
            _dict['creationTime'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if data_reduction (nullable) is None
        # and model_fields_set contains the field
        if self.data_reduction is None and "data_reduction" in self.model_fields_set:
            _dict['dataReduction'] = None

        # set to None if dedup (nullable) is None
        # and model_fields_set contains the field
        if self.dedup is None and "dedup" in self.model_fields_set:
            _dict['dedup'] = None

        # set to None if dev_type (nullable) is None
        # and model_fields_set contains the field
        if self.dev_type is None and "dev_type" in self.model_fields_set:
            _dict['devType'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if efficiency_update_time (nullable) is None
        # and model_fields_set contains the field
        if self.efficiency_update_time is None and "efficiency_update_time" in self.model_fields_set:
            _dict['efficiencyUpdateTime'] = None

        # set to None if expiration_time (nullable) is None
        # and model_fields_set contains the field
        if self.expiration_time is None and "expiration_time" in self.model_fields_set:
            _dict['expirationTime'] = None

        # set to None if fully_provisioned (nullable) is None
        # and model_fields_set contains the field
        if self.fully_provisioned is None and "fully_provisioned" in self.model_fields_set:
            _dict['fullyProvisioned'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if heads_per_cylinder (nullable) is None
        # and model_fields_set contains the field
        if self.heads_per_cylinder is None and "heads_per_cylinder" in self.model_fields_set:
            _dict['headsPerCylinder'] = None

        # set to None if health_state (nullable) is None
        # and model_fields_set contains the field
        if self.health_state is None and "health_state" in self.model_fields_set:
            _dict['healthState'] = None

        # set to None if hidden (nullable) is None
        # and model_fields_set contains the field
        if self.hidden is None and "hidden" in self.model_fields_set:
            _dict['hidden'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if initiators (nullable) is None
        # and model_fields_set contains the field
        if self.initiators is None and "initiators" in self.model_fields_set:
            _dict['initiators'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if parent_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_id is None and "parent_id" in self.model_fields_set:
            _dict['parentID'] = None

        # set to None if phys_parent_id (nullable) is None
        # and model_fields_set contains the field
        if self.phys_parent_id is None and "phys_parent_id" in self.model_fields_set:
            _dict['physParentID'] = None

        # set to None if physical_copy (nullable) is None
        # and model_fields_set contains the field
        if self.physical_copy is None and "physical_copy" in self.model_fields_set:
            _dict['physicalCopy'] = None

        # set to None if policy (nullable) is None
        # and model_fields_set contains the field
        if self.policy is None and "policy" in self.model_fields_set:
            _dict['policy'] = None

        # set to None if prov_type (nullable) is None
        # and model_fields_set contains the field
        if self.prov_type is None and "prov_type" in self.model_fields_set:
            _dict['provType'] = None

        # set to None if raid (nullable) is None
        # and model_fields_set contains the field
        if self.raid is None and "raid" in self.model_fields_set:
            _dict['raid'] = None

        # set to None if rcopy_status (nullable) is None
        # and model_fields_set contains the field
        if self.rcopy_status is None and "rcopy_status" in self.model_fields_set:
            _dict['rcopyStatus'] = None

        # set to None if read_only (nullable) is None
        # and model_fields_set contains the field
        if self.read_only is None and "read_only" in self.model_fields_set:
            _dict['readOnly'] = None

        # set to None if retention_time (nullable) is None
        # and model_fields_set contains the field
        if self.retention_time is None and "retention_time" in self.model_fields_set:
            _dict['retentionTime'] = None

        # set to None if ro_child_id (nullable) is None
        # and model_fields_set contains the field
        if self.ro_child_id is None and "ro_child_id" in self.model_fields_set:
            _dict['roChildID'] = None

        # set to None if rw_child_id (nullable) is None
        # and model_fields_set contains the field
        if self.rw_child_id is None and "rw_child_id" in self.model_fields_set:
            _dict['rwChildID'] = None

        # set to None if sectors_per_track (nullable) is None
        # and model_fields_set contains the field
        if self.sectors_per_track is None and "sectors_per_track" in self.model_fields_set:
            _dict['sectorsPerTrack'] = None

        # set to None if shared_parent_id (nullable) is None
        # and model_fields_set contains the field
        if self.shared_parent_id is None and "shared_parent_id" in self.model_fields_set:
            _dict['sharedParentId'] = None

        # set to None if snapshot_alloc_limit (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_alloc_limit is None and "snapshot_alloc_limit" in self.model_fields_set:
            _dict['snapshotAllocLimit'] = None

        # set to None if snapshot_alloc_warning (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_alloc_warning is None and "snapshot_alloc_warning" in self.model_fields_set:
            _dict['snapshotAllocWarning'] = None

        # set to None if snapshot_allocation_settings (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_allocation_settings is None and "snapshot_allocation_settings" in self.model_fields_set:
            _dict['snapshotAllocationSettings'] = None

        # set to None if snapshot_capacity (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_capacity is None and "snapshot_capacity" in self.model_fields_set:
            _dict['snapshotCapacity'] = None

        # set to None if snapshot_id (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_id is None and "snapshot_id" in self.model_fields_set:
            _dict['snapshotId'] = None

        # set to None if snapshot_type (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_type is None and "snapshot_type" in self.model_fields_set:
            _dict['snapshotType'] = None

        # set to None if space_calculation_time (nullable) is None
        # and model_fields_set contains the field
        if self.space_calculation_time is None and "space_calculation_time" in self.model_fields_set:
            _dict['spaceCalculationTime'] = None

        # set to None if started (nullable) is None
        # and model_fields_set contains the field
        if self.started is None and "started" in self.model_fields_set:
            _dict['started'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if system_id (nullable) is None
        # and model_fields_set contains the field
        if self.system_id is None and "system_id" in self.model_fields_set:
            _dict['systemId'] = None

        # set to None if thin_provisioned (nullable) is None
        # and model_fields_set contains the field
        if self.thin_provisioned is None and "thin_provisioned" in self.model_fields_set:
            _dict['thinProvisioned'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if unref_space_freed_time (nullable) is None
        # and model_fields_set contains the field
        if self.unref_space_freed_time is None and "unref_space_freed_time" in self.model_fields_set:
            _dict['unrefSpaceFreedTime'] = None

        # set to None if user_alloc_limit (nullable) is None
        # and model_fields_set contains the field
        if self.user_alloc_limit is None and "user_alloc_limit" in self.model_fields_set:
            _dict['userAllocLimit'] = None

        # set to None if user_alloc_warning (nullable) is None
        # and model_fields_set contains the field
        if self.user_alloc_warning is None and "user_alloc_warning" in self.model_fields_set:
            _dict['userAllocWarning'] = None

        # set to None if user_allocation_settings (nullable) is None
        # and model_fields_set contains the field
        if self.user_allocation_settings is None and "user_allocation_settings" in self.model_fields_set:
            _dict['userAllocationSettings'] = None

        # set to None if user_cpg_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_cpg_id is None and "user_cpg_id" in self.model_fields_set:
            _dict['userCpgID'] = None

        # set to None if user_cpg_name (nullable) is None
        # and model_fields_set contains the field
        if self.user_cpg_name is None and "user_cpg_name" in self.model_fields_set:
            _dict['userCpgName'] = None

        # set to None if vlun_sector_size (nullable) is None
        # and model_fields_set contains the field
        if self.vlun_sector_size is None and "vlun_sector_size" in self.model_fields_set:
            _dict['vlunSectorSize'] = None

        # set to None if wwn (nullable) is None
        # and model_fields_set contains the field
        if self.wwn is None and "wwn" in self.model_fields_set:
            _dict['wwn'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4snapshotsList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adminAllocationSettings": DeviceType4userAllocationSettingsSingle.from_dict(obj["adminAllocationSettings"]) if obj.get("adminAllocationSettings") is not None else None,
            "baseId": obj.get("baseId"),
            "comment": obj.get("comment"),
            "commonResourceAttributes": CommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "compressionPolicy": obj.get("compressionPolicy"),
            "conversionType": obj.get("conversionType"),
            "copyOfID": obj.get("copyOfID"),
            "creationTime": DeviceType4SnapshotsListSingleCreationTime.from_dict(obj["creationTime"]) if obj.get("creationTime") is not None else None,
            "customerId": obj.get("customerId"),
            "dataReduction": obj.get("dataReduction"),
            "dedup": obj.get("dedup"),
            "devType": obj.get("devType"),
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "efficiencyUpdateTime": DeprecatedDeviceType4calendar.from_dict(obj["efficiencyUpdateTime"]) if obj.get("efficiencyUpdateTime") is not None else None,
            "expirationTime": DeprecatedDeviceType4calendar.from_dict(obj["expirationTime"]) if obj.get("expirationTime") is not None else None,
            "fullyProvisioned": obj.get("fullyProvisioned"),
            "generation": obj.get("generation"),
            "headsPerCylinder": obj.get("headsPerCylinder"),
            "healthState": obj.get("healthState"),
            "hidden": obj.get("hidden"),
            "id": obj.get("id"),
            "initiators": [DeviceType4ApplicationSetDetailsInitiatorsInner.from_dict(_item) for _item in obj["initiators"]] if obj.get("initiators") is not None else None,
            "name": obj.get("name"),
            "parentID": obj.get("parentID"),
            "physParentID": obj.get("physParentID"),
            "physicalCopy": obj.get("physicalCopy"),
            "policy": DeviceType4policy.from_dict(obj["policy"]) if obj.get("policy") is not None else None,
            "provType": obj.get("provType"),
            "raid": obj.get("raid"),
            "rcopyStatus": obj.get("rcopyStatus"),
            "readOnly": obj.get("readOnly"),
            "retentionTime": DeprecatedDeviceType4calendar.from_dict(obj["retentionTime"]) if obj.get("retentionTime") is not None else None,
            "roChildID": obj.get("roChildID"),
            "rwChildID": obj.get("rwChildID"),
            "sectorsPerTrack": obj.get("sectorsPerTrack"),
            "sharedParentId": obj.get("sharedParentId"),
            "snapshotAllocLimit": obj.get("snapshotAllocLimit"),
            "snapshotAllocWarning": obj.get("snapshotAllocWarning"),
            "snapshotAllocationSettings": DeprecatedDeviceType4userAllocationSettingsSingle.from_dict(obj["snapshotAllocationSettings"]) if obj.get("snapshotAllocationSettings") is not None else None,
            "snapshotCapacity": DeviceType4SnapshotCapacity.from_dict(obj["snapshotCapacity"]) if obj.get("snapshotCapacity") is not None else None,
            "snapshotId": obj.get("snapshotId"),
            "snapshotType": obj.get("snapshotType"),
            "spaceCalculationTime": DeprecatedDeviceType4calendar.from_dict(obj["spaceCalculationTime"]) if obj.get("spaceCalculationTime") is not None else None,
            "started": obj.get("started"),
            "state": DeviceType4State.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "systemId": obj.get("systemId"),
            "thinProvisioned": obj.get("thinProvisioned"),
            "type": obj.get("type"),
            "unrefSpaceFreedTime": DeprecatedDeviceType4calendar.from_dict(obj["unrefSpaceFreedTime"]) if obj.get("unrefSpaceFreedTime") is not None else None,
            "userAllocLimit": obj.get("userAllocLimit"),
            "userAllocWarning": obj.get("userAllocWarning"),
            "userAllocationSettings": DeviceType4userAllocationSettingsSingle.from_dict(obj["userAllocationSettings"]) if obj.get("userAllocationSettings") is not None else None,
            "userCpgID": obj.get("userCpgID"),
            "userCpgName": obj.get("userCpgName"),
            "vlunSectorSize": obj.get("vlunSectorSize"),
            "wwn": obj.get("wwn")
        })
        return _obj


