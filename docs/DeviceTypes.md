# DeviceTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the device family | [optional] 
**device_type** | **str** | Storage Device type | [optional] 

## Example

```python
from dscc.models.device_types import DeviceTypes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceTypes from a JSON string
device_types_instance = DeviceTypes.from_json(json)
# print the JSON string representation of the object
print(DeviceTypes.to_json())

# convert the object into a dict
device_types_dict = device_types_instance.to_dict()
# create an instance of DeviceTypes from a dict
device_types_from_dict = DeviceTypes.from_dict(device_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


