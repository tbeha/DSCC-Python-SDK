# HeadroomUtilization

headroom-utilization response structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_headroom_utilization_data** | [**HeadroomUtilizationAverageHeadroomUtilizationData**](HeadroomUtilizationAverageHeadroomUtilizationData.md) |  | [optional] 
**customer_id** | **str** | CustomerId | [optional] 
**end_time** | **int** | End time of the interval for which headroom-utilization are calculated | [optional] 
**granularity_in_min** | **int** | Time interval granularity in minutes | [optional] 
**headroom_utilization_data** | [**List[HeadroomData]**](HeadroomData.md) |  | [optional] 
**request_uri** | **str** | requestUri for headroom-utilization  | [optional] 
**start_time** | **int** | Start time of the interval for which headroom-utilization are calculated | [optional] 

## Example

```python
from dscc.models.headroom_utilization import HeadroomUtilization

# TODO update the JSON string below
json = "{}"
# create an instance of HeadroomUtilization from a JSON string
headroom_utilization_instance = HeadroomUtilization.from_json(json)
# print the JSON string representation of the object
print(HeadroomUtilization.to_json())

# convert the object into a dict
headroom_utilization_dict = headroom_utilization_instance.to_dict()
# create an instance of HeadroomUtilization from a dict
headroom_utilization_from_dict = HeadroomUtilization.from_dict(headroom_utilization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


