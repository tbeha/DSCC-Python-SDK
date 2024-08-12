# DeviceType4LocateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locate** | **bool** | Indicates if the locate beacon should be enabled or not | [optional] 

## Example

```python
from dscc.models.device_type4_locate_input import DeviceType4LocateInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4LocateInput from a JSON string
device_type4_locate_input_instance = DeviceType4LocateInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4LocateInput.to_json())

# convert the object into a dict
device_type4_locate_input_dict = device_type4_locate_input_instance.to_dict()
# create an instance of DeviceType4LocateInput from a dict
device_type4_locate_input_from_dict = DeviceType4LocateInput.from_dict(device_type4_locate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


