# NimbleNetworkInterfaceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleNetworkInterfaceListItemsInner]**](NimbleNetworkInterfaceListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for  Network Interfaces | [optional] 
**total** | **int** | Total number of Network Interfaces. | [optional] 

## Example

```python
from dscc.models.nimble_network_interface_list import NimbleNetworkInterfaceList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNetworkInterfaceList from a JSON string
nimble_network_interface_list_instance = NimbleNetworkInterfaceList.from_json(json)
# print the JSON string representation of the object
print(NimbleNetworkInterfaceList.to_json())

# convert the object into a dict
nimble_network_interface_list_dict = nimble_network_interface_list_instance.to_dict()
# create an instance of NimbleNetworkInterfaceList from a dict
nimble_network_interface_list_from_dict = NimbleNetworkInterfaceList.from_dict(nimble_network_interface_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


