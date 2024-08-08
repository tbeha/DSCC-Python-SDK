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
from typing import Optional, Set
from typing_extensions import Self

class ManufacturingSys(BaseModel):
    """
    Manufacturing information
    """ # noqa: E501
    assembly_rev: Optional[StrictStr] = Field(default=None, description="Assembly revision", alias="assemblyRev")
    check_sum: Optional[StrictStr] = Field(default=None, description="Checksum", alias="checkSum")
    hpe_model_name: Optional[StrictStr] = Field(default=None, description="HPE model name", alias="hpeModelName")
    manufacturer: Optional[StrictStr] = Field(default=None, description="Manufacturer `Filter`")
    model: Optional[StrictStr] = Field(default=None, description="Model `Filter`")
    saleable_part_number: Optional[StrictStr] = Field(default=None, description="Saleable part number", alias="saleablePartNumber")
    saleable_serial_number: Optional[StrictStr] = Field(default=None, description="Saleable serial number", alias="saleableSerialNumber")
    serial_number: Optional[StrictStr] = Field(default=None, description="Serial number `Filter, Sort`", alias="serialNumber")
    spare_part_number: Optional[StrictStr] = Field(default=None, description="Spare part number", alias="sparePartNumber")
    __properties: ClassVar[List[str]] = ["assemblyRev", "checkSum", "hpeModelName", "manufacturer", "model", "saleablePartNumber", "saleableSerialNumber", "serialNumber", "sparePartNumber"]

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
        """Create an instance of ManufacturingSys from a JSON string"""
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
        # set to None if assembly_rev (nullable) is None
        # and model_fields_set contains the field
        if self.assembly_rev is None and "assembly_rev" in self.model_fields_set:
            _dict['assemblyRev'] = None

        # set to None if check_sum (nullable) is None
        # and model_fields_set contains the field
        if self.check_sum is None and "check_sum" in self.model_fields_set:
            _dict['checkSum'] = None

        # set to None if hpe_model_name (nullable) is None
        # and model_fields_set contains the field
        if self.hpe_model_name is None and "hpe_model_name" in self.model_fields_set:
            _dict['hpeModelName'] = None

        # set to None if manufacturer (nullable) is None
        # and model_fields_set contains the field
        if self.manufacturer is None and "manufacturer" in self.model_fields_set:
            _dict['manufacturer'] = None

        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        # set to None if saleable_part_number (nullable) is None
        # and model_fields_set contains the field
        if self.saleable_part_number is None and "saleable_part_number" in self.model_fields_set:
            _dict['saleablePartNumber'] = None

        # set to None if saleable_serial_number (nullable) is None
        # and model_fields_set contains the field
        if self.saleable_serial_number is None and "saleable_serial_number" in self.model_fields_set:
            _dict['saleableSerialNumber'] = None

        # set to None if serial_number (nullable) is None
        # and model_fields_set contains the field
        if self.serial_number is None and "serial_number" in self.model_fields_set:
            _dict['serialNumber'] = None

        # set to None if spare_part_number (nullable) is None
        # and model_fields_set contains the field
        if self.spare_part_number is None and "spare_part_number" in self.model_fields_set:
            _dict['sparePartNumber'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManufacturingSys from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assemblyRev": obj.get("assemblyRev"),
            "checkSum": obj.get("checkSum"),
            "hpeModelName": obj.get("hpeModelName"),
            "manufacturer": obj.get("manufacturer"),
            "model": obj.get("model"),
            "saleablePartNumber": obj.get("saleablePartNumber"),
            "saleableSerialNumber": obj.get("saleableSerialNumber"),
            "serialNumber": obj.get("serialNumber"),
            "sparePartNumber": obj.get("sparePartNumber")
        })
        return _obj


