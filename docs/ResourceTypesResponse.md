# ResourceTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** | Resource types on which the user has a read permission | 

## Example

```python
from dscc.models.resource_types_response import ResourceTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceTypesResponse from a JSON string
resource_types_response_instance = ResourceTypesResponse.from_json(json)
# print the JSON string representation of the object
print(ResourceTypesResponse.to_json())

# convert the object into a dict
resource_types_response_dict = resource_types_response_instance.to_dict()
# create an instance of ResourceTypesResponse from a dict
resource_types_response_from_dict = ResourceTypesResponse.from_dict(resource_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


