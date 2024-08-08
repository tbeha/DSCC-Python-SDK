# CommonResourceProperties

Common properties included in all resource models.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | The customer application identifier | [optional] [readonly] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] [readonly] 
**id** | **str** | An identifier for the resource, usually a UUID. | [optional] [readonly] 
**name** | **str** | A system specified name for the resource. | [optional] 
**resource_uri** | **str** | The &#39;self&#39; reference for this resource. | [optional] [readonly] 
**type** | **str** | The type of resource. | [optional] [readonly] 

## Example

```python
from dscc.models.common_resource_properties import CommonResourceProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResourceProperties from a JSON string
common_resource_properties_instance = CommonResourceProperties.from_json(json)
# print the JSON string representation of the object
print(CommonResourceProperties.to_json())

# convert the object into a dict
common_resource_properties_dict = common_resource_properties_instance.to_dict()
# create an instance of CommonResourceProperties from a dict
common_resource_properties_from_dict = CommonResourceProperties.from_dict(common_resource_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


