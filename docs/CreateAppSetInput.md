# CreateAppSetInput

Request body for creating Application Sets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_set_business_unit** | **str** | App set business unit | [optional] 
**app_set_comments** | **str** | App set comments | [optional] 
**app_set_importance** | [**VolumeSetImportance**](VolumeSetImportance.md) |  | [optional] 
**app_set_name** | **str** | App set name | 
**app_set_type** | [**VolumeSetApplicationType**](VolumeSetApplicationType.md) |  | 
**create_app_set_qos_config_input** | [**CreateAppSetQosConfigInput**](CreateAppSetQosConfigInput.md) |  | [optional] 
**custom_app_type** | **str** | App set name for Custom workloads when appSetType&#x3D;CUSTOM | [optional] 
**members** | **List[Optional[str]]** | volumes list | [optional] 

## Example

```python
from dscc.models.create_app_set_input import CreateAppSetInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAppSetInput from a JSON string
create_app_set_input_instance = CreateAppSetInput.from_json(json)
# print the JSON string representation of the object
print(CreateAppSetInput.to_json())

# convert the object into a dict
create_app_set_input_dict = create_app_set_input_instance.to_dict()
# create an instance of CreateAppSetInput from a dict
create_app_set_input_from_dict = CreateAppSetInput.from_dict(create_app_set_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


