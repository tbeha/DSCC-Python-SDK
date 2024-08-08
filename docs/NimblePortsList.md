# NimblePortsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**fibre_channel_interface** | [**NimblePortsListFibreChannelInterface**](NimblePortsListFibreChannelInterface.md) |  | [optional] 
**network_interface** | [**NimblePortsListNetworkInterface**](NimblePortsListNetworkInterface.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for storage port objects | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**total** | **int** | Total number of fibre channel interface and network interface ports. | [optional] 

## Example

```python
from dscc.models.nimble_ports_list import NimblePortsList

# TODO update the JSON string below
json = "{}"
# create an instance of NimblePortsList from a JSON string
nimble_ports_list_instance = NimblePortsList.from_json(json)
# print the JSON string representation of the object
print(NimblePortsList.to_json())

# convert the object into a dict
nimble_ports_list_dict = nimble_ports_list_instance.to_dict()
# create an instance of NimblePortsList from a dict
nimble_ports_list_from_dict = NimblePortsList.from_dict(nimble_ports_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


