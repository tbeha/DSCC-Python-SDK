# NodeMcusSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NodeMcuList]**](NodeMcuList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed node mcu object | [optional] 
**total** | **int** | Number of node Mcus. | [optional] 

## Example

```python
from dscc.models.node_mcus_summary_list import NodeMcusSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of NodeMcusSummaryList from a JSON string
node_mcus_summary_list_instance = NodeMcusSummaryList.from_json(json)
# print the JSON string representation of the object
print(NodeMcusSummaryList.to_json())

# convert the object into a dict
node_mcus_summary_list_dict = node_mcus_summary_list_instance.to_dict()
# create an instance of NodeMcusSummaryList from a dict
node_mcus_summary_list_from_dict = NodeMcusSummaryList.from_dict(node_mcus_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


