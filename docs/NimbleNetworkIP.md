# NimbleNetworkIP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | Associated ip address. | [optional] 
**vlan_id** | **int** | vlan id. | [optional] 

## Example

```python
from dscc.models.nimble_network_ip import NimbleNetworkIP

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNetworkIP from a JSON string
nimble_network_ip_instance = NimbleNetworkIP.from_json(json)
# print the JSON string representation of the object
print(NimbleNetworkIP.to_json())

# convert the object into a dict
nimble_network_ip_dict = nimble_network_ip_instance.to_dict()
# create an instance of NimbleNetworkIP from a dict
nimble_network_ip_from_dict = NimbleNetworkIP.from_dict(nimble_network_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


