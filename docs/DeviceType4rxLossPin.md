# DeviceType4rxLossPin

RX loss pin position. If position is HI, RX loss of signal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from dscc.models.device_type4rx_loss_pin import DeviceType4rxLossPin

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4rxLossPin from a JSON string
device_type4rx_loss_pin_instance = DeviceType4rxLossPin.from_json(json)
# print the JSON string representation of the object
print(DeviceType4rxLossPin.to_json())

# convert the object into a dict
device_type4rx_loss_pin_dict = device_type4rx_loss_pin_instance.to_dict()
# create an instance of DeviceType4rxLossPin from a dict
device_type4rx_loss_pin_from_dict = DeviceType4rxLossPin.from_dict(device_type4rx_loss_pin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


