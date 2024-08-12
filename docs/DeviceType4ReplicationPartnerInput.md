# DeviceType4ReplicationPartnerInput

Source and Target replication partner input details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partner_system_id** | **str** | SystemId of target array | 
**source** | [**DeviceType4CreateRemoteCopyTargetInput**](DeviceType4CreateRemoteCopyTargetInput.md) |  | 
**target** | [**DeviceType4CreateRemoteCopyTargetInput**](DeviceType4CreateRemoteCopyTargetInput.md) |  | 

## Example

```python
from dscc.models.device_type4_replication_partner_input import DeviceType4ReplicationPartnerInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ReplicationPartnerInput from a JSON string
device_type4_replication_partner_input_instance = DeviceType4ReplicationPartnerInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ReplicationPartnerInput.to_json())

# convert the object into a dict
device_type4_replication_partner_input_dict = device_type4_replication_partner_input_instance.to_dict()
# create an instance of DeviceType4ReplicationPartnerInput from a dict
device_type4_replication_partner_input_from_dict = DeviceType4ReplicationPartnerInput.from_dict(device_type4_replication_partner_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


