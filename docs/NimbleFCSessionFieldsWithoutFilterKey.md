# NimbleFCSessionFieldsWithoutFilterKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the Fibre Channel session. A 42 digit hexadecimal number. | [optional] 

## Example

```python
from dscc.models.nimble_fc_session_fields_without_filter_key import NimbleFCSessionFieldsWithoutFilterKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFCSessionFieldsWithoutFilterKey from a JSON string
nimble_fc_session_fields_without_filter_key_instance = NimbleFCSessionFieldsWithoutFilterKey.from_json(json)
# print the JSON string representation of the object
print(NimbleFCSessionFieldsWithoutFilterKey.to_json())

# convert the object into a dict
nimble_fc_session_fields_without_filter_key_dict = nimble_fc_session_fields_without_filter_key_instance.to_dict()
# create an instance of NimbleFCSessionFieldsWithoutFilterKey from a dict
nimble_fc_session_fields_without_filter_key_from_dict = NimbleFCSessionFieldsWithoutFilterKey.from_dict(nimble_fc_session_fields_without_filter_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


