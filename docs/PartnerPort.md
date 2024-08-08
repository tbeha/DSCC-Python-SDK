# PartnerPort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_wwn_or_name** | **str** | Node WWN (for FC) or iSCSI name (for iSCSI) | [optional] 
**port_wwn_or_ip** | **str** | Port WWN (for FC) or IP address (for iSCSI) | [optional] 
**position** | [**PartnerPortPosition**](PartnerPortPosition.md) |  | [optional] 

## Example

```python
from dscc.models.partner_port import PartnerPort

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerPort from a JSON string
partner_port_instance = PartnerPort.from_json(json)
# print the JSON string representation of the object
print(PartnerPort.to_json())

# convert the object into a dict
partner_port_dict = partner_port_instance.to_dict()
# create an instance of PartnerPort from a dict
partner_port_from_dict = PartnerPort.from_dict(partner_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


