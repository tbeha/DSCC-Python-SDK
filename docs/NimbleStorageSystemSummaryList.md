# NimbleStorageSystemSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleStorageSystemSummaryListItemsInner]**](NimbleStorageSystemSummaryListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for Nimble storage objects | [optional] 
**total** | **int** | Number of systems | [optional] 

## Example

```python
from dscc.models.nimble_storage_system_summary_list import NimbleStorageSystemSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleStorageSystemSummaryList from a JSON string
nimble_storage_system_summary_list_instance = NimbleStorageSystemSummaryList.from_json(json)
# print the JSON string representation of the object
print(NimbleStorageSystemSummaryList.to_json())

# convert the object into a dict
nimble_storage_system_summary_list_dict = nimble_storage_system_summary_list_instance.to_dict()
# create an instance of NimbleStorageSystemSummaryList from a dict
nimble_storage_system_summary_list_from_dict = NimbleStorageSystemSummaryList.from_dict(nimble_storage_system_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


