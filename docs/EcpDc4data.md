# EcpDc4data


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_rx_led** | [**LED**](LED.md) |  | [optional] 
**link_tx_led** | [**LED**](LED.md) |  | [optional] 

## Example

```python
from dscc.models.ecp_dc4data import EcpDc4data

# TODO update the JSON string below
json = "{}"
# create an instance of EcpDc4data from a JSON string
ecp_dc4data_instance = EcpDc4data.from_json(json)
# print the JSON string representation of the object
print(EcpDc4data.to_json())

# convert the object into a dict
ecp_dc4data_dict = ecp_dc4data_instance.to_dict()
# create an instance of EcpDc4data from a dict
ecp_dc4data_from_dict = EcpDc4data.from_dict(ecp_dc4data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


