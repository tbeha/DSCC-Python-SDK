# ResourceReference

References to other resources include the name, type and URI of the other resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**resource_uri** | **str** |  | [readonly] 
**type** | **str** |  | [readonly] 

## Example

```python
from dscc.models.resource_reference import ResourceReference

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceReference from a JSON string
resource_reference_instance = ResourceReference.from_json(json)
# print the JSON string representation of the object
print(ResourceReference.to_json())

# convert the object into a dict
resource_reference_dict = resource_reference_instance.to_dict()
# create an instance of ResourceReference from a dict
resource_reference_from_dict = ResourceReference.from_dict(resource_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


