# DeviceType4VolumeSetHostGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**host_group_name** | **str** | Host group name | [optional] 
**hosts** | [**List[DeviceType4VolumeSetHostProximityInfo]**](DeviceType4VolumeSetHostProximityInfo.md) |  | [optional] 
**system_id** | **str** | Unique ID or serial number of the system. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.device_type4_volume_set_host_group_list import DeviceType4VolumeSetHostGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VolumeSetHostGroupList from a JSON string
device_type4_volume_set_host_group_list_instance = DeviceType4VolumeSetHostGroupList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VolumeSetHostGroupList.to_json())

# convert the object into a dict
device_type4_volume_set_host_group_list_dict = device_type4_volume_set_host_group_list_instance.to_dict()
# create an instance of DeviceType4VolumeSetHostGroupList from a dict
device_type4_volume_set_host_group_list_from_dict = DeviceType4VolumeSetHostGroupList.from_dict(device_type4_volume_set_host_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


