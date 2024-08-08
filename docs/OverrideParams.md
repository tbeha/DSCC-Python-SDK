# OverrideParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_name** | **str** | Replication partner name (target name) on which the override action is to be performed. | [optional] 

## Example

```python
from dscc.models.override_params import OverrideParams

# TODO update the JSON string below
json = "{}"
# create an instance of OverrideParams from a JSON string
override_params_instance = OverrideParams.from_json(json)
# print the JSON string representation of the object
print(OverrideParams.to_json())

# convert the object into a dict
override_params_dict = override_params_instance.to_dict()
# create an instance of OverrideParams from a dict
override_params_from_dict = OverrideParams.from_dict(override_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


