# EdDc4data


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esi** | **bool** |  | [optional] 
**esi_status** | **str** |  | [optional] 
**system_led** | [**LED**](LED.md) |  | [optional] 

## Example

```python
from dscc.models.ed_dc4data import EdDc4data

# TODO update the JSON string below
json = "{}"
# create an instance of EdDc4data from a JSON string
ed_dc4data_instance = EdDc4data.from_json(json)
# print the JSON string representation of the object
print(EdDc4data.to_json())

# convert the object into a dict
ed_dc4data_dict = ed_dc4data_instance.to_dict()
# create an instance of EdDc4data from a dict
ed_dc4data_from_dict = EdDc4data.from_dict(ed_dc4data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


