# DeviceType4SnapshotSetsSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4snapshotsetsList]**](DeviceType4snapshotsetsList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed snapshots object | [optional] 
**total** | **int** | Number of snapshots | [optional] 

## Example

```python
from dscc.models.device_type4_snapshot_sets_summary_list import DeviceType4SnapshotSetsSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SnapshotSetsSummaryList from a JSON string
device_type4_snapshot_sets_summary_list_instance = DeviceType4SnapshotSetsSummaryList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SnapshotSetsSummaryList.to_json())

# convert the object into a dict
device_type4_snapshot_sets_summary_list_dict = device_type4_snapshot_sets_summary_list_instance.to_dict()
# create an instance of DeviceType4SnapshotSetsSummaryList from a dict
device_type4_snapshot_sets_summary_list_from_dict = DeviceType4SnapshotSetsSummaryList.from_dict(device_type4_snapshot_sets_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


