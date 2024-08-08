# DeviceType4RemoveReplicationPartnersInput

Request body for deleting replication partner pairs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partners** | [**List[DeviceType4RemoveRemoteCopyTargetInput]**](DeviceType4RemoveRemoteCopyTargetInput.md) | List of replication partner pairs to be deleted | 

## Example

```python
from dscc.models.device_type4_remove_replication_partners_input import DeviceType4RemoveReplicationPartnersInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RemoveReplicationPartnersInput from a JSON string
device_type4_remove_replication_partners_input_instance = DeviceType4RemoveReplicationPartnersInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RemoveReplicationPartnersInput.to_json())

# convert the object into a dict
device_type4_remove_replication_partners_input_dict = device_type4_remove_replication_partners_input_instance.to_dict()
# create an instance of DeviceType4RemoveReplicationPartnersInput from a dict
device_type4_remove_replication_partners_input_from_dict = DeviceType4RemoveReplicationPartnersInput.from_dict(device_type4_remove_replication_partners_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


