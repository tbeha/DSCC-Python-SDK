# NodeBatteriesSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NodeBatteriesList]**](NodeBatteriesList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed node battery object | [optional] 
**total** | **int** | Number of node Batteries. | [optional] 

## Example

```python
from dscc.models.node_batteries_summary_list import NodeBatteriesSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of NodeBatteriesSummaryList from a JSON string
node_batteries_summary_list_instance = NodeBatteriesSummaryList.from_json(json)
# print the JSON string representation of the object
print(NodeBatteriesSummaryList.to_json())

# convert the object into a dict
node_batteries_summary_list_dict = node_batteries_summary_list_instance.to_dict()
# create an instance of NodeBatteriesSummaryList from a dict
node_batteries_summary_list_from_dict = NodeBatteriesSummaryList.from_dict(node_batteries_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


