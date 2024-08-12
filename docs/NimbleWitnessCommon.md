# NimbleWitnessCommon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**auto_switchover_messages** | [**List[NimbleErrorWithArguments]**](NimbleErrorWithArguments.md) | List of validation messages for automatic switchover of Group Management. This will be empty when there are no conflicts found. List of error codes with details. | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.nimble_witness_common import NimbleWitnessCommon

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleWitnessCommon from a JSON string
nimble_witness_common_instance = NimbleWitnessCommon.from_json(json)
# print the JSON string representation of the object
print(NimbleWitnessCommon.to_json())

# convert the object into a dict
nimble_witness_common_dict = nimble_witness_common_instance.to_dict()
# create an instance of NimbleWitnessCommon from a dict
nimble_witness_common_from_dict = NimbleWitnessCommon.from_dict(nimble_witness_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


