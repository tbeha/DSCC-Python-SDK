# VlunsListSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates if this is an active VLUN or a template | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**device_wwns** | **str** | Device WWNs | [optional] 
**disk_partition** | **str** | Disk partition of host | [optional] 
**displayname** | **str** | SED state | [optional] 
**domain** | **str** | SED state | [optional] 
**failed_path_interval** | **int** | Monitoring interval in seconds after which the host checks for failed paths | [optional] 
**failed_path_policy** | **str** | Failed path monitoring method | [optional] 
**id** | **str** | uid of the vlun | [optional] 
**initiators** | [**DeviceType4VlunsListSingleInitiators**](DeviceType4VlunsListSingleInitiators.md) |  | [optional] 
**lun** | **int** | Exported LUN ID | [optional] 
**mount_point** | **str** | Mount points of devices | [optional] 
**mount_point_fsau** | **int** | File system allocation unit in MiB | [optional] 
**multi_path_type** | **str** | Multi-path method in use | [optional] 
**port_pos** | [**DeviceType4VlunsListSinglePortPos**](DeviceType4VlunsListSinglePortPos.md) |  | [optional] 
**raw_volume** | **str** | Volume that has not been formatted. Yes if it supports | [optional] 
**remote_name** | **str** | Host WWN, iSCSI name, or SAS address; depending on port type | [optional] 
**request_uri** | **str** | requestUri for detailed vlun object | [optional] 
**resource_uri** | **str** | resourceUri for detailed vlun object | [optional] 
**state** | [**DeviceType4VlunsListSingleState**](DeviceType4VlunsListSingleState.md) |  | [optional] 
**status** | **str** | SED state | [optional] 
**system_id** | **str** | SED state | [optional] 
**tpg_id** | **int** | SED state | [optional] 
**type** | **str** | VLUN type | [optional] 
**used_space** | **int** | Host devices used space in MiB | [optional] 
**volume_group** | **str** | Volume group info | [optional] 
**volume_manager** | **str** | Volume Manager tool used | [optional] 
**volume_name** | **str** | Name of exported virtual volume or volume set name | [optional] 
**volume_wwn** | **str** | WWN of exported volume.If a volume set is exported, then this value is null. | [optional] 
**vv_reserved_user_space** | **int** | Volume user reserved space in MiB | [optional] 
**vv_size** | **int** | Size of volume in MiB | [optional] 

## Example

```python
from dscc.models.vluns_list_single import VlunsListSingle

# TODO update the JSON string below
json = "{}"
# create an instance of VlunsListSingle from a JSON string
vluns_list_single_instance = VlunsListSingle.from_json(json)
# print the JSON string representation of the object
print(VlunsListSingle.to_json())

# convert the object into a dict
vluns_list_single_dict = vluns_list_single_instance.to_dict()
# create an instance of VlunsListSingle from a dict
vluns_list_single_from_dict = VlunsListSingle.from_dict(vluns_list_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


