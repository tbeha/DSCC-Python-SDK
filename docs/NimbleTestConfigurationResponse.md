# NimbleTestConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partner_id** | **str** | Replication Id of the parnter. | [optional] 
**response** | **str** | Task Response. | [optional] 
**status** | **str** | Task Status Status of the task. | [optional] 

## Example

```python
from dscc.models.nimble_test_configuration_response import NimbleTestConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleTestConfigurationResponse from a JSON string
nimble_test_configuration_response_instance = NimbleTestConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(NimbleTestConfigurationResponse.to_json())

# convert the object into a dict
nimble_test_configuration_response_dict = nimble_test_configuration_response_instance.to_dict()
# create an instance of NimbleTestConfigurationResponse from a dict
nimble_test_configuration_response_from_dict = NimbleTestConfigurationResponse.from_dict(nimble_test_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


