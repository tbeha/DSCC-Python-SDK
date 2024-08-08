# DeviceType4StorageSystemList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4StorageSystemDetailList]**](DeviceType4StorageSystemDetailList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**total** | **int** | Number of systems | [optional] 

## Example

```python
from dscc.models.device_type4_storage_system_list import DeviceType4StorageSystemList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4StorageSystemList from a JSON string
device_type4_storage_system_list_instance = DeviceType4StorageSystemList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4StorageSystemList.to_json())

# convert the object into a dict
device_type4_storage_system_list_dict = device_type4_storage_system_list_instance.to_dict()
# create an instance of DeviceType4StorageSystemList from a dict
device_type4_storage_system_list_from_dict = DeviceType4StorageSystemList.from_dict(device_type4_storage_system_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


