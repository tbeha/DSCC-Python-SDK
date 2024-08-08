# NimbleWitnessDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str** | Request URI for detailed witness objects | [optional] 
**host** | **str** | Hostname or ip addresses of witness. Comma separated strings of up to 63 characters of hostname and/or ip addresses. Total length cannot exceed 255 characters. | [optional] 
**id** | **str** | Identifier for the witness configuration. A 42 digit hexadecimal number. | [optional] 
**port** | **int** | Port of witness. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**username** | **str** | Username of witness. This has to be a non-root that can login to the witness host. String of up to 32 characters, beginning with a letter or number or period (.) or an underscore (_). It can include underscore (_), dash (-), period (.) and end with doller ($) sign. | [optional] 
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
from dscc.models.nimble_witness_details import NimbleWitnessDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleWitnessDetails from a JSON string
nimble_witness_details_instance = NimbleWitnessDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleWitnessDetails.to_json())

# convert the object into a dict
nimble_witness_details_dict = nimble_witness_details_instance.to_dict()
# create an instance of NimbleWitnessDetails from a dict
nimble_witness_details_from_dict = NimbleWitnessDetails.from_dict(nimble_witness_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


