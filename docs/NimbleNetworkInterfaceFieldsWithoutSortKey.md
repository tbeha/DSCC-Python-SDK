# NimbleNetworkInterfaceFieldsWithoutSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | Identifier for the array. A 42 digit hexadecimal number. | [optional] 
**array_name_or_serial** | **str** | Name or serial of the array where the interface is hosted String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**id** | **str** | Identifier for the array. A 42 digit hexadecimal number. | [optional] 
**mac** | **str** | MAC address of the interface. Mac address of an interfaces. | [optional] 

## Example

```python
from dscc.models.nimble_network_interface_fields_without_sort_key import NimbleNetworkInterfaceFieldsWithoutSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNetworkInterfaceFieldsWithoutSortKey from a JSON string
nimble_network_interface_fields_without_sort_key_instance = NimbleNetworkInterfaceFieldsWithoutSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleNetworkInterfaceFieldsWithoutSortKey.to_json())

# convert the object into a dict
nimble_network_interface_fields_without_sort_key_dict = nimble_network_interface_fields_without_sort_key_instance.to_dict()
# create an instance of NimbleNetworkInterfaceFieldsWithoutSortKey from a dict
nimble_network_interface_fields_without_sort_key_from_dict = NimbleNetworkInterfaceFieldsWithoutSortKey.from_dict(nimble_network_interface_fields_without_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


