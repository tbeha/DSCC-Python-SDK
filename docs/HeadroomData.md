# HeadroomData

List of headroom-utilization metrics based on timestamp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | Write latency in milliseconds | [optional] 
**timestamp_ms** | **int** | Timestamp in epoch milliseconds for which the metrics are listed | [optional] 
**value** | **float** | Read latency in milliseconds | [optional] 

## Example

```python
from dscc.models.headroom_data import HeadroomData

# TODO update the JSON string below
json = "{}"
# create an instance of HeadroomData from a JSON string
headroom_data_instance = HeadroomData.from_json(json)
# print the JSON string representation of the object
print(HeadroomData.to_json())

# convert the object into a dict
headroom_data_dict = headroom_data_instance.to_dict()
# create an instance of HeadroomData from a dict
headroom_data_from_dict = HeadroomData.from_dict(headroom_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


