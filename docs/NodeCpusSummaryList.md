# NodeCpusSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NodeCpuList]**](NodeCpuList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed node cpu object | [optional] 
**total** | **int** | Number of node Cpus. | [optional] 

## Example

```python
from dscc.models.node_cpus_summary_list import NodeCpusSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of NodeCpusSummaryList from a JSON string
node_cpus_summary_list_instance = NodeCpusSummaryList.from_json(json)
# print the JSON string representation of the object
print(NodeCpusSummaryList.to_json())

# convert the object into a dict
node_cpus_summary_list_dict = node_cpus_summary_list_instance.to_dict()
# create an instance of NodeCpusSummaryList from a dict
node_cpus_summary_list_from_dict = NodeCpusSummaryList.from_dict(node_cpus_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


