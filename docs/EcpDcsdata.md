# EcpDcsdata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sas_link_enabled** | **bool** |  | [optional] 
**sas_link_online** | **bool** |  | [optional] 

## Example

```python
from dscc.models.ecp_dcsdata import EcpDcsdata

# TODO update the JSON string below
json = "{}"
# create an instance of EcpDcsdata from a JSON string
ecp_dcsdata_instance = EcpDcsdata.from_json(json)
# print the JSON string representation of the object
print(EcpDcsdata.to_json())

# convert the object into a dict
ecp_dcsdata_dict = ecp_dcsdata_instance.to_dict()
# create an instance of EcpDcsdata from a dict
ecp_dcsdata_from_dict = EcpDcsdata.from_dict(ecp_dcsdata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


