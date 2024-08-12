# DiskLoop

Disk Loop

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**degraded** | **bool** | degraded loop | [optional] 
**disabled** | **bool** | disabled loop | [optional] 
**port** | [**DiskPortPosition**](DiskPortPosition.md) |  | [optional] 
**primary** | **bool** | primary loop | [optional] 

## Example

```python
from dscc.models.disk_loop import DiskLoop

# TODO update the JSON string below
json = "{}"
# create an instance of DiskLoop from a JSON string
disk_loop_instance = DiskLoop.from_json(json)
# print the JSON string representation of the object
print(DiskLoop.to_json())

# convert the object into a dict
disk_loop_dict = disk_loop_instance.to_dict()
# create an instance of DiskLoop from a dict
disk_loop_from_dict = DiskLoop.from_dict(disk_loop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


