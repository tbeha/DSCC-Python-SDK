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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from dscc.models.device_type4snapshot_tdvvsize import DeviceType4snapshotTdvvsize
from dscc.models.device_type4space import DeviceType4space
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4SnapshotCapacity(BaseModel):
    """
    DeviceType4SnapshotCapacity
    """ # noqa: E501
    admin_space: Optional[DeviceType4space] = Field(default=None, alias="adminSpace")
    branch_used_blocks_mi_b: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Branch used blocks size in MiB. This attribute contains the used space of the base volume and its Read-Only snapshots. This field is relevant for the system OS version 10.3.0 and above.", alias="branchUsedBlocksMiB")
    branch_v_size_mi_b: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Branch virtual size in MiB. This attribute contains the provisioned or virtual size of the base volume and its Read-Only snapshots.", alias="branchVSizeMiB")
    compact_efficiency: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Compact Efficiency", alias="compactEfficiency")
    compression_efficiency: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Compression Efficiency", alias="compressionEfficiency")
    copied_mb: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Copied MB", alias="copiedMB")
    copied_perc: Optional[StrictInt] = Field(default=None, description="Copied Perecentage", alias="copiedPerc")
    ddc_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ddcSize")
    dds_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ddsSize")
    dedup_savings_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="dedupSavingsSize")
    dedup_written_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="dedupWrittenSize")
    host_written_mi_b: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Host written data size in MiB.", alias="hostWrittenMiB")
    host_written_to_virtual_percent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Host written to virtual percent", alias="hostWrittenToVirtualPercent")
    size_mi_b: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Size in MiB", alias="sizeMiB")
    snapshot_tdvv_size: Optional[DeviceType4snapshotTdvvsize] = Field(default=None, alias="snapshotTdvvSize")
    snapshot_used_to_virtual_percent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Snapshot used to virtual percent", alias="snapshotUsedToVirtualPercent")
    total_raw_reserved_mi_b: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total Raw Reserved Space in MiB", alias="totalRawReservedMiB")
    total_reserved_mi_b: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Description", alias="totalReservedMiB")
    total_space_mi_b: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total Space in MiB", alias="totalSpaceMiB")
    used_blocks_mi_b: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Used Blocks Size in MiB. This attribute contains the used space of the base volume and its Read-Only snapshots. This field is relevant for the system OS versions equal and below 10.2.x. For the system OS version 10.3.0 and above, please refer the field branchUsedBlocksMiB.", alias="usedBlocksMiB")
    used_capacity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Used volume capacity.", alias="usedCapacity")
    used_size_mi_b: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Used Size in MiB", alias="usedSizeMiB")
    user_reserved_to_virtual_percent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="User reseved to virtual percent", alias="userReservedToVirtualPercent")
    user_space: Optional[DeviceType4space] = Field(default=None, alias="userSpace")
    user_used_to_virtual_percent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="User used to virtual percent", alias="userUsedToVirtualPercent")
    __properties: ClassVar[List[str]] = ["adminSpace", "branchUsedBlocksMiB", "branchVSizeMiB", "compactEfficiency", "compressionEfficiency", "copiedMB", "copiedPerc", "ddcSize", "ddsSize", "dedupSavingsSize", "dedupWrittenSize", "hostWrittenMiB", "hostWrittenToVirtualPercent", "sizeMiB", "snapshotTdvvSize", "snapshotUsedToVirtualPercent", "totalRawReservedMiB", "totalReservedMiB", "totalSpaceMiB", "usedBlocksMiB", "usedCapacity", "usedSizeMiB", "userReservedToVirtualPercent", "userSpace", "userUsedToVirtualPercent"]

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
        """Create an instance of DeviceType4SnapshotCapacity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of admin_space
        if self.admin_space:
            _dict['adminSpace'] = self.admin_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of snapshot_tdvv_size
        if self.snapshot_tdvv_size:
            _dict['snapshotTdvvSize'] = self.snapshot_tdvv_size.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_space
        if self.user_space:
            _dict['userSpace'] = self.user_space.to_dict()
        # set to None if admin_space (nullable) is None
        # and model_fields_set contains the field
        if self.admin_space is None and "admin_space" in self.model_fields_set:
            _dict['adminSpace'] = None

        # set to None if branch_used_blocks_mi_b (nullable) is None
        # and model_fields_set contains the field
        if self.branch_used_blocks_mi_b is None and "branch_used_blocks_mi_b" in self.model_fields_set:
            _dict['branchUsedBlocksMiB'] = None

        # set to None if branch_v_size_mi_b (nullable) is None
        # and model_fields_set contains the field
        if self.branch_v_size_mi_b is None and "branch_v_size_mi_b" in self.model_fields_set:
            _dict['branchVSizeMiB'] = None

        # set to None if compact_efficiency (nullable) is None
        # and model_fields_set contains the field
        if self.compact_efficiency is None and "compact_efficiency" in self.model_fields_set:
            _dict['compactEfficiency'] = None

        # set to None if compression_efficiency (nullable) is None
        # and model_fields_set contains the field
        if self.compression_efficiency is None and "compression_efficiency" in self.model_fields_set:
            _dict['compressionEfficiency'] = None

        # set to None if copied_mb (nullable) is None
        # and model_fields_set contains the field
        if self.copied_mb is None and "copied_mb" in self.model_fields_set:
            _dict['copiedMB'] = None

        # set to None if copied_perc (nullable) is None
        # and model_fields_set contains the field
        if self.copied_perc is None and "copied_perc" in self.model_fields_set:
            _dict['copiedPerc'] = None

        # set to None if ddc_size (nullable) is None
        # and model_fields_set contains the field
        if self.ddc_size is None and "ddc_size" in self.model_fields_set:
            _dict['ddcSize'] = None

        # set to None if dds_size (nullable) is None
        # and model_fields_set contains the field
        if self.dds_size is None and "dds_size" in self.model_fields_set:
            _dict['ddsSize'] = None

        # set to None if dedup_savings_size (nullable) is None
        # and model_fields_set contains the field
        if self.dedup_savings_size is None and "dedup_savings_size" in self.model_fields_set:
            _dict['dedupSavingsSize'] = None

        # set to None if dedup_written_size (nullable) is None
        # and model_fields_set contains the field
        if self.dedup_written_size is None and "dedup_written_size" in self.model_fields_set:
            _dict['dedupWrittenSize'] = None

        # set to None if host_written_mi_b (nullable) is None
        # and model_fields_set contains the field
        if self.host_written_mi_b is None and "host_written_mi_b" in self.model_fields_set:
            _dict['hostWrittenMiB'] = None

        # set to None if host_written_to_virtual_percent (nullable) is None
        # and model_fields_set contains the field
        if self.host_written_to_virtual_percent is None and "host_written_to_virtual_percent" in self.model_fields_set:
            _dict['hostWrittenToVirtualPercent'] = None

        # set to None if size_mi_b (nullable) is None
        # and model_fields_set contains the field
        if self.size_mi_b is None and "size_mi_b" in self.model_fields_set:
            _dict['sizeMiB'] = None

        # set to None if snapshot_tdvv_size (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_tdvv_size is None and "snapshot_tdvv_size" in self.model_fields_set:
            _dict['snapshotTdvvSize'] = None

        # set to None if snapshot_used_to_virtual_percent (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_used_to_virtual_percent is None and "snapshot_used_to_virtual_percent" in self.model_fields_set:
            _dict['snapshotUsedToVirtualPercent'] = None

        # set to None if total_raw_reserved_mi_b (nullable) is None
        # and model_fields_set contains the field
        if self.total_raw_reserved_mi_b is None and "total_raw_reserved_mi_b" in self.model_fields_set:
            _dict['totalRawReservedMiB'] = None

        # set to None if total_reserved_mi_b (nullable) is None
        # and model_fields_set contains the field
        if self.total_reserved_mi_b is None and "total_reserved_mi_b" in self.model_fields_set:
            _dict['totalReservedMiB'] = None

        # set to None if total_space_mi_b (nullable) is None
        # and model_fields_set contains the field
        if self.total_space_mi_b is None and "total_space_mi_b" in self.model_fields_set:
            _dict['totalSpaceMiB'] = None

        # set to None if used_blocks_mi_b (nullable) is None
        # and model_fields_set contains the field
        if self.used_blocks_mi_b is None and "used_blocks_mi_b" in self.model_fields_set:
            _dict['usedBlocksMiB'] = None

        # set to None if used_capacity (nullable) is None
        # and model_fields_set contains the field
        if self.used_capacity is None and "used_capacity" in self.model_fields_set:
            _dict['usedCapacity'] = None

        # set to None if used_size_mi_b (nullable) is None
        # and model_fields_set contains the field
        if self.used_size_mi_b is None and "used_size_mi_b" in self.model_fields_set:
            _dict['usedSizeMiB'] = None

        # set to None if user_reserved_to_virtual_percent (nullable) is None
        # and model_fields_set contains the field
        if self.user_reserved_to_virtual_percent is None and "user_reserved_to_virtual_percent" in self.model_fields_set:
            _dict['userReservedToVirtualPercent'] = None

        # set to None if user_space (nullable) is None
        # and model_fields_set contains the field
        if self.user_space is None and "user_space" in self.model_fields_set:
            _dict['userSpace'] = None

        # set to None if user_used_to_virtual_percent (nullable) is None
        # and model_fields_set contains the field
        if self.user_used_to_virtual_percent is None and "user_used_to_virtual_percent" in self.model_fields_set:
            _dict['userUsedToVirtualPercent'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4SnapshotCapacity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adminSpace": DeviceType4space.from_dict(obj["adminSpace"]) if obj.get("adminSpace") is not None else None,
            "branchUsedBlocksMiB": obj.get("branchUsedBlocksMiB"),
            "branchVSizeMiB": obj.get("branchVSizeMiB"),
            "compactEfficiency": obj.get("compactEfficiency"),
            "compressionEfficiency": obj.get("compressionEfficiency"),
            "copiedMB": obj.get("copiedMB"),
            "copiedPerc": obj.get("copiedPerc"),
            "ddcSize": obj.get("ddcSize"),
            "ddsSize": obj.get("ddsSize"),
            "dedupSavingsSize": obj.get("dedupSavingsSize"),
            "dedupWrittenSize": obj.get("dedupWrittenSize"),
            "hostWrittenMiB": obj.get("hostWrittenMiB"),
            "hostWrittenToVirtualPercent": obj.get("hostWrittenToVirtualPercent"),
            "sizeMiB": obj.get("sizeMiB"),
            "snapshotTdvvSize": DeviceType4snapshotTdvvsize.from_dict(obj["snapshotTdvvSize"]) if obj.get("snapshotTdvvSize") is not None else None,
            "snapshotUsedToVirtualPercent": obj.get("snapshotUsedToVirtualPercent"),
            "totalRawReservedMiB": obj.get("totalRawReservedMiB"),
            "totalReservedMiB": obj.get("totalReservedMiB"),
            "totalSpaceMiB": obj.get("totalSpaceMiB"),
            "usedBlocksMiB": obj.get("usedBlocksMiB"),
            "usedCapacity": obj.get("usedCapacity"),
            "usedSizeMiB": obj.get("usedSizeMiB"),
            "userReservedToVirtualPercent": obj.get("userReservedToVirtualPercent"),
            "userSpace": DeviceType4space.from_dict(obj["userSpace"]) if obj.get("userSpace") is not None else None,
            "userUsedToVirtualPercent": obj.get("userUsedToVirtualPercent")
        })
        return _obj


