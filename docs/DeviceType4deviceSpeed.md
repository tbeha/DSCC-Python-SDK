# DeviceType4deviceSpeed

device speed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from dscc.models.device_type4device_speed import DeviceType4deviceSpeed

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4deviceSpeed from a JSON string
device_type4device_speed_instance = DeviceType4deviceSpeed.from_json(json)
# print the JSON string representation of the object
print(DeviceType4deviceSpeed.to_json())

# convert the object into a dict
device_type4device_speed_dict = device_type4device_speed_instance.to_dict()
# create an instance of DeviceType4deviceSpeed from a dict
device_type4device_speed_from_dict = DeviceType4deviceSpeed.from_dict(device_type4device_speed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


