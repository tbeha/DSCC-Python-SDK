# NimbleCreateWitnessInput

Create a new witness configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname or ip addresses of witness. Comma separated strings of up to 63 characters of hostname and/or ip addresses. Total length cannot exceed 255 characters. | 
**password** | **str** | Password of witness. String of 0 to 255 characters. | 
**port** | **int** | Port of witness. Positive integer value up to 65535 representing TCP/IP port. Defaults to 5395. | [optional] 
**username** | **str** | Username of witness. This has to be a non-root that can login to the witness host. String of up to 32 characters, beginning with a letter or number or period (.) or an underscore (_). It can include underscore (_), dash (-), period (.) and end with doller ($) sign. | 

## Example

```python
from dscc.models.nimble_create_witness_input import NimbleCreateWitnessInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleCreateWitnessInput from a JSON string
nimble_create_witness_input_instance = NimbleCreateWitnessInput.from_json(json)
# print the JSON string representation of the object
print(NimbleCreateWitnessInput.to_json())

# convert the object into a dict
nimble_create_witness_input_dict = nimble_create_witness_input_instance.to_dict()
# create an instance of NimbleCreateWitnessInput from a dict
nimble_create_witness_input_from_dict = NimbleCreateWitnessInput.from_dict(nimble_create_witness_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


