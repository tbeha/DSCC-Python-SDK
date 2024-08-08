# DeviceType4portFC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_wwn** | **str** | nodeWWN of the FC port | [optional] 
**port_wwn** | **str** | portWWN of the FC port | [optional] 

## Example

```python
from dscc.models.device_type4port_fc import DeviceType4portFC

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4portFC from a JSON string
device_type4port_fc_instance = DeviceType4portFC.from_json(json)
# print the JSON string representation of the object
print(DeviceType4portFC.to_json())

# convert the object into a dict
device_type4port_fc_dict = device_type4port_fc_instance.to_dict()
# create an instance of DeviceType4portFC from a dict
device_type4port_fc_from_dict = DeviceType4portFC.from_dict(device_type4port_fc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


