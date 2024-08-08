# CommonResourceAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_state** | **str** | cloud connectivity status of the system where the resource belongs | [optional] 

## Example

```python
from dscc.models.common_resource_attributes import CommonResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResourceAttributes from a JSON string
common_resource_attributes_instance = CommonResourceAttributes.from_json(json)
# print the JSON string representation of the object
print(CommonResourceAttributes.to_json())

# convert the object into a dict
common_resource_attributes_dict = common_resource_attributes_instance.to_dict()
# create an instance of CommonResourceAttributes from a dict
common_resource_attributes_from_dict = CommonResourceAttributes.from_dict(common_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


