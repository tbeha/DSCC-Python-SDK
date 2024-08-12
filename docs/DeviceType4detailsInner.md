# DeviceType4detailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | [**List[DeviceType4detailsInnerArgsInner]**](DeviceType4detailsInnerArgsInner.md) |  | [optional] 
**default** | **str** | Text in the default language | [optional] 
**key** | **str** | Key of the message | [optional] 

## Example

```python
from dscc.models.device_type4details_inner import DeviceType4detailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4detailsInner from a JSON string
device_type4details_inner_instance = DeviceType4detailsInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4detailsInner.to_json())

# convert the object into a dict
device_type4details_inner_dict = device_type4details_inner_instance.to_dict()
# create an instance of DeviceType4detailsInner from a dict
device_type4details_inner_from_dict = DeviceType4detailsInner.from_dict(device_type4details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


