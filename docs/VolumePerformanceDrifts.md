# VolumePerformanceDrifts

Response structure of read and write latency drifts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**drifts_detected** | [**List[DriftsDetectedInner]**](DriftsDetectedInner.md) | Drifts detected in the selected duration | [optional] 
**end_time** | **float** | End time of the drift detection interval | [optional] 
**request_uri** | **str** | requestUri for HPE Alletra Storage MP insights volume latency drift detection | [optional] 
**start_time** | **float** | Start time of the drift detection interval | [optional] 
**system_id** | **str** | Serial number of the array | [optional] 
**tenant_id** | **str** | Customer identification attribute | [optional] 
**timezone** | **str** | timezone | [optional] 
**volume_id** | **str** | This attributes represents volume identification | [optional] 

## Example

```python
from dscc.models.volume_performance_drifts import VolumePerformanceDrifts

# TODO update the JSON string below
json = "{}"
# create an instance of VolumePerformanceDrifts from a JSON string
volume_performance_drifts_instance = VolumePerformanceDrifts.from_json(json)
# print the JSON string representation of the object
print(VolumePerformanceDrifts.to_json())

# convert the object into a dict
volume_performance_drifts_dict = volume_performance_drifts_instance.to_dict()
# create an instance of VolumePerformanceDrifts from a dict
volume_performance_drifts_from_dict = VolumePerformanceDrifts.from_dict(volume_performance_drifts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


