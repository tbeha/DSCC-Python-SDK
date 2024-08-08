# DeviceType4EnclosureSledsSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4enclosureSledList]**](DeviceType4enclosureSledList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure sleds object | [optional] 
**total** | **int** | Number of enclosure cards | [optional] 

## Example

```python
from dscc.models.device_type4_enclosure_sleds_summary_list import DeviceType4EnclosureSledsSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosureSledsSummaryList from a JSON string
device_type4_enclosure_sleds_summary_list_instance = DeviceType4EnclosureSledsSummaryList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosureSledsSummaryList.to_json())

# convert the object into a dict
device_type4_enclosure_sleds_summary_list_dict = device_type4_enclosure_sleds_summary_list_instance.to_dict()
# create an instance of DeviceType4EnclosureSledsSummaryList from a dict
device_type4_enclosure_sleds_summary_list_from_dict = DeviceType4EnclosureSledsSummaryList.from_dict(device_type4_enclosure_sleds_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


