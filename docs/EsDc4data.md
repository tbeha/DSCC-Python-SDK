# EsDc4data


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hpl_led** | [**LED**](LED.md) |  | [optional] 
**left** | **bool** |  | [optional] 
**right** | **bool** |  | [optional] 
**system_led** | [**LED**](LED.md) |  | [optional] 

## Example

```python
from dscc.models.es_dc4data import EsDc4data

# TODO update the JSON string below
json = "{}"
# create an instance of EsDc4data from a JSON string
es_dc4data_instance = EsDc4data.from_json(json)
# print the JSON string representation of the object
print(EsDc4data.to_json())

# convert the object into a dict
es_dc4data_dict = es_dc4data_instance.to_dict()
# create an instance of EsDc4data from a dict
es_dc4data_from_dict = EsDc4data.from_dict(es_dc4data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


