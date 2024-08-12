# DeviceType4ApplicationSetsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4ApplicationSets]**](DeviceType4ApplicationSets.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | RequestUri for applicationsets resources | [optional] 
**total** | **int** | Total Number of Application sets. | [optional] 

## Example

```python
from dscc.models.device_type4_application_sets_list import DeviceType4ApplicationSetsList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ApplicationSetsList from a JSON string
device_type4_application_sets_list_instance = DeviceType4ApplicationSetsList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ApplicationSetsList.to_json())

# convert the object into a dict
device_type4_application_sets_list_dict = device_type4_application_sets_list_instance.to_dict()
# create an instance of DeviceType4ApplicationSetsList from a dict
device_type4_application_sets_list_from_dict = DeviceType4ApplicationSetsList.from_dict(device_type4_application_sets_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


