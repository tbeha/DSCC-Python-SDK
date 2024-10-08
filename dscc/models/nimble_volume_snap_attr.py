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
from dscc.models.key_value import KeyValue
from typing import Optional, Set
from typing_extensions import Self

class NimbleVolumeSnapAttr(BaseModel):
    """
    Snapshot attributes for snapshots being created as part of snapshot collection creation. List of volumes with per snapshot attributes.
    """ # noqa: E501
    app_uuid: Optional[StrictStr] = Field(default=None, description="Application identifier of snapshots. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed. Defaults to empty string.")
    metadata: Optional[List[Optional[KeyValue]]] = Field(default=None, description="Key-value pairs that augment a volume's attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. Defaults to an empty array.")
    vol_id: Optional[StrictStr] = Field(default=None, description="Identifier of volume. A 42 digit hexadecimal number.")
    __properties: ClassVar[List[str]] = ["app_uuid", "metadata", "vol_id"]

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
        """Create an instance of NimbleVolumeSnapAttr from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item in self.metadata:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metadata'] = _items
        # set to None if app_uuid (nullable) is None
        # and model_fields_set contains the field
        if self.app_uuid is None and "app_uuid" in self.model_fields_set:
            _dict['app_uuid'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if vol_id (nullable) is None
        # and model_fields_set contains the field
        if self.vol_id is None and "vol_id" in self.model_fields_set:
            _dict['vol_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NimbleVolumeSnapAttr from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_uuid": obj.get("app_uuid"),
            "metadata": [KeyValue.from_dict(_item) for _item in obj["metadata"]] if obj.get("metadata") is not None else None,
            "vol_id": obj.get("vol_id")
        })
        return _obj


