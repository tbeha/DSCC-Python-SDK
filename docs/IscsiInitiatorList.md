# IscsiInitiatorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for the ISCSI Initiator. A 42 digit hexadecimal number. | [optional] 
**ip_address** | **str** | IP address of the iSCSI initiator. Each initiator IP address must have an associated name specified using &#39;name&#39; attribute.You can choose not to enter the name for an initiator if you prefer not to authenticate using both name and IP address, in this case the IQN name will be returned as &#39;*&#39;. Alphanumeric, hyphenated, colon or period separated string of up to 255 characters or &#39;*&#39; | [optional] 
**iqn** | **str** | IQN name of the iSCSI initiator. Each initiator IQN name must have an associated IP address specified using the &#39;ip_address&#39; attribute.You can choose not to enter the IP address for an initiator if you prefer not to authenticate using both name and IP address,in this case the IP address will be returned as &#39;*&#39;. | [optional] 
**label** | **str** | Unique Identifier of the iSCSI initiator. Label is required when creating iSCSI initiator. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.iscsi_initiator_list import IscsiInitiatorList

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiInitiatorList from a JSON string
iscsi_initiator_list_instance = IscsiInitiatorList.from_json(json)
# print the JSON string representation of the object
print(IscsiInitiatorList.to_json())

# convert the object into a dict
iscsi_initiator_list_dict = iscsi_initiator_list_instance.to_dict()
# create an instance of IscsiInitiatorList from a dict
iscsi_initiator_list_from_dict = IscsiInitiatorList.from_dict(iscsi_initiator_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


