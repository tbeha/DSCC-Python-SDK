# HostChapInputObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator_chap_enabled** | **bool** | Initiator CHAP enabled or disabled | [optional] 
**initiator_chap_name** | **str** | Name of initiator CHAP | [optional] 
**initiator_encrypted_chap_secret** | **str** | Base64 encoded Initiator CHAP Secret | [optional] 
**system** | **str** | Host CHAP details for a given system | [optional] 
**target_chap_enabled** | **bool** | Target CHAP enabled or disabled | [optional] 
**target_chap_name** | **str** | Name of target CHAP | [optional] 
**target_encrypted_chap_secret** | **str** | Base64 encoded Target CHAP Secret | [optional] 

## Example

```python
from dscc.models.host_chap_input_object import HostChapInputObject

# TODO update the JSON string below
json = "{}"
# create an instance of HostChapInputObject from a JSON string
host_chap_input_object_instance = HostChapInputObject.from_json(json)
# print the JSON string representation of the object
print(HostChapInputObject.to_json())

# convert the object into a dict
host_chap_input_object_dict = host_chap_input_object_instance.to_dict()
# create an instance of HostChapInputObject from a dict
host_chap_input_object_from_dict = HostChapInputObject.from_dict(host_chap_input_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


