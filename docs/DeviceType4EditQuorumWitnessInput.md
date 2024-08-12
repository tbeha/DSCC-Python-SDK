# DeviceType4EditQuorumWitnessInput

Request body to start/stop quorum witness

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partner_system_id** | **str** | SystemId of target replication partner | 
**start_quorum_witness** | **bool** | Specifies start/stop Quorum Witness connectivity on the storage system. If set true, ATF configuration is activated. If set false, ATF configuration is deactivated. | 
**target_replication_id** | **str** | Id of target replication partner on which quorum witness is configured | 

## Example

```python
from dscc.models.device_type4_edit_quorum_witness_input import DeviceType4EditQuorumWitnessInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EditQuorumWitnessInput from a JSON string
device_type4_edit_quorum_witness_input_instance = DeviceType4EditQuorumWitnessInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EditQuorumWitnessInput.to_json())

# convert the object into a dict
device_type4_edit_quorum_witness_input_dict = device_type4_edit_quorum_witness_input_instance.to_dict()
# create an instance of DeviceType4EditQuorumWitnessInput from a dict
device_type4_edit_quorum_witness_input_from_dict = DeviceType4EditQuorumWitnessInput.from_dict(device_type4_edit_quorum_witness_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


