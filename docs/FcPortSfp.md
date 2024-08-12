# FcPortSfp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fw_version** | **str** |  | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**name** | **str** |  | [optional] 
**qualified** | **bool** |  | [optional] 
**rx_loss_pin** | **str** |  | [optional] 
**rx_power_low** | **bool** |  | [optional] 
**speed** | **int** |  | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**tx_disable_pin** | **str** |  | [optional] 
**tx_fault_pin** | **str** |  | [optional] 

## Example

```python
from dscc.models.fc_port_sfp import FcPortSfp

# TODO update the JSON string below
json = "{}"
# create an instance of FcPortSfp from a JSON string
fc_port_sfp_instance = FcPortSfp.from_json(json)
# print the JSON string representation of the object
print(FcPortSfp.to_json())

# convert the object into a dict
fc_port_sfp_dict = fc_port_sfp_instance.to_dict()
# create an instance of FcPortSfp from a dict
fc_port_sfp_from_dict = FcPortSfp.from_dict(fc_port_sfp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


