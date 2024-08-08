# HeadroomResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[HeadroomResources]**](HeadroomResources.md) |  | [optional] 

## Example

```python
from dscc.models.headroom_response import HeadroomResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HeadroomResponse from a JSON string
headroom_response_instance = HeadroomResponse.from_json(json)
# print the JSON string representation of the object
print(HeadroomResponse.to_json())

# convert the object into a dict
headroom_response_dict = headroom_response_instance.to_dict()
# create an instance of HeadroomResponse from a dict
headroom_response_from_dict = HeadroomResponse.from_dict(headroom_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


