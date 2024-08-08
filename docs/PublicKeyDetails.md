# PublicKeyDetails

Public key of the array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key. | [optional] 
**key_name** | **str** | The user that owns the key. | [optional] 
**key_type** | **str** | The key type. | [optional] 

## Example

```python
from dscc.models.public_key_details import PublicKeyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PublicKeyDetails from a JSON string
public_key_details_instance = PublicKeyDetails.from_json(json)
# print the JSON string representation of the object
print(PublicKeyDetails.to_json())

# convert the object into a dict
public_key_details_dict = public_key_details_instance.to_dict()
# create an instance of PublicKeyDetails from a dict
public_key_details_from_dict = PublicKeyDetails.from_dict(public_key_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


