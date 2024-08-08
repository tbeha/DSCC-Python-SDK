# PortClearInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_type** | **str** | For RCIP ports, the IP version of the address that needs to be cleared from the port. Either the IPv4 address or IPv6 address or both addresses can be cleared. Possible values: v4,v6,both | [optional] 

## Example

```python
from dscc.models.port_clear_input import PortClearInput

# TODO update the JSON string below
json = "{}"
# create an instance of PortClearInput from a JSON string
port_clear_input_instance = PortClearInput.from_json(json)
# print the JSON string representation of the object
print(PortClearInput.to_json())

# convert the object into a dict
port_clear_input_dict = port_clear_input_instance.to_dict()
# create an instance of PortClearInput from a dict
port_clear_input_from_dict = PortClearInput.from_dict(port_clear_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


