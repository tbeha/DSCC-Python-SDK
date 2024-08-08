# CommonResourceAttributesPerf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_state** | **str** | Cloud connectivity status of the system to which the resource belongs. | [optional] 

## Example

```python
from dscc.models.common_resource_attributes_perf import CommonResourceAttributesPerf

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResourceAttributesPerf from a JSON string
common_resource_attributes_perf_instance = CommonResourceAttributesPerf.from_json(json)
# print the JSON string representation of the object
print(CommonResourceAttributesPerf.to_json())

# convert the object into a dict
common_resource_attributes_perf_dict = common_resource_attributes_perf_instance.to_dict()
# create an instance of CommonResourceAttributesPerf from a dict
common_resource_attributes_perf_from_dict = CommonResourceAttributesPerf.from_dict(common_resource_attributes_perf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


