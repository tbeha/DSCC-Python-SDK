# FriendlyCert

Certificate detail in readable format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_from** | [**Validity**](Validity.md) |  | [optional] 
**valid_until** | [**Validity**](Validity.md) |  | [optional] 
**issued_to** | **str** | Name of the certificate issued to | [optional] 
**issuer** | **str** | Name of Certificate issued to | [optional] 

## Example

```python
from dscc.models.friendly_cert import FriendlyCert

# TODO update the JSON string below
json = "{}"
# create an instance of FriendlyCert from a JSON string
friendly_cert_instance = FriendlyCert.from_json(json)
# print the JSON string representation of the object
print(FriendlyCert.to_json())

# convert the object into a dict
friendly_cert_dict = friendly_cert_instance.to_dict()
# create an instance of FriendlyCert from a dict
friendly_cert_from_dict = FriendlyCert.from_dict(friendly_cert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


