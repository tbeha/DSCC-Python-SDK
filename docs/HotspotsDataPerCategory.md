# HotspotsDataPerCategory

Contains the hotspots metrics per operation i.e., read and write

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_hotspots** | [**List[HotspotsDataPerOperation]**](HotspotsDataPerOperation.md) | Contains the list of hotspots metrics for read based on metricType | [optional] 
**write_hotspots** | [**List[HotspotsDataPerOperation]**](HotspotsDataPerOperation.md) | Contains the list of hotspots metrics for write based on metricType | [optional] 

## Example

```python
from dscc.models.hotspots_data_per_category import HotspotsDataPerCategory

# TODO update the JSON string below
json = "{}"
# create an instance of HotspotsDataPerCategory from a JSON string
hotspots_data_per_category_instance = HotspotsDataPerCategory.from_json(json)
# print the JSON string representation of the object
print(HotspotsDataPerCategory.to_json())

# convert the object into a dict
hotspots_data_per_category_dict = hotspots_data_per_category_instance.to_dict()
# create an instance of HotspotsDataPerCategory from a dict
hotspots_data_per_category_from_dict = HotspotsDataPerCategory.from_dict(hotspots_data_per_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


