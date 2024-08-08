# CloneVolumesInput

The request body for clone volumes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clone_volume_name** | **str** | Name of a clone volume to be created. | 
**parent_volume_name** | **str** | Name of the parent volume for a given clone volume. | 

## Example

```python
from dscc.models.clone_volumes_input import CloneVolumesInput

# TODO update the JSON string below
json = "{}"
# create an instance of CloneVolumesInput from a JSON string
clone_volumes_input_instance = CloneVolumesInput.from_json(json)
# print the JSON string representation of the object
print(CloneVolumesInput.to_json())

# convert the object into a dict
clone_volumes_input_dict = clone_volumes_input_instance.to_dict()
# create an instance of CloneVolumesInput from a dict
clone_volumes_input_from_dict = CloneVolumesInput.from_dict(clone_volumes_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


