# NimblevolumeCapacityHistory

volume capacity trends for given granularity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**count** | **int** | count of series data | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**series_data** | [**List[NimblevolumeCapacitySeriesData]**](NimblevolumeCapacitySeriesData.md) |  | [optional] 

## Example

```python
from dscc.models.nimblevolume_capacity_history import NimblevolumeCapacityHistory

# TODO update the JSON string below
json = "{}"
# create an instance of NimblevolumeCapacityHistory from a JSON string
nimblevolume_capacity_history_instance = NimblevolumeCapacityHistory.from_json(json)
# print the JSON string representation of the object
print(NimblevolumeCapacityHistory.to_json())

# convert the object into a dict
nimblevolume_capacity_history_dict = nimblevolume_capacity_history_instance.to_dict()
# create an instance of NimblevolumeCapacityHistory from a dict
nimblevolume_capacity_history_from_dict = NimblevolumeCapacityHistory.from_dict(nimblevolume_capacity_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


