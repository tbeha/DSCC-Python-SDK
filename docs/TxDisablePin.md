# TxDisablePin

TX disable pin position. If position is HI, TX laser is disabled

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from dscc.models.tx_disable_pin import TxDisablePin

# TODO update the JSON string below
json = "{}"
# create an instance of TxDisablePin from a JSON string
tx_disable_pin_instance = TxDisablePin.from_json(json)
# print the JSON string representation of the object
print(TxDisablePin.to_json())

# convert the object into a dict
tx_disable_pin_dict = tx_disable_pin_instance.to_dict()
# create an instance of TxDisablePin from a dict
tx_disable_pin_from_dict = TxDisablePin.from_dict(tx_disable_pin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


