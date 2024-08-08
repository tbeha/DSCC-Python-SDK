# DeviceType4HostPathList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4HostPathListObj]**](DeviceType4HostPathListObj.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for HPE Alletra Storage MP Hostpath objects | [optional] 
**total** | **int** | Total number of host paths. | [optional] 

## Example

```python
from dscc.models.device_type4_host_path_list import DeviceType4HostPathList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostPathList from a JSON string
device_type4_host_path_list_instance = DeviceType4HostPathList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostPathList.to_json())

# convert the object into a dict
device_type4_host_path_list_dict = device_type4_host_path_list_instance.to_dict()
# create an instance of DeviceType4HostPathList from a dict
device_type4_host_path_list_from_dict = DeviceType4HostPathList.from_dict(device_type4_host_path_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


