# CapacityHistoryCapacityData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | customerId | [optional] 
**items** | [**List[CapacitySeriesData]**](CapacitySeriesData.md) |  | [optional] 
**total** | **int** | count of series data | [optional] 

## Example

```python
from dscc.models.capacity_history_capacity_data import CapacityHistoryCapacityData

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityHistoryCapacityData from a JSON string
capacity_history_capacity_data_instance = CapacityHistoryCapacityData.from_json(json)
# print the JSON string representation of the object
print(CapacityHistoryCapacityData.to_json())

# convert the object into a dict
capacity_history_capacity_data_dict = capacity_history_capacity_data_instance.to_dict()
# create an instance of CapacityHistoryCapacityData from a dict
capacity_history_capacity_data_from_dict = CapacityHistoryCapacityData.from_dict(capacity_history_capacity_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


