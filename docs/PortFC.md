# PortFC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_wwn** | **str** | nodeWWN of the FC port | [optional] 
**port_wwn** | **str** | portWWN of the FC port | [optional] 

## Example

```python
from dscc.models.port_fc import PortFC

# TODO update the JSON string below
json = "{}"
# create an instance of PortFC from a JSON string
port_fc_instance = PortFC.from_json(json)
# print the JSON string representation of the object
print(PortFC.to_json())

# convert the object into a dict
port_fc_dict = port_fc_instance.to_dict()
# create an instance of PortFC from a dict
port_fc_from_dict = PortFC.from_dict(port_fc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


