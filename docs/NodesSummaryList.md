# NodesSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NodesList]**](NodesList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed nodes object | [optional] 
**total** | **int** | Number of nodes | [optional] 

## Example

```python
from dscc.models.nodes_summary_list import NodesSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of NodesSummaryList from a JSON string
nodes_summary_list_instance = NodesSummaryList.from_json(json)
# print the JSON string representation of the object
print(NodesSummaryList.to_json())

# convert the object into a dict
nodes_summary_list_dict = nodes_summary_list_instance.to_dict()
# create an instance of NodesSummaryList from a dict
nodes_summary_list_from_dict = NodesSummaryList.from_dict(nodes_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


