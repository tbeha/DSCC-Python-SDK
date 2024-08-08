# NimbleArrayNet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ctrlr_a_support_ip** | **str** | IP address of controller A. | [optional] 
**ctrlr_b_support_ip** | **str** | IP address of controller B. | [optional] 
**member_gid** | **int** | GID of member. | [optional] 
**name** | **str** | Name of the array. | [optional] 
**nic_list** | [**List[NimbleNIC]**](NimbleNIC.md) | List of NICs. | [optional] 

## Example

```python
from dscc.models.nimble_array_net import NimbleArrayNet

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleArrayNet from a JSON string
nimble_array_net_instance = NimbleArrayNet.from_json(json)
# print the JSON string representation of the object
print(NimbleArrayNet.to_json())

# convert the object into a dict
nimble_array_net_dict = nimble_array_net_instance.to_dict()
# create an instance of NimbleArrayNet from a dict
nimble_array_net_from_dict = NimbleArrayNet.from_dict(nimble_array_net_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


