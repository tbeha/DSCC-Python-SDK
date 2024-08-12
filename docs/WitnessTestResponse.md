# WitnessTestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_name** | **str** | Name of an array. | [optional] 
**role** | **str** | Role of an array in the group. Possible values: &#39;leader&#39;, &#39;non_member&#39;, &#39;invalid&#39;, &#39;backup_leader&#39;, &#39;member&#39;, &#39;failed&#39;. | [optional] 
**witness_connectivity_message** | **str** | Reachability message of the witness. | [optional] 
**witness_connectivity_state** | **str** | Reachability status of the witness. | [optional] 

## Example

```python
from dscc.models.witness_test_response import WitnessTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WitnessTestResponse from a JSON string
witness_test_response_instance = WitnessTestResponse.from_json(json)
# print the JSON string representation of the object
print(WitnessTestResponse.to_json())

# convert the object into a dict
witness_test_response_dict = witness_test_response_instance.to_dict()
# create an instance of WitnessTestResponse from a dict
witness_test_response_from_dict = WitnessTestResponse.from_dict(witness_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


