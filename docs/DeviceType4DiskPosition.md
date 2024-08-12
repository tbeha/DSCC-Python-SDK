# DeviceType4diskPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cage** | **int** |  | [optional] 
**disk** | **int** |  | [optional] 
**side** | **str** |  | [optional] 
**sled** | **int** |  | [optional] 

## Example

```python
from dscc.models.device_type4disk_position import DeviceType4diskPosition

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4diskPosition from a JSON string
device_type4disk_position_instance = DeviceType4diskPosition.from_json(json)
# print the JSON string representation of the object
print(DeviceType4diskPosition.to_json())

# convert the object into a dict
device_type4disk_position_dict = device_type4disk_position_instance.to_dict()
# create an instance of DeviceType4diskPosition from a dict
device_type4disk_position_from_dict = DeviceType4diskPosition.from_dict(device_type4disk_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


