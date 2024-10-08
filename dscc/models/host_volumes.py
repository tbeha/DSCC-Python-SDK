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

class HostVolumes(BaseModel):
    """
    HostVolumes
    """ # noqa: E501
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    iops: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="IOPS")
    latency_ms: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Latency in ms", alias="latencyMs")
    lun_id: Optional[StrictInt] = Field(default=None, description="lunid", alias="lunId")
    path_count: Optional[StrictInt] = Field(default=None, description="The number of connections from that volume", alias="pathCount")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri of the volume", alias="resourceUri")
    system_id: Optional[StrictStr] = Field(default=None, description="SystemUid of the system associated with the volume", alias="systemId")
    throughput_kbps: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The throughput in kbps", alias="throughputKbps")
    volume_name: Optional[StrictStr] = Field(default=None, description="The name of the volume", alias="volumeName")
    __properties: ClassVar[List[str]] = ["customerId", "iops", "latencyMs", "lunId", "pathCount", "resourceUri", "systemId", "throughputKbps", "volumeName"]

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
        """Create an instance of HostVolumes from a JSON string"""
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
        # set to None if iops (nullable) is None
        # and model_fields_set contains the field
        if self.iops is None and "iops" in self.model_fields_set:
            _dict['iops'] = None

        # set to None if latency_ms (nullable) is None
        # and model_fields_set contains the field
        if self.latency_ms is None and "latency_ms" in self.model_fields_set:
            _dict['latencyMs'] = None

        # set to None if lun_id (nullable) is None
        # and model_fields_set contains the field
        if self.lun_id is None and "lun_id" in self.model_fields_set:
            _dict['lunId'] = None

        # set to None if path_count (nullable) is None
        # and model_fields_set contains the field
        if self.path_count is None and "path_count" in self.model_fields_set:
            _dict['pathCount'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if system_id (nullable) is None
        # and model_fields_set contains the field
        if self.system_id is None and "system_id" in self.model_fields_set:
            _dict['systemId'] = None

        # set to None if throughput_kbps (nullable) is None
        # and model_fields_set contains the field
        if self.throughput_kbps is None and "throughput_kbps" in self.model_fields_set:
            _dict['throughputKbps'] = None

        # set to None if volume_name (nullable) is None
        # and model_fields_set contains the field
        if self.volume_name is None and "volume_name" in self.model_fields_set:
            _dict['volumeName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HostVolumes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customerId": obj.get("customerId"),
            "iops": obj.get("iops"),
            "latencyMs": obj.get("latencyMs"),
            "lunId": obj.get("lunId"),
            "pathCount": obj.get("pathCount"),
            "resourceUri": obj.get("resourceUri"),
            "systemId": obj.get("systemId"),
            "throughputKbps": obj.get("throughputKbps"),
            "volumeName": obj.get("volumeName")
        })
        return _obj


