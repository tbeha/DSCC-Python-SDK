# NimbleSnapshotList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleSnapshot]**](NimbleSnapshot.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for volume snapshot objects | [optional] 
**total** | **int** | Total number of snapshots associated with a volume. | [optional] 

## Example

```python
from dscc.models.nimble_snapshot_list import NimbleSnapshotList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleSnapshotList from a JSON string
nimble_snapshot_list_instance = NimbleSnapshotList.from_json(json)
# print the JSON string representation of the object
print(NimbleSnapshotList.to_json())

# convert the object into a dict
nimble_snapshot_list_dict = nimble_snapshot_list_instance.to_dict()
# create an instance of NimbleSnapshotList from a dict
nimble_snapshot_list_from_dict = NimbleSnapshotList.from_dict(nimble_snapshot_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


