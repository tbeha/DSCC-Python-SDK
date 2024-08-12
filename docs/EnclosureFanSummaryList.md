# EnclosureFanSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EnclosureFanList]**](EnclosureFanList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure fans object | [optional] 
**total** | **int** | Number of enclosure cards | [optional] 

## Example

```python
from dscc.models.enclosure_fan_summary_list import EnclosureFanSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosureFanSummaryList from a JSON string
enclosure_fan_summary_list_instance = EnclosureFanSummaryList.from_json(json)
# print the JSON string representation of the object
print(EnclosureFanSummaryList.to_json())

# convert the object into a dict
enclosure_fan_summary_list_dict = enclosure_fan_summary_list_instance.to_dict()
# create an instance of EnclosureFanSummaryList from a dict
enclosure_fan_summary_list_from_dict = EnclosureFanSummaryList.from_dict(enclosure_fan_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


