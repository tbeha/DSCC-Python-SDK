# RecoverParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_start** | **bool** | Specifies that protection is not started after recover action is completed. | [optional] 
**skip_sync** | **bool** | Specifies that protection is not synced after recover action is completed. | [optional] 
**target_name** | **str** | Replication partner name (target name) on which the recover action to be performed. | [optional] 

## Example

```python
from dscc.models.recover_params import RecoverParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverParams from a JSON string
recover_params_instance = RecoverParams.from_json(json)
# print the JSON string representation of the object
print(RecoverParams.to_json())

# convert the object into a dict
recover_params_dict = recover_params_instance.to_dict()
# create an instance of RecoverParams from a dict
recover_params_from_dict = RecoverParams.from_dict(recover_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


