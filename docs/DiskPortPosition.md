# DiskPortPosition

Port Position

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** | node ID | [optional] 
**port** | **int** | port ID | [optional] 
**slot** | **int** | slot ID | [optional] 

## Example

```python
from dscc.models.disk_port_position import DiskPortPosition

# TODO update the JSON string below
json = "{}"
# create an instance of DiskPortPosition from a JSON string
disk_port_position_instance = DiskPortPosition.from_json(json)
# print the JSON string representation of the object
print(DiskPortPosition.to_json())

# convert the object into a dict
disk_port_position_dict = disk_port_position_instance.to_dict()
# create an instance of DiskPortPosition from a dict
disk_port_position_from_dict = DiskPortPosition.from_dict(disk_port_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


