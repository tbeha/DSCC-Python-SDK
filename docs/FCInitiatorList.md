# FCInitiatorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Alias of the Fibre Channel initiator. Maximum alias length is 32 characters. Each initiator alias must have an associated WWPN specified using the &#39;wwpn&#39; attribute.You can choose not to enter the WWPN for an initiator when using previously saved initiator alias.String of up to 32 alphanumeric characters, or one of $^-_.: cannot begin with non-alphanumeric character. | [optional] 
**id** | **str** | Identifier for the FC Initiator. A 42 digit hexadecimal number. | [optional] 
**wwpn** | **str** | WWPN (World Wide Port Name) of the Fibre Channel initiator. WWPN is required when creating a Fibre Channel initiator. Each initiator WWPN can have an associated alias specified using the &#39;alias&#39; attribute. You can choose not to enter the alias for an initiator if you prefer not to assign an initiator alias. Eight bytes expressed in hex separated by colons. | [optional] 

## Example

```python
from dscc.models.fc_initiator_list import FCInitiatorList

# TODO update the JSON string below
json = "{}"
# create an instance of FCInitiatorList from a JSON string
fc_initiator_list_instance = FCInitiatorList.from_json(json)
# print the JSON string representation of the object
print(FCInitiatorList.to_json())

# convert the object into a dict
fc_initiator_list_dict = fc_initiator_list_instance.to_dict()
# create an instance of FCInitiatorList from a dict
fc_initiator_list_from_dict = FCInitiatorList.from_dict(fc_initiator_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


