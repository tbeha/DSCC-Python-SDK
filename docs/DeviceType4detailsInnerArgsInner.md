# DeviceType4detailsInnerArgsInner

arguments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch time in milliseconds | [optional] 
**tz** | **str** | Time zone name | [optional] 

## Example

```python
from dscc.models.device_type4details_inner_args_inner import DeviceType4detailsInnerArgsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4detailsInnerArgsInner from a JSON string
device_type4details_inner_args_inner_instance = DeviceType4detailsInnerArgsInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4detailsInnerArgsInner.to_json())

# convert the object into a dict
device_type4details_inner_args_inner_dict = device_type4details_inner_args_inner_instance.to_dict()
# create an instance of DeviceType4detailsInnerArgsInner from a dict
device_type4details_inner_args_inner_from_dict = DeviceType4detailsInnerArgsInner.from_dict(device_type4details_inner_args_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


