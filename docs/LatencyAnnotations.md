# LatencyAnnotations

Volume latency annotations response structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read** | [**List[LatencyAnnotationMetrics]**](LatencyAnnotationMetrics.md) |  | [optional] 
**write** | [**List[LatencyAnnotationMetrics]**](LatencyAnnotationMetrics.md) |  | [optional] 

## Example

```python
from dscc.models.latency_annotations import LatencyAnnotations

# TODO update the JSON string below
json = "{}"
# create an instance of LatencyAnnotations from a JSON string
latency_annotations_instance = LatencyAnnotations.from_json(json)
# print the JSON string representation of the object
print(LatencyAnnotations.to_json())

# convert the object into a dict
latency_annotations_dict = latency_annotations_instance.to_dict()
# create an instance of LatencyAnnotations from a dict
latency_annotations_from_dict = LatencyAnnotations.from_dict(latency_annotations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


