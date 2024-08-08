# DeviceType4SwitchPortSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4SwitchPortList]**](DeviceType4SwitchPortList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | resourceUri for detailed switch port object | [optional] 
**total** | **int** | Number of switch Ports | [optional] 

## Example

```python
from dscc.models.device_type4_switch_port_summary_list import DeviceType4SwitchPortSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SwitchPortSummaryList from a JSON string
device_type4_switch_port_summary_list_instance = DeviceType4SwitchPortSummaryList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SwitchPortSummaryList.to_json())

# convert the object into a dict
device_type4_switch_port_summary_list_dict = device_type4_switch_port_summary_list_instance.to_dict()
# create an instance of DeviceType4SwitchPortSummaryList from a dict
device_type4_switch_port_summary_list_from_dict = DeviceType4SwitchPortSummaryList.from_dict(device_type4_switch_port_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


