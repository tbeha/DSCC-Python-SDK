# NimbleControllerConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bus_location** | **str** | Bus location for the fibre channel config.String of up to 64 alphanumeric characters | [optional] 
**name** | **str** | Name of the fibre channel config. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**online** | **bool** | Online state of fibre channel config. | [optional] 
**port** | **int** | Port number for this fibre channel config.Unsigned 64-bit integer. | [optional] 
**slot** | **int** | Slot number for this fibre channel config. Unsigned 64-bit integer. | [optional] 
**wwnn** | **str** | WWNN (World Wide Node Name) of the Fibre Channel port. | [optional] 
**wwpn** | **str** | WWPN (World Wide Port Name) of the Fibre Channel target port. | [optional] 

## Example

```python
from dscc.models.nimble_controller_config import NimbleControllerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleControllerConfig from a JSON string
nimble_controller_config_instance = NimbleControllerConfig.from_json(json)
# print the JSON string representation of the object
print(NimbleControllerConfig.to_json())

# convert the object into a dict
nimble_controller_config_dict = nimble_controller_config_instance.to_dict()
# create an instance of NimbleControllerConfig from a dict
nimble_controller_config_from_dict = NimbleControllerConfig.from_dict(nimble_controller_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


