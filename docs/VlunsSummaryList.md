# VlunsSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[VlunsList]**](VlunsList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed vlun object | [optional] 
**total** | **int** | Number of Vluns. | [optional] 

## Example

```python
from dscc.models.vluns_summary_list import VlunsSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of VlunsSummaryList from a JSON string
vluns_summary_list_instance = VlunsSummaryList.from_json(json)
# print the JSON string representation of the object
print(VlunsSummaryList.to_json())

# convert the object into a dict
vluns_summary_list_dict = vluns_summary_list_instance.to_dict()
# create an instance of VlunsSummaryList from a dict
vluns_summary_list_from_dict = VlunsSummaryList.from_dict(vluns_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


