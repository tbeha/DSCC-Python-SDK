# NimbleDisksList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleDisk]**](NimbleDisk.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for disk objects | [optional] 
**total** | **int** | Total number of disks. | [optional] 

## Example

```python
from dscc.models.nimble_disks_list import NimbleDisksList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleDisksList from a JSON string
nimble_disks_list_instance = NimbleDisksList.from_json(json)
# print the JSON string representation of the object
print(NimbleDisksList.to_json())

# convert the object into a dict
nimble_disks_list_dict = nimble_disks_list_instance.to_dict()
# create an instance of NimbleDisksList from a dict
nimble_disks_list_from_dict = NimbleDisksList.from_dict(nimble_disks_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


