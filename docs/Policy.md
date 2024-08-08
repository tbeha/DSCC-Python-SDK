# Policy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_service** | **bool** |  | [optional] 
**host_dif3par** | **bool** |  | [optional] 
**host_dif_std** | **bool** |  | [optional] 
**no_cache** | **bool** |  | [optional] 
**one_host** | **bool** |  | [optional] 
**stale_snapshot** | **bool** |  | [optional] 
**system** | **bool** |  | [optional] 
**zero_detect** | **bool** |  | [optional] 
**zero_fill** | **bool** |  | [optional] 

## Example

```python
from dscc.models.policy import Policy

# TODO update the JSON string below
json = "{}"
# create an instance of Policy from a JSON string
policy_instance = Policy.from_json(json)
# print the JSON string representation of the object
print(Policy.to_json())

# convert the object into a dict
policy_dict = policy_instance.to_dict()
# create an instance of Policy from a dict
policy_from_dict = Policy.from_dict(policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


