# SnapshotsSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SnapshotsList]**](SnapshotsList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed snapshots object | [optional] 
**total** | **int** | Number of snapshots | [optional] 

## Example

```python
from dscc.models.snapshots_summary_list import SnapshotsSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotsSummaryList from a JSON string
snapshots_summary_list_instance = SnapshotsSummaryList.from_json(json)
# print the JSON string representation of the object
print(SnapshotsSummaryList.to_json())

# convert the object into a dict
snapshots_summary_list_dict = snapshots_summary_list_instance.to_dict()
# create an instance of SnapshotsSummaryList from a dict
snapshots_summary_list_from_dict = SnapshotsSummaryList.from_dict(snapshots_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


