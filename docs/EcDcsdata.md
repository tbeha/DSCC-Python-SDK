# EcDcsdata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fw_status** | **str** |  | [optional] 
**fw_version** | **str** |  | [optional] 
**master** | **bool** |  | [optional] 
**sas_status** | **str** |  | [optional] 

## Example

```python
from dscc.models.ec_dcsdata import EcDcsdata

# TODO update the JSON string below
json = "{}"
# create an instance of EcDcsdata from a JSON string
ec_dcsdata_instance = EcDcsdata.from_json(json)
# print the JSON string representation of the object
print(EcDcsdata.to_json())

# convert the object into a dict
ec_dcsdata_dict = ec_dcsdata_instance.to_dict()
# create an instance of EcDcsdata from a dict
ec_dcsdata_from_dict = EcDcsdata.from_dict(ec_dcsdata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


