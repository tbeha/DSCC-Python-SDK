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
from typing import Optional, Set
from typing_extensions import Self

class PmPerfData(BaseModel):
    """
    Performance metrics average values
    """ # noqa: E501
    avg_of1day: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="last one day avg data", alias="avgOf1day")
    avg_of1hour: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="last one hour avg data", alias="avgOf1hour")
    avg_of8hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="last 8 hours avg data", alias="avgOf8hours")
    avg_of_latest: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="latest perf data", alias="avgOfLatest")
    __properties: ClassVar[List[str]] = ["avgOf1day", "avgOf1hour", "avgOf8hours", "avgOfLatest"]

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
        """Create an instance of PmPerfData from a JSON string"""
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
        # set to None if avg_of1day (nullable) is None
        # and model_fields_set contains the field
        if self.avg_of1day is None and "avg_of1day" in self.model_fields_set:
            _dict['avgOf1day'] = None

        # set to None if avg_of1hour (nullable) is None
        # and model_fields_set contains the field
        if self.avg_of1hour is None and "avg_of1hour" in self.model_fields_set:
            _dict['avgOf1hour'] = None

        # set to None if avg_of8hours (nullable) is None
        # and model_fields_set contains the field
        if self.avg_of8hours is None and "avg_of8hours" in self.model_fields_set:
            _dict['avgOf8hours'] = None

        # set to None if avg_of_latest (nullable) is None
        # and model_fields_set contains the field
        if self.avg_of_latest is None and "avg_of_latest" in self.model_fields_set:
            _dict['avgOfLatest'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PmPerfData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "avgOf1day": obj.get("avgOf1day"),
            "avgOf1hour": obj.get("avgOf1hour"),
            "avgOf8hours": obj.get("avgOf8hours"),
            "avgOfLatest": obj.get("avgOfLatest")
        })
        return _obj


