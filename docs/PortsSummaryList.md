# PortsSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PortsList]**](PortsList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed ports object | [optional] 
**total** | **int** | Number of ports | [optional] 

## Example

```python
from dscc.models.ports_summary_list import PortsSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of PortsSummaryList from a JSON string
ports_summary_list_instance = PortsSummaryList.from_json(json)
# print the JSON string representation of the object
print(PortsSummaryList.to_json())

# convert the object into a dict
ports_summary_list_dict = ports_summary_list_instance.to_dict()
# create an instance of PortsSummaryList from a dict
ports_summary_list_from_dict = PortsSummaryList.from_dict(ports_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


