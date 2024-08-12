# CreateQuorumWitnessInput

Request body to configure quorum witness

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**CreateQuorumWitnessInputParameters**](CreateQuorumWitnessInputParameters.md) |  | 
**replication_partner_system_id** | **str** | SystemId of target replication partner | 
**src_replication_id** | **str** | Id of source replication partner on which quorum witness is to be configured | 
**start_quorum_witness** | **bool** | Specifies start/stop Quorum Witness connectivity on the storage system. If set true, ATF configuration is activated. If set false, ATF configuration is deactivated. | [optional] 
**target_replication_id** | **str** | Id of target replication partner on which quorum witness is to be configured | 

## Example

```python
from dscc.models.create_quorum_witness_input import CreateQuorumWitnessInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuorumWitnessInput from a JSON string
create_quorum_witness_input_instance = CreateQuorumWitnessInput.from_json(json)
# print the JSON string representation of the object
print(CreateQuorumWitnessInput.to_json())

# convert the object into a dict
create_quorum_witness_input_dict = create_quorum_witness_input_instance.to_dict()
# create an instance of CreateQuorumWitnessInput from a dict
create_quorum_witness_input_from_dict = CreateQuorumWitnessInput.from_dict(create_quorum_witness_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


