# AppSetQoSConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth_max_limit_ki_b** | **float** | Bandwidth Maximum Limit in KiB | [optional] 
**displayname** | **str** | QoS Config Display name | [optional] 
**domain** | **str** | Domain Name | [optional] 
**enable** | **bool** | Enable of QoS Configuration | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **float** | id of the QoS Configuration | [optional] 
**iops_max_limit** | **float** | iops Maximum Limit | [optional] 
**last_modified_epoch** | **float** | last modified Epoch | [optional] 
**system_uid** | **str** | System Id | [optional] 
**system_wwn** | **str** | System WWN | [optional] 
**target_name** | **str** | Target Name of the QoS Config | [optional] 
**target_type** | **str** | Target Type of the QoS Config | [optional] 
**uid** | **str** | UID of the QoS Config resource | [optional] 
**volumes** | **List[str]** | List of volumes | [optional] 

## Example

```python
from dscc.models.app_set_qo_s_config import AppSetQoSConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppSetQoSConfig from a JSON string
app_set_qo_s_config_instance = AppSetQoSConfig.from_json(json)
# print the JSON string representation of the object
print(AppSetQoSConfig.to_json())

# convert the object into a dict
app_set_qo_s_config_dict = app_set_qo_s_config_instance.to_dict()
# create an instance of AppSetQoSConfig from a dict
app_set_qo_s_config_from_dict = AppSetQoSConfig.from_dict(app_set_qo_s_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


