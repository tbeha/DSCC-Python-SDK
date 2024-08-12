# PartnerPortPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** | Port position node number | [optional] 
**port** | **int** | Port position port number | [optional] 
**slot** | **int** | Port position slot number | [optional] 

## Example

```python
from dscc.models.partner_port_position import PartnerPortPosition

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerPortPosition from a JSON string
partner_port_position_instance = PartnerPortPosition.from_json(json)
# print the JSON string representation of the object
print(PartnerPortPosition.to_json())

# convert the object into a dict
partner_port_position_dict = partner_port_position_instance.to_dict()
# create an instance of PartnerPortPosition from a dict
partner_port_position_from_dict = PartnerPortPosition.from_dict(partner_port_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


