# AccessControlsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** | List of user permissions based on the supplied filter in the form of &#39;resource type.permission&#39;.  Ex. volume.create | 

## Example

```python
from dscc.models.access_controls_response import AccessControlsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessControlsResponse from a JSON string
access_controls_response_instance = AccessControlsResponse.from_json(json)
# print the JSON string representation of the object
print(AccessControlsResponse.to_json())

# convert the object into a dict
access_controls_response_dict = access_controls_response_instance.to_dict()
# create an instance of AccessControlsResponse from a dict
access_controls_response_from_dict = AccessControlsResponse.from_dict(access_controls_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


