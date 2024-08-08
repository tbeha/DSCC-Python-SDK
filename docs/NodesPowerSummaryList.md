# NodesPowerSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NodePowerSuppliesList]**](NodePowerSuppliesList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed node power object | [optional] 
**total** | **int** | Number of node power supplies. | [optional] 

## Example

```python
from dscc.models.nodes_power_summary_list import NodesPowerSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of NodesPowerSummaryList from a JSON string
nodes_power_summary_list_instance = NodesPowerSummaryList.from_json(json)
# print the JSON string representation of the object
print(NodesPowerSummaryList.to_json())

# convert the object into a dict
nodes_power_summary_list_dict = nodes_power_summary_list_instance.to_dict()
# create an instance of NodesPowerSummaryList from a dict
nodes_power_summary_list_from_dict = NodesPowerSummaryList.from_dict(nodes_power_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


