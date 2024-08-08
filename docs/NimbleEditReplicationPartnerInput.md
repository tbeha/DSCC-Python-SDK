# NimbleEditReplicationPartnerInput

Edit Replication Partner input on {Device-Type2}.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partners** | [**List[EditReplicationPartner]**](EditReplicationPartner.md) | List of replication partners. | 

## Example

```python
from dscc.models.nimble_edit_replication_partner_input import NimbleEditReplicationPartnerInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleEditReplicationPartnerInput from a JSON string
nimble_edit_replication_partner_input_instance = NimbleEditReplicationPartnerInput.from_json(json)
# print the JSON string representation of the object
print(NimbleEditReplicationPartnerInput.to_json())

# convert the object into a dict
nimble_edit_replication_partner_input_dict = nimble_edit_replication_partner_input_instance.to_dict()
# create an instance of NimbleEditReplicationPartnerInput from a dict
nimble_edit_replication_partner_input_from_dict = NimbleEditReplicationPartnerInput.from_dict(nimble_edit_replication_partner_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


