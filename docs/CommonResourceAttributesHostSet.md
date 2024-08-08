# CommonResourceAttributesHostSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_state** | **str** | Cloud connectivity status of the system where the host set resource belongs | [optional] 

## Example

```python
from dscc.models.common_resource_attributes_host_set import CommonResourceAttributesHostSet

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResourceAttributesHostSet from a JSON string
common_resource_attributes_host_set_instance = CommonResourceAttributesHostSet.from_json(json)
# print the JSON string representation of the object
print(CommonResourceAttributesHostSet.to_json())

# convert the object into a dict
common_resource_attributes_host_set_dict = common_resource_attributes_host_set_instance.to_dict()
# create an instance of CommonResourceAttributesHostSet from a dict
common_resource_attributes_host_set_from_dict = CommonResourceAttributesHostSet.from_dict(common_resource_attributes_host_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


