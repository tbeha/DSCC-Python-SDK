# TxFaultPin

TX fault pin position. If position is HI, TX fault

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from dscc.models.tx_fault_pin import TxFaultPin

# TODO update the JSON string below
json = "{}"
# create an instance of TxFaultPin from a JSON string
tx_fault_pin_instance = TxFaultPin.from_json(json)
# print the JSON string representation of the object
print(TxFaultPin.to_json())

# convert the object into a dict
tx_fault_pin_dict = tx_fault_pin_instance.to_dict()
# create an instance of TxFaultPin from a dict
tx_fault_pin_from_dict = TxFaultPin.from_dict(tx_fault_pin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


