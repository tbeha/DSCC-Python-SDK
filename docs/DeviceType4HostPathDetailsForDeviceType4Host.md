# DeviceType4HostPathDetailsForDeviceType4Host


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4HostPathsForDeviceType4Host]**](DeviceType4HostPathsForDeviceType4Host.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Total number of host paths. | [optional] 

## Example

```python
from dscc.models.device_type4_host_path_details_for_device_type4_host import DeviceType4HostPathDetailsForDeviceType4Host

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostPathDetailsForDeviceType4Host from a JSON string
device_type4_host_path_details_for_device_type4_host_instance = DeviceType4HostPathDetailsForDeviceType4Host.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostPathDetailsForDeviceType4Host.to_json())

# convert the object into a dict
device_type4_host_path_details_for_device_type4_host_dict = device_type4_host_path_details_for_device_type4_host_instance.to_dict()
# create an instance of DeviceType4HostPathDetailsForDeviceType4Host from a dict
device_type4_host_path_details_for_device_type4_host_from_dict = DeviceType4HostPathDetailsForDeviceType4Host.from_dict(device_type4_host_path_details_for_device_type4_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


