# NimblePerformancePolicyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimblePerformancePolicyListItemsInner]**](NimblePerformancePolicyListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for Performance Policy objects | [optional] 
**total** | **int** | Total number of Performance Policies. | [optional] 

## Example

```python
from dscc.models.nimble_performance_policy_list import NimblePerformancePolicyList

# TODO update the JSON string below
json = "{}"
# create an instance of NimblePerformancePolicyList from a JSON string
nimble_performance_policy_list_instance = NimblePerformancePolicyList.from_json(json)
# print the JSON string representation of the object
print(NimblePerformancePolicyList.to_json())

# convert the object into a dict
nimble_performance_policy_list_dict = nimble_performance_policy_list_instance.to_dict()
# create an instance of NimblePerformancePolicyList from a dict
nimble_performance_policy_list_from_dict = NimblePerformancePolicyList.from_dict(nimble_performance_policy_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


