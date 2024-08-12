# DeviceType4portSfp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fw_version** | **str** | Firmware version | [optional] 
**manufacturing** | [**DeviceType4ManufacturingSingle**](DeviceType4ManufacturingSingle.md) |  | [optional] 
**qualified** | **bool** | Indicates if the SFP is qualified or not | [optional] 
**rx_loss_pin** | [**DeviceType4rxLossPin**](DeviceType4rxLossPin.md) |  | [optional] 
**rx_power_low** | **bool** | Indicates if RX power is low or not | [optional] 
**speed** | **int** | Speed in bits per second | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**support_ddm** | **bool** | Indicates if the SFP supports DDM | [optional] 
**tx_disable_pin** | [**DeviceType4txDisablePin**](DeviceType4txDisablePin.md) |  | [optional] 
**tx_fault_pin** | [**DeviceType4txFaultPin**](DeviceType4txFaultPin.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4port_sfp import DeviceType4portSfp

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4portSfp from a JSON string
device_type4port_sfp_instance = DeviceType4portSfp.from_json(json)
# print the JSON string representation of the object
print(DeviceType4portSfp.to_json())

# convert the object into a dict
device_type4port_sfp_dict = device_type4port_sfp_instance.to_dict()
# create an instance of DeviceType4portSfp from a dict
device_type4port_sfp_from_dict = DeviceType4portSfp.from_dict(device_type4port_sfp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


