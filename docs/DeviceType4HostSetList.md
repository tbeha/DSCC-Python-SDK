# DeviceType4HostSetList

List of HPE Alletra Storage MP Host Paths

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4HostSetListObj]**](DeviceType4HostSetListObj.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**total** | **int** | Number of hostsets | [optional] 

## Example

```python
from dscc.models.device_type4_host_set_list import DeviceType4HostSetList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostSetList from a JSON string
device_type4_host_set_list_instance = DeviceType4HostSetList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostSetList.to_json())

# convert the object into a dict
device_type4_host_set_list_dict = device_type4_host_set_list_instance.to_dict()
# create an instance of DeviceType4HostSetList from a dict
device_type4_host_set_list_from_dict = DeviceType4HostSetList.from_dict(device_type4_host_set_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


