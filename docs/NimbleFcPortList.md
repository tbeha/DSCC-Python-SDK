# NimbleFcPortList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bus_location** | **str** | Bus location for the fibre channel config.String of up to 64 alphanumeric characters | [optional] 
**name** | **str** | Name of the fibre channel config. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**port** | **int** | Port number for this fibre channel config.Unsigned 64-bit integer. | [optional] 
**slot** | **int** | Slot number for this fibre channel config. Unsigned 64-bit integer. | [optional] 

## Example

```python
from dscc.models.nimble_fc_port_list import NimbleFcPortList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFcPortList from a JSON string
nimble_fc_port_list_instance = NimbleFcPortList.from_json(json)
# print the JSON string representation of the object
print(NimbleFcPortList.to_json())

# convert the object into a dict
nimble_fc_port_list_dict = nimble_fc_port_list_instance.to_dict()
# create an instance of NimbleFcPortList from a dict
nimble_fc_port_list_from_dict = NimbleFcPortList.from_dict(nimble_fc_port_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


