# HostChapObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator_chap_enabled** | **bool** | Initiator CHAP enabled or disabled | [optional] 
**initiator_chap_name** | **str** | Name of initiator CHAP set on iSCSI host | [optional] 
**initiator_encrypted_chap_secret** | **str** | Encrypted Initiator CHAP secret set on iSCSI host | [optional] 
**system** | **str** | Host CHAP details for a given system | [optional] 
**target_chap_enabled** | **bool** | Target CHAP enabled or disabled | [optional] 
**target_chap_name** | **str** | Name of target CHAP set on iSCSI host | [optional] 
**target_encrypted_chap_secret** | **str** | Encrypted Target CHAP secret set on iSCSI host | [optional] 

## Example

```python
from dscc.models.host_chap_object import HostChapObject

# TODO update the JSON string below
json = "{}"
# create an instance of HostChapObject from a JSON string
host_chap_object_instance = HostChapObject.from_json(json)
# print the JSON string representation of the object
print(HostChapObject.to_json())

# convert the object into a dict
host_chap_object_dict = host_chap_object_instance.to_dict()
# create an instance of HostChapObject from a dict
host_chap_object_from_dict = HostChapObject.from_dict(host_chap_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


