# DeviceType4EnclosureCardsSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4enclosureCardList]**](DeviceType4enclosureCardList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure cards object | [optional] 
**total** | **int** | Number of enclosure cards | [optional] 

## Example

```python
from dscc.models.device_type4_enclosure_cards_summary_list import DeviceType4EnclosureCardsSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosureCardsSummaryList from a JSON string
device_type4_enclosure_cards_summary_list_instance = DeviceType4EnclosureCardsSummaryList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosureCardsSummaryList.to_json())

# convert the object into a dict
device_type4_enclosure_cards_summary_list_dict = device_type4_enclosure_cards_summary_list_instance.to_dict()
# create an instance of DeviceType4EnclosureCardsSummaryList from a dict
device_type4_enclosure_cards_summary_list_from_dict = DeviceType4EnclosureCardsSummaryList.from_dict(device_type4_enclosure_cards_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


