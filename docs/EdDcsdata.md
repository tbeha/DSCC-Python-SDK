# EdDcsdata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esi** | **bool** |  | [optional] 
**esi_status** | **str** |  | [optional] 

## Example

```python
from dscc.models.ed_dcsdata import EdDcsdata

# TODO update the JSON string below
json = "{}"
# create an instance of EdDcsdata from a JSON string
ed_dcsdata_instance = EdDcsdata.from_json(json)
# print the JSON string representation of the object
print(EdDcsdata.to_json())

# convert the object into a dict
ed_dcsdata_dict = ed_dcsdata_instance.to_dict()
# create an instance of EdDcsdata from a dict
ed_dcsdata_from_dict = EdDcsdata.from_dict(ed_dcsdata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


