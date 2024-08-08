# EnclosureExpandersSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EnclosureExpanderList]**](EnclosureExpanderList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure fans object | [optional] 
**total** | **int** | Number of enclosure cards | [optional] 

## Example

```python
from dscc.models.enclosure_expanders_summary_list import EnclosureExpandersSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosureExpandersSummaryList from a JSON string
enclosure_expanders_summary_list_instance = EnclosureExpandersSummaryList.from_json(json)
# print the JSON string representation of the object
print(EnclosureExpandersSummaryList.to_json())

# convert the object into a dict
enclosure_expanders_summary_list_dict = enclosure_expanders_summary_list_instance.to_dict()
# create an instance of EnclosureExpandersSummaryList from a dict
enclosure_expanders_summary_list_from_dict = EnclosureExpandersSummaryList.from_dict(enclosure_expanders_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


