# PrimeraPoolsSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PrimeraPoolList]**](PrimeraPoolList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | resourceUri for detailed storage-pool object | [optional] 
**total** | **int** | Number of storage-pools | [optional] 

## Example

```python
from dscc.models.primera_pools_summary_list import PrimeraPoolsSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeraPoolsSummaryList from a JSON string
primera_pools_summary_list_instance = PrimeraPoolsSummaryList.from_json(json)
# print the JSON string representation of the object
print(PrimeraPoolsSummaryList.to_json())

# convert the object into a dict
primera_pools_summary_list_dict = primera_pools_summary_list_instance.to_dict()
# create an instance of PrimeraPoolsSummaryList from a dict
primera_pools_summary_list_from_dict = PrimeraPoolsSummaryList.from_dict(primera_pools_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


