# DeviceType4NodesSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4nodesList]**](DeviceType4nodesList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed nodes object | [optional] 
**total** | **int** | Number of nodes | [optional] 

## Example

```python
from dscc.models.device_type4_nodes_summary_list import DeviceType4NodesSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4NodesSummaryList from a JSON string
device_type4_nodes_summary_list_instance = DeviceType4NodesSummaryList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4NodesSummaryList.to_json())

# convert the object into a dict
device_type4_nodes_summary_list_dict = device_type4_nodes_summary_list_instance.to_dict()
# create an instance of DeviceType4NodesSummaryList from a dict
device_type4_nodes_summary_list_from_dict = DeviceType4NodesSummaryList.from_dict(device_type4_nodes_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


