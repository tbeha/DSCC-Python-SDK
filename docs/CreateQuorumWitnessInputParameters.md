# CreateQuorumWitnessInputParameters

Parameters for create quorum witness action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | Specifies the IP address of the Quorum Witness (QW) application to which the connectivity is created | 
**port** | **int** | Specifies port number to be used to communicate with SSL to the Quorum Witness application.Default value is 8843 | [optional] 
**ssl** | **bool** | Specifies the SSL connectivity to the Quorum Witness to be created | [optional] 

## Example

```python
from dscc.models.create_quorum_witness_input_parameters import CreateQuorumWitnessInputParameters

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuorumWitnessInputParameters from a JSON string
create_quorum_witness_input_parameters_instance = CreateQuorumWitnessInputParameters.from_json(json)
# print the JSON string representation of the object
print(CreateQuorumWitnessInputParameters.to_json())

# convert the object into a dict
create_quorum_witness_input_parameters_dict = create_quorum_witness_input_parameters_instance.to_dict()
# create an instance of CreateQuorumWitnessInputParameters from a dict
create_quorum_witness_input_parameters_from_dict = CreateQuorumWitnessInputParameters.from_dict(create_quorum_witness_input_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


