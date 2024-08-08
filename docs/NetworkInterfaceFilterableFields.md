# NetworkInterfaceFilterableFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | Identifier for the array. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**controller_name** | **str** | Name (A or B) of the controller where the interface is hosted. Plain string. &#x60;Filter&#x60; | [optional] 
**id** | **str** | Identifier for the interface. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of the interface. &#x60;Filter&#x60; | [optional] 

## Example

```python
from dscc.models.network_interface_filterable_fields import NetworkInterfaceFilterableFields

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInterfaceFilterableFields from a JSON string
network_interface_filterable_fields_instance = NetworkInterfaceFilterableFields.from_json(json)
# print the JSON string representation of the object
print(NetworkInterfaceFilterableFields.to_json())

# convert the object into a dict
network_interface_filterable_fields_dict = network_interface_filterable_fields_instance.to_dict()
# create an instance of NetworkInterfaceFilterableFields from a dict
network_interface_filterable_fields_from_dict = NetworkInterfaceFilterableFields.from_dict(network_interface_filterable_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


