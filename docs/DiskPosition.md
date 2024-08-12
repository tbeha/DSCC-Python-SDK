# DiskPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cage** | **int** |  | [optional] 
**disk** | **int** |  | [optional] 
**side** | **str** |  | [optional] 
**sled** | **int** |  | [optional] 

## Example

```python
from dscc.models.disk_position import DiskPosition

# TODO update the JSON string below
json = "{}"
# create an instance of DiskPosition from a JSON string
disk_position_instance = DiskPosition.from_json(json)
# print the JSON string representation of the object
print(DiskPosition.to_json())

# convert the object into a dict
disk_position_dict = disk_position_instance.to_dict()
# create an instance of DiskPosition from a dict
disk_position_from_dict = DiskPosition.from_dict(disk_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


