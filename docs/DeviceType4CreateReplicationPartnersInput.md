# DeviceType4CreateReplicationPartnersInput

Request body to create replication partners

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partners** | [**List[DeviceType4ReplicationPartnerInput]**](DeviceType4ReplicationPartnerInput.md) |  | 

## Example

```python
from dscc.models.device_type4_create_replication_partners_input import DeviceType4CreateReplicationPartnersInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CreateReplicationPartnersInput from a JSON string
device_type4_create_replication_partners_input_instance = DeviceType4CreateReplicationPartnersInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CreateReplicationPartnersInput.to_json())

# convert the object into a dict
device_type4_create_replication_partners_input_dict = device_type4_create_replication_partners_input_instance.to_dict()
# create an instance of DeviceType4CreateReplicationPartnersInput from a dict
device_type4_create_replication_partners_input_from_dict = DeviceType4CreateReplicationPartnersInput.from_dict(device_type4_create_replication_partners_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


