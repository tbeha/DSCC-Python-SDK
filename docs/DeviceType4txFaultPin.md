# DeviceType4txFaultPin

TX fault pin position. If position is HI, TX fault

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from dscc.models.device_type4tx_fault_pin import DeviceType4txFaultPin

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4txFaultPin from a JSON string
device_type4tx_fault_pin_instance = DeviceType4txFaultPin.from_json(json)
# print the JSON string representation of the object
print(DeviceType4txFaultPin.to_json())

# convert the object into a dict
device_type4tx_fault_pin_dict = device_type4tx_fault_pin_instance.to_dict()
# create an instance of DeviceType4txFaultPin from a dict
device_type4tx_fault_pin_from_dict = DeviceType4txFaultPin.from_dict(device_type4tx_fault_pin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


