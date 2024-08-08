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
from dscc.models.common_resource_attributes import CommonResourceAttributes
from dscc.models.device_type4_manufacturing_single import DeviceType4ManufacturingSingle
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4enclosureCardTpmDetails(BaseModel):
    """
    DeviceType4enclosureCardTpmDetails
    """ # noqa: E501
    common_resource_attributes: Optional[CommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    displayname: Optional[StrictStr] = Field(default=None, description="Name to be used for display purposes")
    domain: Optional[StrictStr] = Field(default=None, description="Domain that the resource belongs to")
    enclosure_card_id: Optional[StrictInt] = Field(default=None, description="ID of enclosure card.", alias="enclosureCardId")
    enclosure_card_tpm_id: Optional[StrictInt] = Field(default=None, description="ID of enclosure card Tpm Id.", alias="enclosureCardTpmId")
    enclosure_card_tpm_type: Optional[StrictStr] = Field(default=None, description="Enclosure Card Tpm Type.", alias="enclosureCardTpmType")
    enclosure_card_uid: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the enclosure card.", alias="enclosureCardUid")
    enclosure_id: Optional[StrictInt] = Field(default=None, description="ID of the enclosure", alias="enclosureId")
    enclosure_uid: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the enclosure.", alias="enclosureUid")
    family: Optional[StrictStr] = Field(default=None, description="Family of TPM")
    fw_version: Optional[StrictStr] = Field(default=None, description="Firmware Version", alias="fwVersion")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    id: Optional[StrictStr] = Field(default=None, description="id")
    level: Optional[StrictInt] = Field(default=None, description="Level of TPM")
    manufacturing: Optional[DeviceType4ManufacturingSingle] = None
    revision: Optional[StrictStr] = Field(default=None, description="Revision firmware of the TPM card")
    system_id: Optional[StrictStr] = Field(default=None, description="systemId", alias="systemId")
    type: Optional[StrictStr] = Field(default=None, description="type")
    vendor: Optional[StrictStr] = Field(default=None, description="vendor information")
    __properties: ClassVar[List[str]] = ["commonResourceAttributes", "customerId", "displayname", "domain", "enclosureCardId", "enclosureCardTpmId", "enclosureCardTpmType", "enclosureCardUid", "enclosureId", "enclosureUid", "family", "fwVersion", "generation", "id", "level", "manufacturing", "revision", "systemId", "type", "vendor"]

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
        """Create an instance of DeviceType4enclosureCardTpmDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manufacturing
        if self.manufacturing:
            _dict['manufacturing'] = self.manufacturing.to_dict()
        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if enclosure_card_id (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_card_id is None and "enclosure_card_id" in self.model_fields_set:
            _dict['enclosureCardId'] = None

        # set to None if enclosure_card_tpm_id (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_card_tpm_id is None and "enclosure_card_tpm_id" in self.model_fields_set:
            _dict['enclosureCardTpmId'] = None

        # set to None if enclosure_card_tpm_type (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_card_tpm_type is None and "enclosure_card_tpm_type" in self.model_fields_set:
            _dict['enclosureCardTpmType'] = None

        # set to None if enclosure_card_uid (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_card_uid is None and "enclosure_card_uid" in self.model_fields_set:
            _dict['enclosureCardUid'] = None

        # set to None if enclosure_id (nullable) is None
        # and model_fields_set contains the field
        if self.enclosure_id is None and "enclosure_id" in self.model_fields_set:
            _dict['enclosureId'] = None

        # set to None if family (nullable) is None
        # and model_fields_set contains the field
        if self.family is None and "family" in self.model_fields_set:
            _dict['family'] = None

        # set to None if fw_version (nullable) is None
        # and model_fields_set contains the field
        if self.fw_version is None and "fw_version" in self.model_fields_set:
            _dict['fwVersion'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if level (nullable) is None
        # and model_fields_set contains the field
        if self.level is None and "level" in self.model_fields_set:
            _dict['level'] = None

        # set to None if manufacturing (nullable) is None
        # and model_fields_set contains the field
        if self.manufacturing is None and "manufacturing" in self.model_fields_set:
            _dict['manufacturing'] = None

        # set to None if revision (nullable) is None
        # and model_fields_set contains the field
        if self.revision is None and "revision" in self.model_fields_set:
            _dict['revision'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if vendor (nullable) is None
        # and model_fields_set contains the field
        if self.vendor is None and "vendor" in self.model_fields_set:
            _dict['vendor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4enclosureCardTpmDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "commonResourceAttributes": CommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "customerId": obj.get("customerId"),
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "enclosureCardId": obj.get("enclosureCardId"),
            "enclosureCardTpmId": obj.get("enclosureCardTpmId"),
            "enclosureCardTpmType": obj.get("enclosureCardTpmType"),
            "enclosureCardUid": obj.get("enclosureCardUid"),
            "enclosureId": obj.get("enclosureId"),
            "enclosureUid": obj.get("enclosureUid"),
            "family": obj.get("family"),
            "fwVersion": obj.get("fwVersion"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "level": obj.get("level"),
            "manufacturing": DeviceType4ManufacturingSingle.from_dict(obj["manufacturing"]) if obj.get("manufacturing") is not None else None,
            "revision": obj.get("revision"),
            "systemId": obj.get("systemId"),
            "type": obj.get("type"),
            "vendor": obj.get("vendor")
        })
        return _obj


