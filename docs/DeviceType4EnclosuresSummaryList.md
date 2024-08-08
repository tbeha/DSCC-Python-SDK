# DeviceType4EnclosuresSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4enclosuresList]**](DeviceType4enclosuresList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosures object | [optional] 
**total** | **int** | Number of enclosures | [optional] 

## Example

```python
from dscc.models.device_type4_enclosures_summary_list import DeviceType4EnclosuresSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosuresSummaryList from a JSON string
device_type4_enclosures_summary_list_instance = DeviceType4EnclosuresSummaryList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosuresSummaryList.to_json())

# convert the object into a dict
device_type4_enclosures_summary_list_dict = device_type4_enclosures_summary_list_instance.to_dict()
# create an instance of DeviceType4EnclosuresSummaryList from a dict
device_type4_enclosures_summary_list_from_dict = DeviceType4EnclosuresSummaryList.from_dict(device_type4_enclosures_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


