# EnclosurePowersSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EnclosurePowersList]**](EnclosurePowersList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure powers object | [optional] 
**total** | **int** | Number of enclosure cards | [optional] 

## Example

```python
from dscc.models.enclosure_powers_summary_list import EnclosurePowersSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosurePowersSummaryList from a JSON string
enclosure_powers_summary_list_instance = EnclosurePowersSummaryList.from_json(json)
# print the JSON string representation of the object
print(EnclosurePowersSummaryList.to_json())

# convert the object into a dict
enclosure_powers_summary_list_dict = enclosure_powers_summary_list_instance.to_dict()
# create an instance of EnclosurePowersSummaryList from a dict
enclosure_powers_summary_list_from_dict = EnclosurePowersSummaryList.from_dict(enclosure_powers_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


