# DeviceType4CreateAppSetInput

Request body for creating Application Sets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_set_business_unit** | **str** | App set business unit | [optional] 
**app_set_comments** | **str** | App set comments | [optional] 
**app_set_importance** | [**DeviceType4VsAppSetImportance**](DeviceType4VsAppSetImportance.md) |  | [optional] 
**app_set_name** | **str** | App set name | 
**app_set_type** | [**DeviceType4VolumeSetApplicationType**](DeviceType4VolumeSetApplicationType.md) |  | 
**create_app_set_qos_config_input** | [**DeviceType4CreateAppSetQosConfigInput**](DeviceType4CreateAppSetQosConfigInput.md) |  | [optional] 
**custom_app_type** | **str** | App set name for Custom workloads when appSetType&#x3D;CUSTOM | [optional] 
**members** | **List[Optional[str]]** | volumes list | [optional] 

## Example

```python
from dscc.models.device_type4_create_app_set_input import DeviceType4CreateAppSetInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CreateAppSetInput from a JSON string
device_type4_create_app_set_input_instance = DeviceType4CreateAppSetInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CreateAppSetInput.to_json())

# convert the object into a dict
device_type4_create_app_set_input_dict = device_type4_create_app_set_input_instance.to_dict()
# create an instance of DeviceType4CreateAppSetInput from a dict
device_type4_create_app_set_input_from_dict = DeviceType4CreateAppSetInput.from_dict(device_type4_create_app_set_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


