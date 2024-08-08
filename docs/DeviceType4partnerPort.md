# DeviceType4partnerPort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_wwn_or_name** | **str** | Node WWN (for FC) or iSCSI name (for iSCSI) | [optional] 
**port_wwn_or_ip** | **str** | Port WWN (for FC) or IP address (for iSCSI) | [optional] 
**position** | [**DeviceType4partnerPortPosition**](DeviceType4partnerPortPosition.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4partner_port import DeviceType4partnerPort

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4partnerPort from a JSON string
device_type4partner_port_instance = DeviceType4partnerPort.from_json(json)
# print the JSON string representation of the object
print(DeviceType4partnerPort.to_json())

# convert the object into a dict
device_type4partner_port_dict = device_type4partner_port_instance.to_dict()
# create an instance of DeviceType4partnerPort from a dict
device_type4partner_port_from_dict = DeviceType4partnerPort.from_dict(device_type4partner_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


