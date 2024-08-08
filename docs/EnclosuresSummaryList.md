# EnclosuresSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EnclosuresList]**](EnclosuresList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosures object | [optional] 
**total** | **int** | Number of enclosures | [optional] 

## Example

```python
from dscc.models.enclosures_summary_list import EnclosuresSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosuresSummaryList from a JSON string
enclosures_summary_list_instance = EnclosuresSummaryList.from_json(json)
# print the JSON string representation of the object
print(EnclosuresSummaryList.to_json())

# convert the object into a dict
enclosures_summary_list_dict = enclosures_summary_list_instance.to_dict()
# create an instance of EnclosuresSummaryList from a dict
enclosures_summary_list_from_dict = EnclosuresSummaryList.from_dict(enclosures_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


