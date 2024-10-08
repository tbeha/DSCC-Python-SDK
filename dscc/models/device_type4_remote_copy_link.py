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
from dscc.models.device_type4_remote_copy_link_port_position import DeviceType4RemoteCopyLinkPortPosition
from typing import Optional, Set
from typing_extensions import Self

class DeviceType4RemoteCopyLink(BaseModel):
    """
    DeviceType4RemoteCopyLink
    """ # noqa: E501
    ipc: Optional[StrictStr] = Field(default=None, description="Name given to the link IPC.", alias="IPC")
    display_name: Optional[StrictStr] = Field(default=None, description="Replication partner link displayname.", alias="displayName")
    domain: Optional[StrictStr] = Field(default=None, description="Domain that the resource belongs to.")
    id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the link")
    name: Optional[StrictStr] = Field(default=None, description="Replication partner link name.")
    partner_name: Optional[StrictStr] = Field(default=None, description="Partner name with which the link is affiliated.", alias="partnerName")
    port: Optional[StrictStr] = Field(default=None, description="Port number.")
    port_pos: Optional[DeviceType4RemoteCopyLinkPortPosition] = Field(default=None, description="Port position of the link", alias="portPos")
    rc_link_id: Optional[StrictInt] = Field(default=None, description="Id of the replication partner link.", alias="rcLinkId")
    remote_address: Optional[StrictStr] = Field(default=None, description="IP address or WWN of the remote link.", alias="remoteAddress")
    remote_id: Optional[StrictStr] = Field(default=None, description="Unique Identifier of the remote partner link", alias="remoteId")
    remote_port_pos: Optional[DeviceType4RemoteCopyLinkPortPosition] = Field(default=None, description="Port position of the remote link", alias="remotePortPos")
    remote_state: Optional[StrictStr] = Field(default=None, description="state of the remote replicatoin partner link.", alias="remoteState")
    remote_status: Optional[StrictStr] = Field(default=None, description="status of the remote replication partner link.", alias="remoteStatus")
    source_address: Optional[StrictStr] = Field(default=None, description="IP address or WWN of the link.", alias="sourceAddress")
    state: Optional[StrictStr] = Field(default=None, description="state of the replication partner link.")
    status: Optional[StrictStr] = Field(default=None, description="status of the replication partner link.")
    system_id: Optional[StrictStr] = Field(default=None, description="Unique ID or serial number of the system.", alias="systemId")
    system_wwn: Optional[StrictStr] = Field(default=None, description="WWN of the system.", alias="systemWWN")
    throughput_k_byte_sec: Optional[StrictInt] = Field(default=None, description="Link throughput in KBytes/sec.", alias="throughputKByteSec")
    type: Optional[StrictInt] = Field(default=None, description="Link type IP or FC.")
    __properties: ClassVar[List[str]] = ["IPC", "displayName", "domain", "id", "name", "partnerName", "port", "portPos", "rcLinkId", "remoteAddress", "remoteId", "remotePortPos", "remoteState", "remoteStatus", "sourceAddress", "state", "status", "systemId", "systemWWN", "throughputKByteSec", "type"]

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
        """Create an instance of DeviceType4RemoteCopyLink from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of port_pos
        if self.port_pos:
            _dict['portPos'] = self.port_pos.to_dict()
        # override the default output from pydantic by calling `to_dict()` of remote_port_pos
        if self.remote_port_pos:
            _dict['remotePortPos'] = self.remote_port_pos.to_dict()
        # set to None if ipc (nullable) is None
        # and model_fields_set contains the field
        if self.ipc is None and "ipc" in self.model_fields_set:
            _dict['IPC'] = None

        # set to None if display_name (nullable) is None
        # and model_fields_set contains the field
        if self.display_name is None and "display_name" in self.model_fields_set:
            _dict['displayName'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if partner_name (nullable) is None
        # and model_fields_set contains the field
        if self.partner_name is None and "partner_name" in self.model_fields_set:
            _dict['partnerName'] = None

        # set to None if port (nullable) is None
        # and model_fields_set contains the field
        if self.port is None and "port" in self.model_fields_set:
            _dict['port'] = None

        # set to None if port_pos (nullable) is None
        # and model_fields_set contains the field
        if self.port_pos is None and "port_pos" in self.model_fields_set:
            _dict['portPos'] = None

        # set to None if rc_link_id (nullable) is None
        # and model_fields_set contains the field
        if self.rc_link_id is None and "rc_link_id" in self.model_fields_set:
            _dict['rcLinkId'] = None

        # set to None if remote_address (nullable) is None
        # and model_fields_set contains the field
        if self.remote_address is None and "remote_address" in self.model_fields_set:
            _dict['remoteAddress'] = None

        # set to None if remote_id (nullable) is None
        # and model_fields_set contains the field
        if self.remote_id is None and "remote_id" in self.model_fields_set:
            _dict['remoteId'] = None

        # set to None if remote_port_pos (nullable) is None
        # and model_fields_set contains the field
        if self.remote_port_pos is None and "remote_port_pos" in self.model_fields_set:
            _dict['remotePortPos'] = None

        # set to None if remote_state (nullable) is None
        # and model_fields_set contains the field
        if self.remote_state is None and "remote_state" in self.model_fields_set:
            _dict['remoteState'] = None

        # set to None if remote_status (nullable) is None
        # and model_fields_set contains the field
        if self.remote_status is None and "remote_status" in self.model_fields_set:
            _dict['remoteStatus'] = None

        # set to None if source_address (nullable) is None
        # and model_fields_set contains the field
        if self.source_address is None and "source_address" in self.model_fields_set:
            _dict['sourceAddress'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if system_id (nullable) is None
        # and model_fields_set contains the field
        if self.system_id is None and "system_id" in self.model_fields_set:
            _dict['systemId'] = None

        # set to None if system_wwn (nullable) is None
        # and model_fields_set contains the field
        if self.system_wwn is None and "system_wwn" in self.model_fields_set:
            _dict['systemWWN'] = None

        # set to None if throughput_k_byte_sec (nullable) is None
        # and model_fields_set contains the field
        if self.throughput_k_byte_sec is None and "throughput_k_byte_sec" in self.model_fields_set:
            _dict['throughputKByteSec'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceType4RemoteCopyLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "IPC": obj.get("IPC"),
            "displayName": obj.get("displayName"),
            "domain": obj.get("domain"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "partnerName": obj.get("partnerName"),
            "port": obj.get("port"),
            "portPos": DeviceType4RemoteCopyLinkPortPosition.from_dict(obj["portPos"]) if obj.get("portPos") is not None else None,
            "rcLinkId": obj.get("rcLinkId"),
            "remoteAddress": obj.get("remoteAddress"),
            "remoteId": obj.get("remoteId"),
            "remotePortPos": DeviceType4RemoteCopyLinkPortPosition.from_dict(obj["remotePortPos"]) if obj.get("remotePortPos") is not None else None,
            "remoteState": obj.get("remoteState"),
            "remoteStatus": obj.get("remoteStatus"),
            "sourceAddress": obj.get("sourceAddress"),
            "state": obj.get("state"),
            "status": obj.get("status"),
            "systemId": obj.get("systemId"),
            "systemWWN": obj.get("systemWWN"),
            "throughputKByteSec": obj.get("throughputKByteSec"),
            "type": obj.get("type")
        })
        return _obj


