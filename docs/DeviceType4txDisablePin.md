# DeviceType4txDisablePin

TX disable pin position. If position is HI, TX laser is disabled

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from dscc.models.device_type4tx_disable_pin import DeviceType4txDisablePin

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4txDisablePin from a JSON string
device_type4tx_disable_pin_instance = DeviceType4txDisablePin.from_json(json)
# print the JSON string representation of the object
print(DeviceType4txDisablePin.to_json())

# convert the object into a dict
device_type4tx_disable_pin_dict = device_type4tx_disable_pin_instance.to_dict()
# create an instance of DeviceType4txDisablePin from a dict
device_type4tx_disable_pin_from_dict = DeviceType4txDisablePin.from_dict(device_type4tx_disable_pin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


