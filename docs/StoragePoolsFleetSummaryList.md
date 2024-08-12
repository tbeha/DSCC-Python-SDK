# StoragePoolsFleetSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FleetPoolList]**](FleetPoolList.md) |  | [optional] 
**page_limit** | **int** | Page Limit | [optional] 
**page_offset** | **int** | Page Offset | [optional] 
**request_uri** | **str** | resourceUri for detailed storage-pool object | [optional] 
**total** | **int** | Number of storage-pools | [optional] 

## Example

```python
from dscc.models.storage_pools_fleet_summary_list import StoragePoolsFleetSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePoolsFleetSummaryList from a JSON string
storage_pools_fleet_summary_list_instance = StoragePoolsFleetSummaryList.from_json(json)
# print the JSON string representation of the object
print(StoragePoolsFleetSummaryList.to_json())

# convert the object into a dict
storage_pools_fleet_summary_list_dict = storage_pools_fleet_summary_list_instance.to_dict()
# create an instance of StoragePoolsFleetSummaryList from a dict
storage_pools_fleet_summary_list_from_dict = StoragePoolsFleetSummaryList.from_dict(storage_pools_fleet_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


