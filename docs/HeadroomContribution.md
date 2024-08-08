# HeadroomContribution

system headroom contribution by volumes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**average_headroom_utilization** | [**SystemData**](SystemData.md) |  | [optional] 
**customer_id** | **str** | id specific to the customer | [optional] 
**end_time** | **float** | endTime refers to last/ending period of the interval for which contributors are fetched | [optional] 
**headroom_contribution** | [**HeadroomResponse**](HeadroomResponse.md) |  | [optional] 
**remaining** | [**List[TimeSeriesData]**](TimeSeriesData.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**resource_type** | **str** | Resource type - volumes | [optional] 
**start_time** | **float** | startTime refers to starting period of the interval for which contributors are fetched | [optional] 
**system** | [**List[TimeSeriesData]**](TimeSeriesData.md) |  | [optional] 
**system_id** | **str** | Serial Number of the array | [optional] 

## Example

```python
from dscc.models.headroom_contribution import HeadroomContribution

# TODO update the JSON string below
json = "{}"
# create an instance of HeadroomContribution from a JSON string
headroom_contribution_instance = HeadroomContribution.from_json(json)
# print the JSON string representation of the object
print(HeadroomContribution.to_json())

# convert the object into a dict
headroom_contribution_dict = headroom_contribution_instance.to_dict()
# create an instance of HeadroomContribution from a dict
headroom_contribution_from_dict = HeadroomContribution.from_dict(headroom_contribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


