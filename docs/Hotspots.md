# Hotspots

Hotspots response structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**customer_id** | **str** | CustomerId | [optional] 
**end_time** | **float** | End time of the interval for which hotspots are calculated | [optional] 
**hotspots** | [**HotspotsDataPerCategory**](HotspotsDataPerCategory.md) |  | [optional] 
**metric_type** | **str** | Metric which is used to calculate hotspots | [optional] 
**request_uri** | **str** | requestUri for HPE Alletra Storage MP insights hotspots | [optional] 
**resource_type** | **str** | Resource for which hotspots is calculated | [optional] 
**start_time** | **float** | Start time of the interval for which hotspots are calculated | [optional] 
**system_id** | **str** | Serial number of the array | [optional] 

## Example

```python
from dscc.models.hotspots import Hotspots

# TODO update the JSON string below
json = "{}"
# create an instance of Hotspots from a JSON string
hotspots_instance = Hotspots.from_json(json)
# print the JSON string representation of the object
print(Hotspots.to_json())

# convert the object into a dict
hotspots_dict = hotspots_instance.to_dict()
# create an instance of Hotspots from a dict
hotspots_from_dict = Hotspots.from_dict(hotspots_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


