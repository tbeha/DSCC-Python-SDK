# StorageSystemSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[StorageSystemDetailList]**](StorageSystemDetailList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**total** | **int** | Number of systems | [optional] 

## Example

```python
from dscc.models.storage_system_summary_list import StorageSystemSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of StorageSystemSummaryList from a JSON string
storage_system_summary_list_instance = StorageSystemSummaryList.from_json(json)
# print the JSON string representation of the object
print(StorageSystemSummaryList.to_json())

# convert the object into a dict
storage_system_summary_list_dict = storage_system_summary_list_instance.to_dict()
# create an instance of StorageSystemSummaryList from a dict
storage_system_summary_list_from_dict = StorageSystemSummaryList.from_dict(storage_system_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


