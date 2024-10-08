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
from dscc.models.descriptors import Descriptors
from dscc.models.device_type4_associated_links_inner import DeviceType4AssociatedLinksInner
from dscc.models.device_type4_storage_system_detail_device_type import DeviceType4StorageSystemDetailDeviceType
from dscc.models.device_type4maintenance_mode_inner import DeviceType4maintenanceModeInner
from dscc.models.manufacturing_single import ManufacturingSingle
from dscc.models.parameters import Parameters
from dscc.models.primera_common_resource_attributes import PrimeraCommonResourceAttributes
from dscc.models.software_versions_solo import SoftwareVersionsSolo
from dscc.models.sys_log_status import SysLogStatus
from dscc.models.system_headroom import SystemHeadroom
from dscc.models.system_state import SystemState
from dscc.models.uptime import Uptime
from dscc.models.version import Version
from typing import Optional, Set
from typing_extensions import Self

class PrimeraStorageSystemDetail(BaseModel):
    """
    PrimeraStorageSystemDetail
    """ # noqa: E501
    associated_links: Optional[List[DeviceType4AssociatedLinksInner]] = Field(default=None, description="Associated Links Details", alias="associatedLinks")
    centerplane_type: Optional[StrictStr] = Field(default=None, description="Centerplane type", alias="centerplaneType")
    chunklet_size_mi_b: Optional[StrictInt] = Field(default=None, description="Size of chunklet in MiB", alias="chunkletSizeMiB")
    cluster_led: Optional[StrictStr] = Field(default=None, description="Cluster LED state", alias="clusterLED")
    common_resource_attributes: Optional[PrimeraCommonResourceAttributes] = Field(default=None, alias="commonResourceAttributes")
    console_uri: Optional[StrictStr] = Field(default=None, description="consoleUri for detailed storage object", alias="consoleUri")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerId", alias="customerId")
    descriptors: Optional[Descriptors] = None
    device_id: Optional[StrictInt] = Field(default=None, description="Numeric ID of the resource", alias="deviceId")
    device_type: Optional[DeviceType4StorageSystemDetailDeviceType] = Field(default=None, alias="deviceType")
    displayname: Optional[StrictStr] = Field(default=None, description="Array Display name")
    domain: Optional[StrictStr] = Field(default=None, description="Domain that the resource belongs to")
    fqdn: Optional[StrictStr] = Field(default=None, description="Fully qualified domain name of the system")
    generation: Optional[StrictInt] = Field(default=None, description="generation")
    id: Optional[StrictStr] = Field(default=None, description="SerialNumber/UUID string uniquely identifying the storage system object.")
    in_cluster_nodes: Optional[List[StrictInt]] = Field(default=None, description="IDs of the nodes that are in cluster", alias="inClusterNodes")
    is_fips_enabled: Optional[StrictBool] = Field(default=None, description="Flag for FIPS", alias="isFIPSEnabled")
    locate_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if the locate beacon is enabled or not", alias="locateEnabled")
    maintenance_mode: Optional[List[DeviceType4maintenanceModeInner]] = Field(default=None, description="Maintenance mode details of the system", alias="maintenanceMode")
    manufacturing: Optional[ManufacturingSingle] = None
    master_node: Optional[StrictInt] = Field(default=None, description="ID of the master node", alias="masterNode")
    minimum_password_length: Optional[StrictInt] = Field(default=None, description="Minimum length of password for users", alias="minimumPasswordLength")
    name: Optional[StrictStr] = Field(default=None, description="Name of the resource")
    network_master_node: Optional[StrictInt] = Field(default=None, description="The Node ID of the current network master", alias="networkMasterNode")
    node_memory: Optional[StrictStr] = Field(default=None, description="Node memory size", alias="nodeMemory")
    nodes_count: Optional[StrictInt] = Field(default=None, description="Number of nodes in the system", alias="nodesCount")
    nodes_present: Optional[List[StrictInt]] = Field(default=None, description="IDs of the nodes that are present", alias="nodesPresent")
    online_nodes: Optional[List[StrictInt]] = Field(default=None, description="IDs of the nodes that are online", alias="onlineNodes")
    parameters: Optional[Parameters] = None
    request_uri: Optional[StrictStr] = Field(default=None, description="requestUri for detailed storage object", alias="requestUri")
    resource_uri: Optional[StrictStr] = Field(default=None, description="resourceUri for detailed storage object", alias="resourceUri")
    safe_to_remove: Optional[StrictBool] = Field(default=None, description="Indicates if the component is safe to remove", alias="safeToRemove")
    software_versions: Optional[SoftwareVersionsSolo] = Field(default=None, alias="softwareVersions")
    state: Optional[SystemState] = None
    sys_log_status: Optional[SysLogStatus] = Field(default=None, alias="sysLogStatus")
    system_date: Optional[StrictInt] = Field(default=None, description="Current date of the system", alias="systemDate")
    system_headroom: Optional[SystemHeadroom] = Field(default=None, alias="systemHeadroom")
    system_wwn: Optional[StrictStr] = Field(default=None, description="WWN of the array.", alias="systemWWN")
    timezone: Optional[StrictStr] = Field(default=None, description="Current timezone of the system.")
    type: Optional[StrictStr] = Field(default=None, description="type")
    uptime: Optional[Uptime] = None
    version: Optional[Version] = None
    __properties: ClassVar[List[str]] = ["associatedLinks", "centerplaneType", "chunkletSizeMiB", "clusterLED", "commonResourceAttributes", "consoleUri", "customerId", "descriptors", "deviceId", "deviceType", "displayname", "domain", "fqdn", "generation", "id", "inClusterNodes", "isFIPSEnabled", "locateEnabled", "maintenanceMode", "manufacturing", "masterNode", "minimumPasswordLength", "name", "networkMasterNode", "nodeMemory", "nodesCount", "nodesPresent", "onlineNodes", "parameters", "requestUri", "resourceUri", "safeToRemove", "softwareVersions", "state", "sysLogStatus", "systemDate", "systemHeadroom", "systemWWN", "timezone", "type", "uptime", "version"]

    @field_validator('cluster_led')
    def cluster_led_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LED_UNKNOWN', 'LED_OFF', 'LED_GREEN', 'LED_GREEN_BLNK', 'LED_AMBER', 'LED_AMBER_BLNK', 'LED_BLUE', 'LED_BLUE_BLNK']):
            raise ValueError("must be one of enum values ('LED_UNKNOWN', 'LED_OFF', 'LED_GREEN', 'LED_GREEN_BLNK', 'LED_AMBER', 'LED_AMBER_BLNK', 'LED_BLUE', 'LED_BLUE_BLNK')")
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
        """Create an instance of PrimeraStorageSystemDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in associated_links (list)
        _items = []
        if self.associated_links:
            for _item in self.associated_links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['associatedLinks'] = _items
        # override the default output from pydantic by calling `to_dict()` of common_resource_attributes
        if self.common_resource_attributes:
            _dict['commonResourceAttributes'] = self.common_resource_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of descriptors
        if self.descriptors:
            _dict['descriptors'] = self.descriptors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device_type
        if self.device_type:
            _dict['deviceType'] = self.device_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in maintenance_mode (list)
        _items = []
        if self.maintenance_mode:
            for _item in self.maintenance_mode:
                if _item:
                    _items.append(_item.to_dict())
            _dict['maintenanceMode'] = _items
        # override the default output from pydantic by calling `to_dict()` of manufacturing
        if self.manufacturing:
            _dict['manufacturing'] = self.manufacturing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of software_versions
        if self.software_versions:
            _dict['softwareVersions'] = self.software_versions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sys_log_status
        if self.sys_log_status:
            _dict['sysLogStatus'] = self.sys_log_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of system_headroom
        if self.system_headroom:
            _dict['systemHeadroom'] = self.system_headroom.to_dict()
        # override the default output from pydantic by calling `to_dict()` of uptime
        if self.uptime:
            _dict['uptime'] = self.uptime.to_dict()
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        # set to None if associated_links (nullable) is None
        # and model_fields_set contains the field
        if self.associated_links is None and "associated_links" in self.model_fields_set:
            _dict['associatedLinks'] = None

        # set to None if centerplane_type (nullable) is None
        # and model_fields_set contains the field
        if self.centerplane_type is None and "centerplane_type" in self.model_fields_set:
            _dict['centerplaneType'] = None

        # set to None if chunklet_size_mi_b (nullable) is None
        # and model_fields_set contains the field
        if self.chunklet_size_mi_b is None and "chunklet_size_mi_b" in self.model_fields_set:
            _dict['chunkletSizeMiB'] = None

        # set to None if common_resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.common_resource_attributes is None and "common_resource_attributes" in self.model_fields_set:
            _dict['commonResourceAttributes'] = None

        # set to None if console_uri (nullable) is None
        # and model_fields_set contains the field
        if self.console_uri is None and "console_uri" in self.model_fields_set:
            _dict['consoleUri'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if descriptors (nullable) is None
        # and model_fields_set contains the field
        if self.descriptors is None and "descriptors" in self.model_fields_set:
            _dict['descriptors'] = None

        # set to None if device_id (nullable) is None
        # and model_fields_set contains the field
        if self.device_id is None and "device_id" in self.model_fields_set:
            _dict['deviceId'] = None

        # set to None if device_type (nullable) is None
        # and model_fields_set contains the field
        if self.device_type is None and "device_type" in self.model_fields_set:
            _dict['deviceType'] = None

        # set to None if displayname (nullable) is None
        # and model_fields_set contains the field
        if self.displayname is None and "displayname" in self.model_fields_set:
            _dict['displayname'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if fqdn (nullable) is None
        # and model_fields_set contains the field
        if self.fqdn is None and "fqdn" in self.model_fields_set:
            _dict['fqdn'] = None

        # set to None if generation (nullable) is None
        # and model_fields_set contains the field
        if self.generation is None and "generation" in self.model_fields_set:
            _dict['generation'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if in_cluster_nodes (nullable) is None
        # and model_fields_set contains the field
        if self.in_cluster_nodes is None and "in_cluster_nodes" in self.model_fields_set:
            _dict['inClusterNodes'] = None

        # set to None if is_fips_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.is_fips_enabled is None and "is_fips_enabled" in self.model_fields_set:
            _dict['isFIPSEnabled'] = None

        # set to None if locate_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.locate_enabled is None and "locate_enabled" in self.model_fields_set:
            _dict['locateEnabled'] = None

        # set to None if maintenance_mode (nullable) is None
        # and model_fields_set contains the field
        if self.maintenance_mode is None and "maintenance_mode" in self.model_fields_set:
            _dict['maintenanceMode'] = None

        # set to None if manufacturing (nullable) is None
        # and model_fields_set contains the field
        if self.manufacturing is None and "manufacturing" in self.model_fields_set:
            _dict['manufacturing'] = None

        # set to None if master_node (nullable) is None
        # and model_fields_set contains the field
        if self.master_node is None and "master_node" in self.model_fields_set:
            _dict['masterNode'] = None

        # set to None if minimum_password_length (nullable) is None
        # and model_fields_set contains the field
        if self.minimum_password_length is None and "minimum_password_length" in self.model_fields_set:
            _dict['minimumPasswordLength'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if network_master_node (nullable) is None
        # and model_fields_set contains the field
        if self.network_master_node is None and "network_master_node" in self.model_fields_set:
            _dict['networkMasterNode'] = None

        # set to None if node_memory (nullable) is None
        # and model_fields_set contains the field
        if self.node_memory is None and "node_memory" in self.model_fields_set:
            _dict['nodeMemory'] = None

        # set to None if nodes_count (nullable) is None
        # and model_fields_set contains the field
        if self.nodes_count is None and "nodes_count" in self.model_fields_set:
            _dict['nodesCount'] = None

        # set to None if nodes_present (nullable) is None
        # and model_fields_set contains the field
        if self.nodes_present is None and "nodes_present" in self.model_fields_set:
            _dict['nodesPresent'] = None

        # set to None if online_nodes (nullable) is None
        # and model_fields_set contains the field
        if self.online_nodes is None and "online_nodes" in self.model_fields_set:
            _dict['onlineNodes'] = None

        # set to None if parameters (nullable) is None
        # and model_fields_set contains the field
        if self.parameters is None and "parameters" in self.model_fields_set:
            _dict['parameters'] = None

        # set to None if request_uri (nullable) is None
        # and model_fields_set contains the field
        if self.request_uri is None and "request_uri" in self.model_fields_set:
            _dict['requestUri'] = None

        # set to None if resource_uri (nullable) is None
        # and model_fields_set contains the field
        if self.resource_uri is None and "resource_uri" in self.model_fields_set:
            _dict['resourceUri'] = None

        # set to None if safe_to_remove (nullable) is None
        # and model_fields_set contains the field
        if self.safe_to_remove is None and "safe_to_remove" in self.model_fields_set:
            _dict['safeToRemove'] = None

        # set to None if software_versions (nullable) is None
        # and model_fields_set contains the field
        if self.software_versions is None and "software_versions" in self.model_fields_set:
            _dict['softwareVersions'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if sys_log_status (nullable) is None
        # and model_fields_set contains the field
        if self.sys_log_status is None and "sys_log_status" in self.model_fields_set:
            _dict['sysLogStatus'] = None

        # set to None if system_date (nullable) is None
        # and model_fields_set contains the field
        if self.system_date is None and "system_date" in self.model_fields_set:
            _dict['systemDate'] = None

        # set to None if system_headroom (nullable) is None
        # and model_fields_set contains the field
        if self.system_headroom is None and "system_headroom" in self.model_fields_set:
            _dict['systemHeadroom'] = None

        # set to None if system_wwn (nullable) is None
        # and model_fields_set contains the field
        if self.system_wwn is None and "system_wwn" in self.model_fields_set:
            _dict['systemWWN'] = None

        # set to None if timezone (nullable) is None
        # and model_fields_set contains the field
        if self.timezone is None and "timezone" in self.model_fields_set:
            _dict['timezone'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if uptime (nullable) is None
        # and model_fields_set contains the field
        if self.uptime is None and "uptime" in self.model_fields_set:
            _dict['uptime'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PrimeraStorageSystemDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedLinks": [DeviceType4AssociatedLinksInner.from_dict(_item) for _item in obj["associatedLinks"]] if obj.get("associatedLinks") is not None else None,
            "centerplaneType": obj.get("centerplaneType"),
            "chunkletSizeMiB": obj.get("chunkletSizeMiB"),
            "clusterLED": obj.get("clusterLED"),
            "commonResourceAttributes": PrimeraCommonResourceAttributes.from_dict(obj["commonResourceAttributes"]) if obj.get("commonResourceAttributes") is not None else None,
            "consoleUri": obj.get("consoleUri"),
            "customerId": obj.get("customerId"),
            "descriptors": Descriptors.from_dict(obj["descriptors"]) if obj.get("descriptors") is not None else None,
            "deviceId": obj.get("deviceId"),
            "deviceType": DeviceType4StorageSystemDetailDeviceType.from_dict(obj["deviceType"]) if obj.get("deviceType") is not None else None,
            "displayname": obj.get("displayname"),
            "domain": obj.get("domain"),
            "fqdn": obj.get("fqdn"),
            "generation": obj.get("generation"),
            "id": obj.get("id"),
            "inClusterNodes": obj.get("inClusterNodes"),
            "isFIPSEnabled": obj.get("isFIPSEnabled"),
            "locateEnabled": obj.get("locateEnabled"),
            "maintenanceMode": [DeviceType4maintenanceModeInner.from_dict(_item) for _item in obj["maintenanceMode"]] if obj.get("maintenanceMode") is not None else None,
            "manufacturing": ManufacturingSingle.from_dict(obj["manufacturing"]) if obj.get("manufacturing") is not None else None,
            "masterNode": obj.get("masterNode"),
            "minimumPasswordLength": obj.get("minimumPasswordLength"),
            "name": obj.get("name"),
            "networkMasterNode": obj.get("networkMasterNode"),
            "nodeMemory": obj.get("nodeMemory"),
            "nodesCount": obj.get("nodesCount"),
            "nodesPresent": obj.get("nodesPresent"),
            "onlineNodes": obj.get("onlineNodes"),
            "parameters": Parameters.from_dict(obj["parameters"]) if obj.get("parameters") is not None else None,
            "requestUri": obj.get("requestUri"),
            "resourceUri": obj.get("resourceUri"),
            "safeToRemove": obj.get("safeToRemove"),
            "softwareVersions": SoftwareVersionsSolo.from_dict(obj["softwareVersions"]) if obj.get("softwareVersions") is not None else None,
            "state": SystemState.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "sysLogStatus": SysLogStatus.from_dict(obj["sysLogStatus"]) if obj.get("sysLogStatus") is not None else None,
            "systemDate": obj.get("systemDate"),
            "systemHeadroom": SystemHeadroom.from_dict(obj["systemHeadroom"]) if obj.get("systemHeadroom") is not None else None,
            "systemWWN": obj.get("systemWWN"),
            "timezone": obj.get("timezone"),
            "type": obj.get("type"),
            "uptime": Uptime.from_dict(obj["uptime"]) if obj.get("uptime") is not None else None,
            "version": Version.from_dict(obj["version"]) if obj.get("version") is not None else None
        })
        return _obj


