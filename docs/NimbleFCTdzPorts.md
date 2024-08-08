# NimbleFCTdzPorts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_name** | **str** | Unique name of the array. | [optional] 
**fc_name** | **str** | Target port interface name. | [optional] 

## Example

```python
from dscc.models.nimble_fc_tdz_ports import NimbleFCTdzPorts

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFCTdzPorts from a JSON string
nimble_fc_tdz_ports_instance = NimbleFCTdzPorts.from_json(json)
# print the JSON string representation of the object
print(NimbleFCTdzPorts.to_json())

# convert the object into a dict
nimble_fc_tdz_ports_dict = nimble_fc_tdz_ports_instance.to_dict()
# create an instance of NimbleFCTdzPorts from a dict
nimble_fc_tdz_ports_from_dict = NimbleFCTdzPorts.from_dict(nimble_fc_tdz_ports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


