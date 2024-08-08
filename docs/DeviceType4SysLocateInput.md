# DeviceType4SysLocateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locate_enabled** | **bool** | Indicates if the locate beacon should be enabled or not | [optional] 

## Example

```python
from dscc.models.device_type4_sys_locate_input import DeviceType4SysLocateInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SysLocateInput from a JSON string
device_type4_sys_locate_input_instance = DeviceType4SysLocateInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SysLocateInput.to_json())

# convert the object into a dict
device_type4_sys_locate_input_dict = device_type4_sys_locate_input_instance.to_dict()
# create an instance of DeviceType4SysLocateInput from a dict
device_type4_sys_locate_input_from_dict = DeviceType4SysLocateInput.from_dict(device_type4_sys_locate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


