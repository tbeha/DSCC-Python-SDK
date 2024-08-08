# Partner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_wwn_or_name** | **str** | Node WWN (for FC) or iSCSI name (for iSCSI)  &#x60;Filter, Sort&#x60; | [optional] 
**port_wwn_or_ip** | **str** | Port WWN (for FC) or IP address (for iSCSI)  &#x60;Filter, Sort&#x60; | [optional] 
**position** | [**PartnerPortPosition**](PartnerPortPosition.md) |  | [optional] 

## Example

```python
from dscc.models.partner import Partner

# TODO update the JSON string below
json = "{}"
# create an instance of Partner from a JSON string
partner_instance = Partner.from_json(json)
# print the JSON string representation of the object
print(Partner.to_json())

# convert the object into a dict
partner_dict = partner_instance.to_dict()
# create an instance of Partner from a dict
partner_from_dict = Partner.from_dict(partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


