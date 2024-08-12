# NodesMemorySummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NodeMemoriesList]**](NodeMemoriesList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed node memory object | [optional] 
**total** | **int** | Number of node Memories. | [optional] 

## Example

```python
from dscc.models.nodes_memory_summary_list import NodesMemorySummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of NodesMemorySummaryList from a JSON string
nodes_memory_summary_list_instance = NodesMemorySummaryList.from_json(json)
# print the JSON string representation of the object
print(NodesMemorySummaryList.to_json())

# convert the object into a dict
nodes_memory_summary_list_dict = nodes_memory_summary_list_instance.to_dict()
# create an instance of NodesMemorySummaryList from a dict
nodes_memory_summary_list_from_dict = NodesMemorySummaryList.from_dict(nodes_memory_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


