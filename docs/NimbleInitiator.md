# NimbleInitiator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_protocol** | **str** | Access protocol used by the initiator. Possible values: &#39;iscsi&#39;, &#39;fc&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**alias** | **str** | Alias of the Fibre Channel initiator. Maximum alias length is 32 characters. Each initiator alias must have an associated WWPN specified using the &#39;wwpn&#39; attribute.You can choose not to enter the WWPN for an initiator when using previously saved initiator alias.String of up to 32 alphanumeric characters, or one of $^-_.: cannot begin with non-alphanumeric character.&#x60;Filter, Sort&#x60; | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**chapuser_id** | **str** | Identifier for the CHAP user.&#x60;Filter, Sort&#x60; | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**creation_time** | **int** | Time when this initiator group was created. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Identifier for initiator. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**initiator_group_id** | **str** | Identifier of the initiator group that this initiator is assigned to. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**initiator_group_name** | **str** | Name of the initiator group that this initiator is assigned to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character &#x60;Filter, Sort&#x60; | [optional] 
**ip_address** | **str** | IP address of the iSCSI initiator. Each initiator IP address must have an associated name specified using &#39;name&#39; attribute.You can choose not to enter the name for an initiator if you prefer not to authenticate using both name and IP address, in this case the IQN name will be returned as &#39;*&#39;. Alphanumeric, hyphenated, colon or period separated string of up to 255 characters or &#39;*&#39; &#x60;Filter, Sort&#x60; | [optional] 
**iqn** | **str** | IQN name of the iSCSI initiator. Each initiator IQN name must have an associated IP address specified using the &#39;ip_address&#39; attribute.You can choose not to enter the IP address for an initiator if you prefer not to authenticate using both name and IP address,in this case the IP address will be returned as &#39;*&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**label** | **str** | Unique Identifier of the iSCSI initiator. Label is required when creating iSCSI initiator. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. &#x60;Filter, Sort&#x60; | [optional] 
**last_modified** | **int** | Time when this initiator group was last modified.Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**override_existing_alias** | **bool** | Forcibly add Fibre Channel initiator to initiator group by updating or removing conflicting Fibre Channel initiator aliases. (this argument is deprecated) | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**sc_host_initiator_id** | **str** | Host Service Initiator Id (this argument is deprecated) | [optional] 
**type** | **str** | type | [optional] 
**wwpn** | **str** | WWPN (World Wide Port Name) of the Fibre Channel initiator. WWPN is required when creating a Fibre Channel initiator. Each initiator WWPN can have an associated alias specified using the &#39;alias&#39; attribute. You can choose not to enter the alias for an initiator if you prefer not to assign an initiator alias. Eight bytes expressed in hex separated by colons.&#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.nimble_initiator import NimbleInitiator

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleInitiator from a JSON string
nimble_initiator_instance = NimbleInitiator.from_json(json)
# print the JSON string representation of the object
print(NimbleInitiator.to_json())

# convert the object into a dict
nimble_initiator_dict = nimble_initiator_instance.to_dict()
# create an instance of NimbleInitiator from a dict
nimble_initiator_from_dict = NimbleInitiator.from_dict(nimble_initiator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


