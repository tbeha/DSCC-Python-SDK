# DeviceType4VolumesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4VolumeDetailsList]**](DeviceType4VolumeDetailsList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed volume object | [optional] 
**total** | **int** | Total number of volumes. | [optional] 

## Example

```python
from dscc.models.device_type4_volumes_list import DeviceType4VolumesList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VolumesList from a JSON string
device_type4_volumes_list_instance = DeviceType4VolumesList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VolumesList.to_json())

# convert the object into a dict
device_type4_volumes_list_dict = device_type4_volumes_list_instance.to_dict()
# create an instance of DeviceType4VolumesList from a dict
device_type4_volumes_list_from_dict = DeviceType4VolumesList.from_dict(device_type4_volumes_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


