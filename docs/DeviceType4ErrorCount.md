# DeviceType4ErrorCount

Number of errors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correctable** | **int** | correctable errors | [optional] 
**uncorrectable** | **int** | uncorrectable errors | [optional] 

## Example

```python
from dscc.models.device_type4_error_count import DeviceType4ErrorCount

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ErrorCount from a JSON string
device_type4_error_count_instance = DeviceType4ErrorCount.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ErrorCount.to_json())

# convert the object into a dict
device_type4_error_count_dict = device_type4_error_count_instance.to_dict()
# create an instance of DeviceType4ErrorCount from a dict
device_type4_error_count_from_dict = DeviceType4ErrorCount.from_dict(device_type4_error_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


