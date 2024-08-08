# DeviceType4EnclosurePowersSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4enclosurePowersList]**](DeviceType4enclosurePowersList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure powers object | [optional] 
**total** | **int** | Number of enclosure cards | [optional] 

## Example

```python
from dscc.models.device_type4_enclosure_powers_summary_list import DeviceType4EnclosurePowersSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosurePowersSummaryList from a JSON string
device_type4_enclosure_powers_summary_list_instance = DeviceType4EnclosurePowersSummaryList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosurePowersSummaryList.to_json())

# convert the object into a dict
device_type4_enclosure_powers_summary_list_dict = device_type4_enclosure_powers_summary_list_instance.to_dict()
# create an instance of DeviceType4EnclosurePowersSummaryList from a dict
device_type4_enclosure_powers_summary_list_from_dict = DeviceType4EnclosurePowersSummaryList.from_dict(device_type4_enclosure_powers_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


