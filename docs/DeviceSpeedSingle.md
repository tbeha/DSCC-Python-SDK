# DeviceSpeedSingle

device speed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from dscc.models.device_speed_single import DeviceSpeedSingle

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSpeedSingle from a JSON string
device_speed_single_instance = DeviceSpeedSingle.from_json(json)
# print the JSON string representation of the object
print(DeviceSpeedSingle.to_json())

# convert the object into a dict
device_speed_single_dict = device_speed_single_instance.to_dict()
# create an instance of DeviceSpeedSingle from a dict
device_speed_single_from_dict = DeviceSpeedSingle.from_dict(device_speed_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


