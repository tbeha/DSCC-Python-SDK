# PauseResumeNimbleReplicationPartnerPairInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partners** | [**List[ReplicationPartnerPairAction]**](ReplicationPartnerPairAction.md) | List of replication partner pairs. | 

## Example

```python
from dscc.models.pause_resume_nimble_replication_partner_pair_input import PauseResumeNimbleReplicationPartnerPairInput

# TODO update the JSON string below
json = "{}"
# create an instance of PauseResumeNimbleReplicationPartnerPairInput from a JSON string
pause_resume_nimble_replication_partner_pair_input_instance = PauseResumeNimbleReplicationPartnerPairInput.from_json(json)
# print the JSON string representation of the object
print(PauseResumeNimbleReplicationPartnerPairInput.to_json())

# convert the object into a dict
pause_resume_nimble_replication_partner_pair_input_dict = pause_resume_nimble_replication_partner_pair_input_instance.to_dict()
# create an instance of PauseResumeNimbleReplicationPartnerPairInput from a dict
pause_resume_nimble_replication_partner_pair_input_from_dict = PauseResumeNimbleReplicationPartnerPairInput.from_dict(pause_resume_nimble_replication_partner_pair_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


