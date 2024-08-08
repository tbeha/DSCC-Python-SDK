# NimbleFcInterfaceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bus_location** | **str** | Bus location for the array.String of up to 64 alphanumeric characters | [optional] 
**name** | **str** | Name of the fibre channel config. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**online** | **bool** | Online state of fibre channel config. | [optional] 
**port** | **int** | Port number for this interface.Unsigned 64-bit integer. | [optional] 
**slot** | **int** | Slot number for this fibre channel config. Unsigned 64-bit integer. | [optional] 
**wwnn** | **str** | WWNN (World Wide Node Name) of the Fibre Channel port. | [optional] 
**wwpn** | **str** | WWPN (World Wide Port Name) of the Fibre Channel target port. | [optional] 

## Example

```python
from dscc.models.nimble_fc_interface_list import NimbleFcInterfaceList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFcInterfaceList from a JSON string
nimble_fc_interface_list_instance = NimbleFcInterfaceList.from_json(json)
# print the JSON string representation of the object
print(NimbleFcInterfaceList.to_json())

# convert the object into a dict
nimble_fc_interface_list_dict = nimble_fc_interface_list_instance.to_dict()
# create an instance of NimbleFcInterfaceList from a dict
nimble_fc_interface_list_from_dict = NimbleFcInterfaceList.from_dict(nimble_fc_interface_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


