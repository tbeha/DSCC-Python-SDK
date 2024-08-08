# NimbleHealthStatusWithoutSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | Identifier of the array to which this result belongs. | [optional] 
**context** | **str** | Context for aggregating health check results. Possible values: &#39;all&#39;, &#39;failover&#39;, &#39;sw_update&#39;. | [optional] 
**ctrlr_id** | **str** | Identifier of the controller to which this result belongs. | [optional] 
**id** | **str** | Identifier for the health check. | [optional] 
**scope** | **str** | Scope at which the health check is to be run.Possible values: &#39;controller&#39;, &#39;array&#39;, &#39;group&#39;. | [optional] 

## Example

```python
from dscc.models.nimble_health_status_without_sort_key import NimbleHealthStatusWithoutSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleHealthStatusWithoutSortKey from a JSON string
nimble_health_status_without_sort_key_instance = NimbleHealthStatusWithoutSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleHealthStatusWithoutSortKey.to_json())

# convert the object into a dict
nimble_health_status_without_sort_key_dict = nimble_health_status_without_sort_key_instance.to_dict()
# create an instance of NimbleHealthStatusWithoutSortKey from a dict
nimble_health_status_without_sort_key_from_dict = NimbleHealthStatusWithoutSortKey.from_dict(nimble_health_status_without_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


