# VolumeLatencyAnnotations

Volume latency annotations response structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**customer_id** | **str** | CustomerId | [optional] 
**end_time** | **float** | End time of the interval for which annotated points are returned | [optional] 
**latency_annotations** | [**LatencyAnnotations**](LatencyAnnotations.md) |  | [optional] 
**request_uri** | **str** | requestUri for HPE Alletra Storage MP insights volume latency annotations | [optional] 
**start_time** | **float** | Start time of the interval for which annotated points are selected | [optional] 
**system_id** | **str** | Serial number of the array | [optional] 
**volume_id** | **str** | VolumeId | [optional] 

## Example

```python
from dscc.models.volume_latency_annotations import VolumeLatencyAnnotations

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeLatencyAnnotations from a JSON string
volume_latency_annotations_instance = VolumeLatencyAnnotations.from_json(json)
# print the JSON string representation of the object
print(VolumeLatencyAnnotations.to_json())

# convert the object into a dict
volume_latency_annotations_dict = volume_latency_annotations_instance.to_dict()
# create an instance of VolumeLatencyAnnotations from a dict
volume_latency_annotations_from_dict = VolumeLatencyAnnotations.from_dict(volume_latency_annotations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


