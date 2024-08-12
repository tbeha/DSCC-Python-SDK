# AppKeyValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Identifier of key-value pair. | [optional] 
**value** | **str** | Value of key-value pair. | [optional] 

## Example

```python
from dscc.models.app_key_value import AppKeyValue

# TODO update the JSON string below
json = "{}"
# create an instance of AppKeyValue from a JSON string
app_key_value_instance = AppKeyValue.from_json(json)
# print the JSON string representation of the object
print(AppKeyValue.to_json())

# convert the object into a dict
app_key_value_dict = app_key_value_instance.to_dict()
# create an instance of AppKeyValue from a dict
app_key_value_from_dict = AppKeyValue.from_dict(app_key_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


