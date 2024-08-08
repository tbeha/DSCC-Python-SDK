# ExpirationDate

expiray Date of the battery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | time in millisecond | [optional] 
**tz** | **str** | timezone | [optional] 

## Example

```python
from dscc.models.expiration_date import ExpirationDate

# TODO update the JSON string below
json = "{}"
# create an instance of ExpirationDate from a JSON string
expiration_date_instance = ExpirationDate.from_json(json)
# print the JSON string representation of the object
print(ExpirationDate.to_json())

# convert the object into a dict
expiration_date_dict = expiration_date_instance.to_dict()
# create an instance of ExpirationDate from a dict
expiration_date_from_dict = ExpirationDate.from_dict(expiration_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


