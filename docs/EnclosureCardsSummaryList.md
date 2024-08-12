# EnclosureCardsSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EnclosureCardList]**](EnclosureCardList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure cards object | [optional] 
**total** | **int** | Number of enclosure cards | [optional] 

## Example

```python
from dscc.models.enclosure_cards_summary_list import EnclosureCardsSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosureCardsSummaryList from a JSON string
enclosure_cards_summary_list_instance = EnclosureCardsSummaryList.from_json(json)
# print the JSON string representation of the object
print(EnclosureCardsSummaryList.to_json())

# convert the object into a dict
enclosure_cards_summary_list_dict = enclosure_cards_summary_list_instance.to_dict()
# create an instance of EnclosureCardsSummaryList from a dict
enclosure_cards_summary_list_from_dict = EnclosureCardsSummaryList.from_dict(enclosure_cards_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


