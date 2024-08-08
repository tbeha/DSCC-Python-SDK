# DeviceType4AssociatedLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_uri** | **str** | Resource Uri | [optional] 
**type** | **str** | Resource Name | [optional] 

## Example

```python
from dscc.models.device_type4_associated_links_inner import DeviceType4AssociatedLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4AssociatedLinksInner from a JSON string
device_type4_associated_links_inner_instance = DeviceType4AssociatedLinksInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4AssociatedLinksInner.to_json())

# convert the object into a dict
device_type4_associated_links_inner_dict = device_type4_associated_links_inner_instance.to_dict()
# create an instance of DeviceType4AssociatedLinksInner from a dict
device_type4_associated_links_inner_from_dict = DeviceType4AssociatedLinksInner.from_dict(device_type4_associated_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


