# HotspotsDataPerTimestamp

List of hotspots metrics per timestamp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp_ms** | **float** | Timestamp in epoch milliseconds for which the metrics are listed | [optional] 
**value** | **float** | metric value for example latency value | [optional] 

## Example

```python
from dscc.models.hotspots_data_per_timestamp import HotspotsDataPerTimestamp

# TODO update the JSON string below
json = "{}"
# create an instance of HotspotsDataPerTimestamp from a JSON string
hotspots_data_per_timestamp_instance = HotspotsDataPerTimestamp.from_json(json)
# print the JSON string representation of the object
print(HotspotsDataPerTimestamp.to_json())

# convert the object into a dict
hotspots_data_per_timestamp_dict = hotspots_data_per_timestamp_instance.to_dict()
# create an instance of HotspotsDataPerTimestamp from a dict
hotspots_data_per_timestamp_from_dict = HotspotsDataPerTimestamp.from_dict(hotspots_data_per_timestamp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


