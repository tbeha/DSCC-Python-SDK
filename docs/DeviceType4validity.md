# DeviceType4validity

The validity of the certificates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch time in milliseconds | [optional] 
**tz** | **str** | Time zone name | [optional] 

## Example

```python
from dscc.models.device_type4validity import DeviceType4validity

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4validity from a JSON string
device_type4validity_instance = DeviceType4validity.from_json(json)
# print the JSON string representation of the object
print(DeviceType4validity.to_json())

# convert the object into a dict
device_type4validity_dict = device_type4validity_instance.to_dict()
# create an instance of DeviceType4validity from a dict
device_type4validity_from_dict = DeviceType4validity.from_dict(device_type4validity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


