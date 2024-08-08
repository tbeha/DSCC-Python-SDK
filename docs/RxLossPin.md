# RxLossPin

RX loss pin position. If position is HI, RX loss of signal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from dscc.models.rx_loss_pin import RxLossPin

# TODO update the JSON string below
json = "{}"
# create an instance of RxLossPin from a JSON string
rx_loss_pin_instance = RxLossPin.from_json(json)
# print the JSON string representation of the object
print(RxLossPin.to_json())

# convert the object into a dict
rx_loss_pin_dict = rx_loss_pin_instance.to_dict()
# create an instance of RxLossPin from a dict
rx_loss_pin_from_dict = RxLossPin.from_dict(rx_loss_pin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


