# FilterDiskPositionNow

Disk Position Now

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cage** | **int** | cage ID. &#x60;Filter, Sort&#x60; | [optional] 
**disk** | **int** | disk ID. | [optional] 
**side** | **str** | disk side | [optional] 
**sled** | **int** | sled ID. | [optional] 

## Example

```python
from dscc.models.filter_disk_position_now import FilterDiskPositionNow

# TODO update the JSON string below
json = "{}"
# create an instance of FilterDiskPositionNow from a JSON string
filter_disk_position_now_instance = FilterDiskPositionNow.from_json(json)
# print the JSON string representation of the object
print(FilterDiskPositionNow.to_json())

# convert the object into a dict
filter_disk_position_now_dict = filter_disk_position_now_instance.to_dict()
# create an instance of FilterDiskPositionNow from a dict
filter_disk_position_now_from_dict = FilterDiskPositionNow.from_dict(filter_disk_position_now_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


