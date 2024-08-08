# Validity

The validity of the certificates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch time in milliseconds | [optional] 
**tz** | **str** | Time zone name | [optional] 

## Example

```python
from dscc.models.validity import Validity

# TODO update the JSON string below
json = "{}"
# create an instance of Validity from a JSON string
validity_instance = Validity.from_json(json)
# print the JSON string representation of the object
print(Validity.to_json())

# convert the object into a dict
validity_dict = validity_instance.to_dict()
# create an instance of Validity from a dict
validity_from_dict = Validity.from_dict(validity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


