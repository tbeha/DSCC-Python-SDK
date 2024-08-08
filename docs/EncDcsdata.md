# EncDcsdata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fw_status** | **str** |  | [optional] 
**fw_version** | **str** |  | [optional] 

## Example

```python
from dscc.models.enc_dcsdata import EncDcsdata

# TODO update the JSON string below
json = "{}"
# create an instance of EncDcsdata from a JSON string
enc_dcsdata_instance = EncDcsdata.from_json(json)
# print the JSON string representation of the object
print(EncDcsdata.to_json())

# convert the object into a dict
enc_dcsdata_dict = enc_dcsdata_instance.to_dict()
# create an instance of EncDcsdata from a dict
enc_dcsdata_from_dict = EncDcsdata.from_dict(enc_dcsdata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


