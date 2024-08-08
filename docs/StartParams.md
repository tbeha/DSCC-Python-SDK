# StartParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_initial_sync** | **bool** | Specifies that volumes will skip the initial synchronization and set the volumes to a synchronized state once the stopped replicated volume set is started. The default setting is false. | [optional] 
**target_name** | **str** | Target name on which the protection has to be started. | [optional] 

## Example

```python
from dscc.models.start_params import StartParams

# TODO update the JSON string below
json = "{}"
# create an instance of StartParams from a JSON string
start_params_instance = StartParams.from_json(json)
# print the JSON string representation of the object
print(StartParams.to_json())

# convert the object into a dict
start_params_dict = start_params_instance.to_dict()
# create an instance of StartParams from a dict
start_params_from_dict = StartParams.from_dict(start_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


