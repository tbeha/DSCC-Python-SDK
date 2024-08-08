# VolumeSetPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_members** | **List[Optional[str]]** | Members to add to application set | [optional] 
**app_set_business_unit** | **str** | App set business unit | [optional] 
**app_set_comments** | **str** | App set comments | [optional] 
**app_set_importance** | [**VolumeSetImportance**](VolumeSetImportance.md) |  | [optional] 
**app_set_name** | **str** | App set name | [optional] 
**app_set_type** | [**VolumeSetApplicationType**](VolumeSetApplicationType.md) |  | [optional] 
**custom_app_type** | **str** | App set name for Custom workloads when appSetType&#x3D;CUSTOM | [optional] 
**edit_app_set_qos_config_input** | [**EditAppSetQosConfigInput**](EditAppSetQosConfigInput.md) |  | [optional] 
**remove_members** | **List[Optional[str]]** | Members to remove from application set | [optional] 

## Example

```python
from dscc.models.volume_set_put import VolumeSetPut

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeSetPut from a JSON string
volume_set_put_instance = VolumeSetPut.from_json(json)
# print the JSON string representation of the object
print(VolumeSetPut.to_json())

# convert the object into a dict
volume_set_put_dict = volume_set_put_instance.to_dict()
# create an instance of VolumeSetPut from a dict
volume_set_put_from_dict = VolumeSetPut.from_dict(volume_set_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


