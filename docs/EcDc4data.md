# EcDc4data


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hpl_led** | [**LED**](LED.md) |  | [optional] 
**split_led** | [**LED**](LED.md) |  | [optional] 
**system_led** | [**LED**](LED.md) |  | [optional] 

## Example

```python
from dscc.models.ec_dc4data import EcDc4data

# TODO update the JSON string below
json = "{}"
# create an instance of EcDc4data from a JSON string
ec_dc4data_instance = EcDc4data.from_json(json)
# print the JSON string representation of the object
print(EcDc4data.to_json())

# convert the object into a dict
ec_dc4data_dict = ec_dc4data_instance.to_dict()
# create an instance of EcDc4data from a dict
ec_dc4data_from_dict = EcDc4data.from_dict(ec_dc4data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


