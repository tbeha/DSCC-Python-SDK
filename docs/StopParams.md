# StopParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**no_snapshot** | **bool** | This option turns off creation of snapshots in synchronous and periodic modes, and deletes the current synchronization snapshots. | [optional] 
**target_name** | **str** | Target name on which the protection has to be stopped. | [optional] 

## Example

```python
from dscc.models.stop_params import StopParams

# TODO update the JSON string below
json = "{}"
# create an instance of StopParams from a JSON string
stop_params_instance = StopParams.from_json(json)
# print the JSON string representation of the object
print(StopParams.to_json())

# convert the object into a dict
stop_params_dict = stop_params_instance.to_dict()
# create an instance of StopParams from a dict
stop_params_from_dict = StopParams.from_dict(stop_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


