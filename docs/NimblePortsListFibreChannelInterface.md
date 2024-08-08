# NimblePortsListFibreChannelInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimblePortsListFibreChannelInterfaceItemsInner]**](NimblePortsListFibreChannelInterfaceItemsInner.md) |  | [optional] 
**total** | **int** | Total number of fibre channel interface ports. | [optional] 

## Example

```python
from dscc.models.nimble_ports_list_fibre_channel_interface import NimblePortsListFibreChannelInterface

# TODO update the JSON string below
json = "{}"
# create an instance of NimblePortsListFibreChannelInterface from a JSON string
nimble_ports_list_fibre_channel_interface_instance = NimblePortsListFibreChannelInterface.from_json(json)
# print the JSON string representation of the object
print(NimblePortsListFibreChannelInterface.to_json())

# convert the object into a dict
nimble_ports_list_fibre_channel_interface_dict = nimble_ports_list_fibre_channel_interface_instance.to_dict()
# create an instance of NimblePortsListFibreChannelInterface from a dict
nimble_ports_list_fibre_channel_interface_from_dict = NimblePortsListFibreChannelInterface.from_dict(nimble_ports_list_fibre_channel_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


