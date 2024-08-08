# DiskPositionNow

Disk Position Now

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cage** | **int** | cage ID | [optional] 
**disk** | **int** | disk ID | [optional] 
**side** | **str** | disk side | [optional] 
**sled** | **int** | sled ID | [optional] 

## Example

```python
from dscc.models.disk_position_now import DiskPositionNow

# TODO update the JSON string below
json = "{}"
# create an instance of DiskPositionNow from a JSON string
disk_position_now_instance = DiskPositionNow.from_json(json)
# print the JSON string representation of the object
print(DiskPositionNow.to_json())

# convert the object into a dict
disk_position_now_dict = disk_position_now_instance.to_dict()
# create an instance of DiskPositionNow from a dict
disk_position_now_from_dict = DiskPositionNow.from_dict(disk_position_now_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


