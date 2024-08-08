# DeviceType4SwitchPSSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4SwitchPSList]**](DeviceType4SwitchPSList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | resourceUri for detailed switch object | [optional] 
**total** | **int** | Number of switch powersupplies | [optional] 

## Example

```python
from dscc.models.device_type4_switch_ps_summary_list import DeviceType4SwitchPSSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SwitchPSSummaryList from a JSON string
device_type4_switch_ps_summary_list_instance = DeviceType4SwitchPSSummaryList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SwitchPSSummaryList.to_json())

# convert the object into a dict
device_type4_switch_ps_summary_list_dict = device_type4_switch_ps_summary_list_instance.to_dict()
# create an instance of DeviceType4SwitchPSSummaryList from a dict
device_type4_switch_ps_summary_list_from_dict = DeviceType4SwitchPSSummaryList.from_dict(device_type4_switch_ps_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


