# NimbleRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** | Gateway IP address. | [optional] 
**tgt_netmask** | **str** | Target network mask. | [optional] 
**tgt_network** | **str** | Target network address. | [optional] 

## Example

```python
from dscc.models.nimble_route import NimbleRoute

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleRoute from a JSON string
nimble_route_instance = NimbleRoute.from_json(json)
# print the JSON string representation of the object
print(NimbleRoute.to_json())

# convert the object into a dict
nimble_route_dict = nimble_route_instance.to_dict()
# create an instance of NimbleRoute from a dict
nimble_route_from_dict = NimbleRoute.from_dict(nimble_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


