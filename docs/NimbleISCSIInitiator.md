# NimbleISCSIInitiator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the iSCSI initiator. | [optional] 
**ip_address** | **str** | IP address of the iSCSI initiator. | [optional] 
**iqn** | **str** | IQN name of the iSCSI initiator. | [optional] 
**label** | **str** | Unique label of the iSCSI initiator. | [optional] 

## Example

```python
from dscc.models.nimble_iscsi_initiator import NimbleISCSIInitiator

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleISCSIInitiator from a JSON string
nimble_iscsi_initiator_instance = NimbleISCSIInitiator.from_json(json)
# print the JSON string representation of the object
print(NimbleISCSIInitiator.to_json())

# convert the object into a dict
nimble_iscsi_initiator_dict = nimble_iscsi_initiator_instance.to_dict()
# create an instance of NimbleISCSIInitiator from a dict
nimble_iscsi_initiator_from_dict = NimbleISCSIInitiator.from_dict(nimble_iscsi_initiator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


