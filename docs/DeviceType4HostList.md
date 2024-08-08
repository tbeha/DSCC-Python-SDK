# DeviceType4HostList

List of HPE Alletra Storage MP Host Paths

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4HostListObj]**](DeviceType4HostListObj.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**total** | **int** | Total number of Hosts | [optional] 

## Example

```python
from dscc.models.device_type4_host_list import DeviceType4HostList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostList from a JSON string
device_type4_host_list_instance = DeviceType4HostList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostList.to_json())

# convert the object into a dict
device_type4_host_list_dict = device_type4_host_list_instance.to_dict()
# create an instance of DeviceType4HostList from a dict
device_type4_host_list_from_dict = DeviceType4HostList.from_dict(device_type4_host_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


