# EditQuorumWitnessInput

Request body to start/stop quorum witness

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partner_system_id** | **str** | SystemId of target replication partner | 
**start_quorum_witness** | **bool** | Specifies start/stop Quorum Witness connectivity on the storage system. If set true, ATF configuration is activated. If set false, ATF configuration is deactivated. | 
**target_replication_id** | **str** | Id of target replication partner on which quorum witness is configured | 

## Example

```python
from dscc.models.edit_quorum_witness_input import EditQuorumWitnessInput

# TODO update the JSON string below
json = "{}"
# create an instance of EditQuorumWitnessInput from a JSON string
edit_quorum_witness_input_instance = EditQuorumWitnessInput.from_json(json)
# print the JSON string representation of the object
print(EditQuorumWitnessInput.to_json())

# convert the object into a dict
edit_quorum_witness_input_dict = edit_quorum_witness_input_instance.to_dict()
# create an instance of EditQuorumWitnessInput from a dict
edit_quorum_witness_input_from_dict = EditQuorumWitnessInput.from_dict(edit_quorum_witness_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


