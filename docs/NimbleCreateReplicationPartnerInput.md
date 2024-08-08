# NimbleCreateReplicationPartnerInput

Create Replication Partner input on {Device-Type2}.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partners** | [**List[ReplicationPartnerObj]**](ReplicationPartnerObj.md) | List of replication partners. | 

## Example

```python
from dscc.models.nimble_create_replication_partner_input import NimbleCreateReplicationPartnerInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleCreateReplicationPartnerInput from a JSON string
nimble_create_replication_partner_input_instance = NimbleCreateReplicationPartnerInput.from_json(json)
# print the JSON string representation of the object
print(NimbleCreateReplicationPartnerInput.to_json())

# convert the object into a dict
nimble_create_replication_partner_input_dict = nimble_create_replication_partner_input_instance.to_dict()
# create an instance of NimbleCreateReplicationPartnerInput from a dict
nimble_create_replication_partner_input_from_dict = NimbleCreateReplicationPartnerInput.from_dict(nimble_create_replication_partner_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


