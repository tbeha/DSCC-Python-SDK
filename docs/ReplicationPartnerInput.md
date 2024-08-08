# ReplicationPartnerInput

Source and Target replication partner input details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partner_system_id** | **str** | SystemId of target array | 
**source** | [**CreateRemoteCopyTargetInput**](CreateRemoteCopyTargetInput.md) |  | 
**target** | [**CreateRemoteCopyTargetInput**](CreateRemoteCopyTargetInput.md) |  | 

## Example

```python
from dscc.models.replication_partner_input import ReplicationPartnerInput

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationPartnerInput from a JSON string
replication_partner_input_instance = ReplicationPartnerInput.from_json(json)
# print the JSON string representation of the object
print(ReplicationPartnerInput.to_json())

# convert the object into a dict
replication_partner_input_dict = replication_partner_input_instance.to_dict()
# create an instance of ReplicationPartnerInput from a dict
replication_partner_input_from_dict = ReplicationPartnerInput.from_dict(replication_partner_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


