# NimbleTargetSubnets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Subnet ID. | [optional] 
**label** | **str** | Subnet label. | [optional] 

## Example

```python
from dscc.models.nimble_target_subnets import NimbleTargetSubnets

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleTargetSubnets from a JSON string
nimble_target_subnets_instance = NimbleTargetSubnets.from_json(json)
# print the JSON string representation of the object
print(NimbleTargetSubnets.to_json())

# convert the object into a dict
nimble_target_subnets_dict = nimble_target_subnets_instance.to_dict()
# create an instance of NimbleTargetSubnets from a dict
nimble_target_subnets_from_dict = NimbleTargetSubnets.from_dict(nimble_target_subnets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


