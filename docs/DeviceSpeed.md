# DeviceSpeed

device speed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from dscc.models.device_speed import DeviceSpeed

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSpeed from a JSON string
device_speed_instance = DeviceSpeed.from_json(json)
# print the JSON string representation of the object
print(DeviceSpeed.to_json())

# convert the object into a dict
device_speed_dict = device_speed_instance.to_dict()
# create an instance of DeviceSpeed from a dict
device_speed_from_dict = DeviceSpeed.from_dict(device_speed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


