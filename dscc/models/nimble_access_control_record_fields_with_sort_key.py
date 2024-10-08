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
from typing import Optional, Set
from typing_extensions import Self

class NimbleAccessControlRecordFieldsWithSortKey(BaseModel):
    """
    NimbleAccessControlRecordFieldsWithSortKey
    """ # noqa: E501
    access_protocol: Optional[StrictStr] = Field(default=None, description="Access protocol of the volume. Possible values:'iscsi', 'fc'. `Filter, Sort`")
    chap_user_id: Optional[StrictStr] = Field(default=None, description="Identifier for the CHAP user. `Filter, Sort`")
    chap_user_name: Optional[StrictStr] = Field(default=None, description="Flag denoting if data in the associated volume should be compressed. `Filter, Sort`")
    creation_time: Optional[StrictInt] = Field(default=None, description="Time when this access control record was created. `Filter, Sort`")
    id: Optional[StrictStr] = Field(default=None, description="Identifier for the access control record. `Filter`")
    initiator_group_id: Optional[StrictStr] = Field(default=None, description="Identifier for the initiator group. `Filter, Sort`")
    initiator_group_name: Optional[StrictStr] = Field(default=None, description="Name of the initiator group. `Filter, Sort` (this argument is deprecated)")
    last_modified: Optional[StrictInt] = Field(default=None, description="Time when this access control record was last modified. `Filter, Sort`")
    lun: Optional[StrictInt] = Field(default=None, description="If this access control record applies to a regular volume, this attribute is the volume's LUN (Logical Unit Number). If the access protocol is iSCSI, the LUN will be 0. However, if the access protocol is Fibre Channel, the LUN will be in the range from 0 to 2047. If this record applies to a Virtual Volume, this attribute is the volume's secondary LUN in the range from 0 to 399999, for both iSCSI and Fibre Channel. If the record applies to a OpenstackV2 volume, the LUN will be in the range from 0 to 2047, for both iSCSI and Fibre Channel. If this record applies to a protocol endpoint or only a snapshot, this attribute is not meaningful and is set to null. `Filter, Sort`")
    pe_id: Optional[StrictStr] = Field(default=None, description="Identifier for the protocol endpoint this access control record applies to. `Filter, Sort`")
    pe_lun: Optional[StrictInt] = Field(default=None, description="LUN (Logical Unit Number) to associate with this protocol endpoint. Valid LUNs are in the 0-2047 range. `Filter, Sort`")
    pe_name: Optional[StrictStr] = Field(default=None, description="Name of the protocol endpoint this access control record applies to. `Filter, Sort`")
    snap_id: Optional[StrictStr] = Field(default=None, description="Identifier for the snapshot this access control record applies to. `Filter, Sort`")
    snap_name: Optional[StrictStr] = Field(default=None, description="Name of the snapshot this access control record applies to. `Filter, Sort`")
    vol_id: Optional[StrictStr] = Field(default=None, description="Identifier for the volume this access control record applies to. `Filter, Sort`")
    vol_name: Optional[StrictStr] = Field(default=None, description="Name of the volume this access control record applies to. `Filter, Sort`")
    __properties: ClassVar[List[str]] = ["access_protocol", "chap_user_id", "chap_user_name", "creation_time", "id", "initiator_group_id", "initiator_group_name", "last_modified", "lun", "pe_id", "pe_lun", "pe_name", "snap_id", "snap_name", "vol_id", "vol_name"]

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
        """Create an instance of NimbleAccessControlRecordFieldsWithSortKey from a JSON string"""
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
        # set to None if access_protocol (nullable) is None
        # and model_fields_set contains the field
        if self.access_protocol is None and "access_protocol" in self.model_fields_set:
            _dict['access_protocol'] = None

        # set to None if chap_user_id (nullable) is None
        # and model_fields_set contains the field
        if self.chap_user_id is None and "chap_user_id" in self.model_fields_set:
            _dict['chap_user_id'] = None

        # set to None if chap_user_name (nullable) is None
        # and model_fields_set contains the field
        if self.chap_user_name is None and "chap_user_name" in self.model_fields_set:
            _dict['chap_user_name'] = None

        # set to None if creation_time (nullable) is None
        # and model_fields_set contains the field
        if self.creation_time is None and "creation_time" in self.model_fields_set:
            _dict['creation_time'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if initiator_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.initiator_group_id is None and "initiator_group_id" in self.model_fields_set:
            _dict['initiator_group_id'] = None

        # set to None if initiator_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.initiator_group_name is None and "initiator_group_name" in self.model_fields_set:
            _dict['initiator_group_name'] = None

        # set to None if last_modified (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified is None and "last_modified" in self.model_fields_set:
            _dict['last_modified'] = None

        # set to None if lun (nullable) is None
        # and model_fields_set contains the field
        if self.lun is None and "lun" in self.model_fields_set:
            _dict['lun'] = None

        # set to None if pe_id (nullable) is None
        # and model_fields_set contains the field
        if self.pe_id is None and "pe_id" in self.model_fields_set:
            _dict['pe_id'] = None

        # set to None if pe_lun (nullable) is None
        # and model_fields_set contains the field
        if self.pe_lun is None and "pe_lun" in self.model_fields_set:
            _dict['pe_lun'] = None

        # set to None if pe_name (nullable) is None
        # and model_fields_set contains the field
        if self.pe_name is None and "pe_name" in self.model_fields_set:
            _dict['pe_name'] = None

        # set to None if snap_id (nullable) is None
        # and model_fields_set contains the field
        if self.snap_id is None and "snap_id" in self.model_fields_set:
            _dict['snap_id'] = None

        # set to None if snap_name (nullable) is None
        # and model_fields_set contains the field
        if self.snap_name is None and "snap_name" in self.model_fields_set:
            _dict['snap_name'] = None

        # set to None if vol_id (nullable) is None
        # and model_fields_set contains the field
        if self.vol_id is None and "vol_id" in self.model_fields_set:
            _dict['vol_id'] = None

        # set to None if vol_name (nullable) is None
        # and model_fields_set contains the field
        if self.vol_name is None and "vol_name" in self.model_fields_set:
            _dict['vol_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleAccessControlRecordFieldsWithSortKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access_protocol": obj.get("access_protocol"),
            "chap_user_id": obj.get("chap_user_id"),
            "chap_user_name": obj.get("chap_user_name"),
            "creation_time": obj.get("creation_time"),
            "id": obj.get("id"),
            "initiator_group_id": obj.get("initiator_group_id"),
            "initiator_group_name": obj.get("initiator_group_name"),
            "last_modified": obj.get("last_modified"),
            "lun": obj.get("lun"),
            "pe_id": obj.get("pe_id"),
            "pe_lun": obj.get("pe_lun"),
            "pe_name": obj.get("pe_name"),
            "snap_id": obj.get("snap_id"),
            "snap_name": obj.get("snap_name"),
            "vol_id": obj.get("vol_id"),
            "vol_name": obj.get("vol_name")
        })
        return _obj


