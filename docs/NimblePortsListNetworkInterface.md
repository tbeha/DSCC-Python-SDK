# NimblePortsListNetworkInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimblePortsListNetworkInterfaceItemsInner]**](NimblePortsListNetworkInterfaceItemsInner.md) |  | [optional] 
**total** | **int** | Total number of network interface ports. | [optional] 

## Example

```python
from dscc.models.nimble_ports_list_network_interface import NimblePortsListNetworkInterface

# TODO update the JSON string below
json = "{}"
# create an instance of NimblePortsListNetworkInterface from a JSON string
nimble_ports_list_network_interface_instance = NimblePortsListNetworkInterface.from_json(json)
# print the JSON string representation of the object
print(NimblePortsListNetworkInterface.to_json())

# convert the object into a dict
nimble_ports_list_network_interface_dict = nimble_ports_list_network_interface_instance.to_dict()
# create an instance of NimblePortsListNetworkInterface from a dict
nimble_ports_list_network_interface_from_dict = NimblePortsListNetworkInterface.from_dict(nimble_ports_list_network_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


