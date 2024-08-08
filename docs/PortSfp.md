# PortSfp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fw_version** | **str** | Firmware version | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**qualified** | **bool** | Indicates if the SFP is qualified or not | [optional] 
**rx_loss_pin** | [**RxLossPin**](RxLossPin.md) |  | [optional] 
**rx_power_low** | **bool** | Indicates if RX power is low or not | [optional] 
**speed** | **int** | Speed in bits per second | [optional] 
**state** | [**STATE**](STATE.md) |  | [optional] 
**support_ddm** | **bool** | Indicates if the SFP supports DDM | [optional] 
**tx_disable_pin** | [**TxDisablePin**](TxDisablePin.md) |  | [optional] 
**tx_fault_pin** | [**TxFaultPin**](TxFaultPin.md) |  | [optional] 

## Example

```python
from dscc.models.port_sfp import PortSfp

# TODO update the JSON string below
json = "{}"
# create an instance of PortSfp from a JSON string
port_sfp_instance = PortSfp.from_json(json)
# print the JSON string representation of the object
print(PortSfp.to_json())

# convert the object into a dict
port_sfp_dict = port_sfp_instance.to_dict()
# create an instance of PortSfp from a dict
port_sfp_from_dict = PortSfp.from_dict(port_sfp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


