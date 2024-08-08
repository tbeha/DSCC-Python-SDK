# NimbleNIC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_ip** | **str** | Data IP address. | [optional] 
**name** | **str** | Name of NIC. | [optional] 
**subnet_label** | **str** | Subnet label for this NIC. | [optional] 
**tagged** | **bool** | Identify whether the NIC is tagged. | [optional] 

## Example

```python
from dscc.models.nimble_nic import NimbleNIC

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNIC from a JSON string
nimble_nic_instance = NimbleNIC.from_json(json)
# print the JSON string representation of the object
print(NimbleNIC.to_json())

# convert the object into a dict
nimble_nic_dict = nimble_nic_instance.to_dict()
# create an instance of NimbleNIC from a dict
nimble_nic_from_dict = NimbleNIC.from_dict(nimble_nic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


