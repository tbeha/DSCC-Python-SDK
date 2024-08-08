# DeviceType4StorageSystemDetailList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[DeviceType4AssociatedLinksInner]**](DeviceType4AssociatedLinksInner.md) | Associated Links Details | [optional] 
**centerplane_type** | **str** | Centerplane type | [optional] 
**chunklet_size_mi_b** | **int** | Size of chunklet in MiB | [optional] 
**cluster_led** | **str** | Cluster LED state | [optional] 
**customer_id** | **str** | customerId | [optional] 
**descriptors** | [**DeviceType4descriptors**](DeviceType4descriptors.md) |  | [optional] 
**device_id** | **int** | Numeric ID of the resource &#x60;Filter&#x60; | [optional] 
**device_type** | [**DeviceType4StorageSystemDetailDeviceType**](DeviceType4StorageSystemDetailDeviceType.md) |  | [optional] 
**displayname** | **str** | Array Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**fqdn** | **str** | Fully qualified domain name of the system | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | SystemWWN/UUID string uniquely identifying the storage system object. &#x60;Filter&#x60; | [optional] 
**in_cluster_nodes** | **List[int]** | IDs of the nodes that are in cluster | [optional] 
**is_fips_enabled** | **bool** | Flag for FIPS | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**maintenance_mode** | [**List[DeviceType4maintenanceModeInner]**](DeviceType4maintenanceModeInner.md) | Maintenance mode details of the system | [optional] 
**manufacturing** | [**DeviceType4manufacturingSys**](DeviceType4manufacturingSys.md) |  | [optional] 
**master_node** | **int** | ID of the master node | [optional] 
**minimum_password_length** | **int** | Minimum length of password for users | [optional] 
**name** | **str** | Name of the resource &#x60;Filter, Sort&#x60; | [optional] 
**network_master_node** | **int** | The Node ID of the current network master &#x60;Filter, Sort&#x60; | [optional] 
**node_memory** | **str** | Node memory size | [optional] 
**nodes_count** | **int** | Number of nodes in the system | [optional] 
**nodes_present** | **List[int]** | IDs of the nodes that are present | [optional] 
**online_nodes** | **List[int]** | IDs of the nodes that are online | [optional] 
**overall_state** | **str** | overallState state derived from enclosure, disk and node state For deviceType1 State derived from ports, enclosure, disk and node state. For deviceType2 state is state reported by deviceType2 array. For deviceType4 state is derived from ports,enclosures,disks,nodes and enclosure-cards. | [optional] 
**overall_state_description** | **str** | Information of hardware resources that are in degraded state. | [optional] 
**parameters** | [**DeviceType4parameters**](DeviceType4parameters.md) |  | [optional] 
**resource_uri** | **str** | resourceUri for detailed storage object | [optional] 
**safe_to_remove** | **bool** | Indicates if the component is safe to remove | [optional] 
**software_versions** | [**DeviceType4softwareVersions**](DeviceType4softwareVersions.md) |  | [optional] 
**state** | [**DeviceType4systemState**](DeviceType4systemState.md) |  | [optional] 
**sys_log_status** | [**DeviceType4sysLogStatus**](DeviceType4sysLogStatus.md) |  | [optional] 
**system_date** | **int** | Current date of the system | [optional] 
**system_headroom** | [**SystemHeadroom**](SystemHeadroom.md) |  | [optional] 
**system_wwn** | **str** | WWN of the array &#x60;Filter, Sort&#x60; | [optional] 
**timezone** | **str** | Current timezone of the system | [optional] 
**type** | **str** | type | [optional] 
**uptime** | [**DeviceType4uptime**](DeviceType4uptime.md) |  | [optional] 
**version** | [**DeviceType4version**](DeviceType4version.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_storage_system_detail_list import DeviceType4StorageSystemDetailList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4StorageSystemDetailList from a JSON string
device_type4_storage_system_detail_list_instance = DeviceType4StorageSystemDetailList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4StorageSystemDetailList.to_json())

# convert the object into a dict
device_type4_storage_system_detail_list_dict = device_type4_storage_system_detail_list_instance.to_dict()
# create an instance of DeviceType4StorageSystemDetailList from a dict
device_type4_storage_system_detail_list_from_dict = DeviceType4StorageSystemDetailList.from_dict(device_type4_storage_system_detail_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


