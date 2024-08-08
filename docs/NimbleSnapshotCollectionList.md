# NimbleSnapshotCollectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleSnapshotCollection]**](NimbleSnapshotCollection.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for sanpshot collecion objects of a volume collection | [optional] 
**total** | **int** | Total number of snapshot collections associated with a volume collection. | [optional] 

## Example

```python
from dscc.models.nimble_snapshot_collection_list import NimbleSnapshotCollectionList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleSnapshotCollectionList from a JSON string
nimble_snapshot_collection_list_instance = NimbleSnapshotCollectionList.from_json(json)
# print the JSON string representation of the object
print(NimbleSnapshotCollectionList.to_json())

# convert the object into a dict
nimble_snapshot_collection_list_dict = nimble_snapshot_collection_list_instance.to_dict()
# create an instance of NimbleSnapshotCollectionList from a dict
nimble_snapshot_collection_list_from_dict = NimbleSnapshotCollectionList.from_dict(nimble_snapshot_collection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


