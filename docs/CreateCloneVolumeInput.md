# CreateCloneVolumeInput

Request body for creating physical copy of a volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_volume** | **str** | Name of the destination volume. | 
**offline_clone** | [**OfflineClone**](OfflineClone.md) |  | [optional] 
**online** | **bool** | Create an online or offline clone of a volume. | [optional] 
**online_clone** | [**OnlineClone**](OnlineClone.md) |  | [optional] 
**priority** | **str** | Priority of the task for clone volume. Defualts to MEDIUM. | [optional] 

## Example

```python
from dscc.models.create_clone_volume_input import CreateCloneVolumeInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCloneVolumeInput from a JSON string
create_clone_volume_input_instance = CreateCloneVolumeInput.from_json(json)
# print the JSON string representation of the object
print(CreateCloneVolumeInput.to_json())

# convert the object into a dict
create_clone_volume_input_dict = create_clone_volume_input_instance.to_dict()
# create an instance of CreateCloneVolumeInput from a dict
create_clone_volume_input_from_dict = CreateCloneVolumeInput.from_dict(create_clone_volume_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


