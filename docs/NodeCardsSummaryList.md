# NodeCardsSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NodeCardList]**](NodeCardList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed node card object | [optional] 
**total** | **int** | Number of node Cards. | [optional] 

## Example

```python
from dscc.models.node_cards_summary_list import NodeCardsSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of NodeCardsSummaryList from a JSON string
node_cards_summary_list_instance = NodeCardsSummaryList.from_json(json)
# print the JSON string representation of the object
print(NodeCardsSummaryList.to_json())

# convert the object into a dict
node_cards_summary_list_dict = node_cards_summary_list_instance.to_dict()
# create an instance of NodeCardsSummaryList from a dict
node_cards_summary_list_from_dict = NodeCardsSummaryList.from_dict(node_cards_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


