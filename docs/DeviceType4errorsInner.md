# DeviceType4errorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alarm_code** | **str** | Alarm code | [optional] 
**alarm_text** | **str** |  | [optional] 
**iom** | **str** |  | [optional] 

## Example

```python
from dscc.models.device_type4errors_inner import DeviceType4errorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4errorsInner from a JSON string
device_type4errors_inner_instance = DeviceType4errorsInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4errorsInner.to_json())

# convert the object into a dict
device_type4errors_inner_dict = device_type4errors_inner_instance.to_dict()
# create an instance of DeviceType4errorsInner from a dict
device_type4errors_inner_from_dict = DeviceType4errorsInner.from_dict(device_type4errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


