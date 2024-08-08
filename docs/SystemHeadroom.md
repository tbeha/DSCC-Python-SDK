# SystemHeadroom

Headroom for the storage-system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**performance** | [**PerformanceHeadroom**](PerformanceHeadroom.md) |  | [optional] 

## Example

```python
from dscc.models.system_headroom import SystemHeadroom

# TODO update the JSON string below
json = "{}"
# create an instance of SystemHeadroom from a JSON string
system_headroom_instance = SystemHeadroom.from_json(json)
# print the JSON string representation of the object
print(SystemHeadroom.to_json())

# convert the object into a dict
system_headroom_dict = system_headroom_instance.to_dict()
# create an instance of SystemHeadroom from a dict
system_headroom_from_dict = SystemHeadroom.from_dict(system_headroom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


