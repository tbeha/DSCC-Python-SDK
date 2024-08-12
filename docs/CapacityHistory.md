# CapacityHistory

capacity performance trends for given granularity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_data** | [**CapacityHistoryCapacityData**](CapacityHistoryCapacityData.md) |  | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**end_time** | **int** | end time of the capacity history | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**start_time** | **int** | start time of the capacity history | [optional] 

## Example

```python
from dscc.models.capacity_history import CapacityHistory

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityHistory from a JSON string
capacity_history_instance = CapacityHistory.from_json(json)
# print the JSON string representation of the object
print(CapacityHistory.to_json())

# convert the object into a dict
capacity_history_dict = capacity_history_instance.to_dict()
# create an instance of CapacityHistory from a dict
capacity_history_from_dict = CapacityHistory.from_dict(capacity_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


