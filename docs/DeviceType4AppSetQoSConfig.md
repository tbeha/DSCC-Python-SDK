# DeviceType4AppSetQoSConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth_max_limit_ki_b** | **float** | Bandwidth Maximum Limit in KiB | [optional] 
**bw_guarantee_tb** | **float** | Bandwidth Guarantee Limit per Tb in KiB | [optional] 
**bw_limit_tb** | **float** | Bandwidth Maximum Limit per Tb in KiB | [optional] 
**displayname** | **str** | QoS Config Display name | [optional] 
**domain** | **str** | Domain Name | [optional] 
**enable** | **bool** | Enable of QoS Configuration | [optional] 
**enable_sr_alert** | **bool** | Specifies if the SR alert is enabled or not for a QoS-configured vvset. The value for the enableSrAlert will be true only if the name of the SR alert criterion matches with the name of the vvset and the criterion&#39;s condition(s) of the SR alert matches with the QoS parameters set. | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **float** | id of the QoS Configuration | [optional] 
**io_guarantee_tb** | **float** | iops Maximum Guarantee per Tb | [optional] 
**io_limit_tb** | **float** | iops Maximum Limit per Tb | [optional] 
**iops_max_limit** | **float** | iops Maxmium Limit | [optional] 
**last_modified_epoch** | **float** | last modified Epoch | [optional] 
**per_tb** | **bool** | Enable of perTb QoS Configuration | [optional] 
**system_uid** | **str** | System Id | [optional] 
**system_wwn** | **str** | System WWN | [optional] 
**target_name** | **str** | Target Name of the QoS Config | [optional] 
**target_type** | **str** | Target Type of the QoS Config | [optional] 
**uid** | **str** | UID of the QoS Config resource | [optional] 
**volumes** | **List[str]** | List of volumes | [optional] 

## Example

```python
from dscc.models.device_type4_app_set_qo_s_config import DeviceType4AppSetQoSConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4AppSetQoSConfig from a JSON string
device_type4_app_set_qo_s_config_instance = DeviceType4AppSetQoSConfig.from_json(json)
# print the JSON string representation of the object
print(DeviceType4AppSetQoSConfig.to_json())

# convert the object into a dict
device_type4_app_set_qo_s_config_dict = device_type4_app_set_qo_s_config_instance.to_dict()
# create an instance of DeviceType4AppSetQoSConfig from a dict
device_type4_app_set_qo_s_config_from_dict = DeviceType4AppSetQoSConfig.from_dict(device_type4_app_set_qo_s_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


