# DeviceType4RecoverParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_start** | **bool** | Specifies that protection is not started after recover action is completed. | [optional] 
**skip_sync** | **bool** | Specifies that protection is not synced after recover action is completed. | [optional] 
**target_name** | **str** | Replication partner name (target name) on which the recover action to be performed. | [optional] 

## Example

```python
from dscc.models.device_type4_recover_params import DeviceType4RecoverParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RecoverParams from a JSON string
device_type4_recover_params_instance = DeviceType4RecoverParams.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RecoverParams.to_json())

# convert the object into a dict
device_type4_recover_params_dict = device_type4_recover_params_instance.to_dict()
# create an instance of DeviceType4RecoverParams from a dict
device_type4_recover_params_from_dict = DeviceType4RecoverParams.from_dict(device_type4_recover_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


