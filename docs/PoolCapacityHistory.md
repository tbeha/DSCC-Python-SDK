# PoolCapacityHistory

capacity performance trends for given granularity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**count** | **int** | count of series data | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**series_data** | [**List[NimblecapacitySeriesData]**](NimblecapacitySeriesData.md) |  | [optional] 

## Example

```python
from dscc.models.pool_capacity_history import PoolCapacityHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PoolCapacityHistory from a JSON string
pool_capacity_history_instance = PoolCapacityHistory.from_json(json)
# print the JSON string representation of the object
print(PoolCapacityHistory.to_json())

# convert the object into a dict
pool_capacity_history_dict = pool_capacity_history_instance.to_dict()
# create an instance of PoolCapacityHistory from a dict
pool_capacity_history_from_dict = PoolCapacityHistory.from_dict(pool_capacity_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


