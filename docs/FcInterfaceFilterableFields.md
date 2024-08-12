# FcInterfaceFilterableFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_name** | **str** | Name (A or B) of the controller where the interface is hosted. Plain string. &#x60;Filter&#x60; | [optional] 
**fc_port_id** | **str** | ID of the port with which the interface is associated. &#x60;Filter&#x60; | [optional] 
**id** | **str** | Identifier for the interface. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of the interface. &#x60;Filter, Sort&#x60; | [optional] 
**wwnn** | **str** | World Wide Node Name for this Fibre Channel interface. &#x60;Filter, Sort&#x60; | [optional] 
**wwpn** | **str** | World Wide Port Name for this Fibre Channel interface. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.fc_interface_filterable_fields import FcInterfaceFilterableFields

# TODO update the JSON string below
json = "{}"
# create an instance of FcInterfaceFilterableFields from a JSON string
fc_interface_filterable_fields_instance = FcInterfaceFilterableFields.from_json(json)
# print the JSON string representation of the object
print(FcInterfaceFilterableFields.to_json())

# convert the object into a dict
fc_interface_filterable_fields_dict = fc_interface_filterable_fields_instance.to_dict()
# create an instance of FcInterfaceFilterableFields from a dict
fc_interface_filterable_fields_from_dict = FcInterfaceFilterableFields.from_dict(fc_interface_filterable_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


