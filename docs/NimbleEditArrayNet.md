# NimbleEditArrayNet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ctrlr_a_support_ip** | **str** | IP address of controller A. | [optional] 
**ctrlr_b_support_ip** | **str** | IP address of controller B. | [optional] 
**name** | **str** | Name of the array. | [optional] 
**nic_list** | [**List[NimbleNIC]**](NimbleNIC.md) | List of NICs. | [optional] 

## Example

```python
from dscc.models.nimble_edit_array_net import NimbleEditArrayNet

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleEditArrayNet from a JSON string
nimble_edit_array_net_instance = NimbleEditArrayNet.from_json(json)
# print the JSON string representation of the object
print(NimbleEditArrayNet.to_json())

# convert the object into a dict
nimble_edit_array_net_dict = nimble_edit_array_net_instance.to_dict()
# create an instance of NimbleEditArrayNet from a dict
nimble_edit_array_net_from_dict = NimbleEditArrayNet.from_dict(nimble_edit_array_net_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


