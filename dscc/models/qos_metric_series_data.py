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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class QosMetricSeriesData(BaseModel):
    """
    QosMetricSeriesData
    """ # noqa: E501
    bw_limit_kbps: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="throughput threshold at particular timestamp", alias="bwLimitKbps")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    timestampms: Optional[StrictInt] = Field(default=None, description="epoch timestamp")
    type: Optional[StrictStr] = Field(default=None, description="type")
    wqlen: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="wait qlen value at particular timestamp")
    __properties: ClassVar[List[str]] = ["bwLimitKbps", "consoleUri", "generation", "timestampms", "type", "wqlen"]

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
        """Create an instance of QosMetricSeriesData from a JSON string"""
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
        # set to None if bw_limit_kbps (nullable) is None
        # and model_fields_set contains the field
        if self.bw_limit_kbps is None and "bw_limit_kbps" in self.model_fields_set:
            _dict['bwLimitKbps'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if timestampms (nullable) is None
        # and model_fields_set contains the field
        if self.timestampms is None and "timestampms" in self.model_fields_set:
            _dict['timestampms'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if wqlen (nullable) is None
        # and model_fields_set contains the field
        if self.wqlen is None and "wqlen" in self.model_fields_set:
            _dict['wqlen'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QosMetricSeriesData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bwLimitKbps": obj.get("bwLimitKbps"),
            "consoleUri": obj.get("consoleUri"),
            "generation": obj.get("generation"),
            "timestampms": obj.get("timestampms"),
            "type": obj.get("type"),
            "wqlen": obj.get("wqlen")
        })
        return _obj


