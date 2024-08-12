# NimbleNetworkInterfacesWithSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | Identifier for the array. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**array_name_or_serial** | **str** | Name or serial of the array where the interface is hosted String of up to 64 alphanumeric characters, - and . and : are allowed after first character.&#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Identifier for the array. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**mac** | **str** | MAC address of the interface. Mac address of an interface. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.nimble_network_interfaces_with_sort_key import NimbleNetworkInterfacesWithSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNetworkInterfacesWithSortKey from a JSON string
nimble_network_interfaces_with_sort_key_instance = NimbleNetworkInterfacesWithSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleNetworkInterfacesWithSortKey.to_json())

# convert the object into a dict
nimble_network_interfaces_with_sort_key_dict = nimble_network_interfaces_with_sort_key_instance.to_dict()
# create an instance of NimbleNetworkInterfacesWithSortKey from a dict
nimble_network_interfaces_with_sort_key_from_dict = NimbleNetworkInterfacesWithSortKey.from_dict(nimble_network_interfaces_with_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


