# FcPortSfpSingle


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
**state** | [**STATE**](STATE.md) |  | [optional] 
**tx_disable_pin** | **str** |  | [optional] 
**tx_fault_pin** | **str** |  | [optional] 

## Example

```python
from dscc.models.fc_port_sfp_single import FcPortSfpSingle

# TODO update the JSON string below
json = "{}"
# create an instance of FcPortSfpSingle from a JSON string
fc_port_sfp_single_instance = FcPortSfpSingle.from_json(json)
# print the JSON string representation of the object
print(FcPortSfpSingle.to_json())

# convert the object into a dict
fc_port_sfp_single_dict = fc_port_sfp_single_instance.to_dict()
# create an instance of FcPortSfpSingle from a dict
fc_port_sfp_single_from_dict = FcPortSfpSingle.from_dict(fc_port_sfp_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


