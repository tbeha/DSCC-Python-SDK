# DeviceType4vlunsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates if this is an active VLUN or a template | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**device_wwns** | **str** | Device WWNs | [optional] 
**disk_partition** | **str** | Disk partition of host | [optional] 
**displayname** | **str** | SED state | [optional] 
**domain** | **str** | SED state | [optional] 
**failed_path_interval** | **int** | Monitoring interval in seconds after which the host checks for failed paths | [optional] 
**failed_path_policy** | **str** | Failed path monitoring method | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | uid of the vlun &#x60;Filter&#x60; | [optional] 
**initiators** | [**DeviceType4VlunsListSingleInitiators**](DeviceType4VlunsListSingleInitiators.md) |  | [optional] 
**lun** | **int** | Exported LUN ID &#x60;Filter, Sort&#x60; | [optional] 
**mount_point** | **str** | Mount points of devices | [optional] 
**mount_point_fsau** | **int** | File system allocation unit in MiB | [optional] 
**multi_path_type** | **str** | Multi-path method in use | [optional] 
**port_pos** | [**DeviceType4vlunsListPortPos**](DeviceType4vlunsListPortPos.md) |  | [optional] 
**raw_volume** | **str** | Volume that has not been formatted. Yes if it supports | [optional] 
**remote_name** | **str** | Host WWN, iSCSI name, or SAS address; depending on port type | [optional] 
**resource_uri** | **str** | resourceUri for detailed vlun object | [optional] 
**state** | [**DeviceType4VlunsListSingleState**](DeviceType4VlunsListSingleState.md) |  | [optional] 
**status** | **str** | SED state | [optional] 
**system_id** | **str** | System Uid &#x60;Filter, Sort&#x60; | [optional] 
**tpg_id** | **int** | SED state | [optional] 
**type** | **str** | type | [optional] 
**used_space** | **int** | Host devices used space in MiB | [optional] 
**vlun_type** | **str** | VLUN type | [optional] 
**volume_group** | **str** | Volume group info | [optional] 
**volume_manager** | **str** | Volume Manager tool used | [optional] 
**volume_name** | **str** | Name of exported virtual volume or volume set name &#x60;Filter, Sort&#x60; | [optional] 
**volume_wwn** | **str** | WWN of exported volume.If a volume set is exported, then this value is null. &#x60;Filter, Sort&#x60; | [optional] 
**vv_reserved_user_space** | **int** | Volume user reserved space in MiB | [optional] 
**vv_size** | **int** | Size of volume in MiB | [optional] 

## Example

```python
from dscc.models.device_type4vluns_list import DeviceType4vlunsList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4vlunsList from a JSON string
device_type4vluns_list_instance = DeviceType4vlunsList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4vlunsList.to_json())

# convert the object into a dict
device_type4vluns_list_dict = device_type4vluns_list_instance.to_dict()
# create an instance of DeviceType4vlunsList from a dict
device_type4vluns_list_from_dict = DeviceType4vlunsList.from_dict(device_type4vluns_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


