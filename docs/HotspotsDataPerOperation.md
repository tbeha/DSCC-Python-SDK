# HotspotsDataPerOperation

Conatins the resource name along with the hotspots metrics per timestamp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_value** | **float** | The max value for metricType and resourceType | [optional] 
**resource_id** | **str** | Id of the resource for which the metrics are listed | [optional] 
**resource_name** | **str** | Name of the resource for which the metrics are listed | [optional] 
**series_data** | [**List[HotspotsDataPerTimestamp]**](HotspotsDataPerTimestamp.md) |  | [optional] 

## Example

```python
from dscc.models.hotspots_data_per_operation import HotspotsDataPerOperation

# TODO update the JSON string below
json = "{}"
# create an instance of HotspotsDataPerOperation from a JSON string
hotspots_data_per_operation_instance = HotspotsDataPerOperation.from_json(json)
# print the JSON string representation of the object
print(HotspotsDataPerOperation.to_json())

# convert the object into a dict
hotspots_data_per_operation_dict = hotspots_data_per_operation_instance.to_dict()
# create an instance of HotspotsDataPerOperation from a dict
hotspots_data_per_operation_from_dict = HotspotsDataPerOperation.from_dict(hotspots_data_per_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


