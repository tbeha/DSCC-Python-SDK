# DeviceType4SetEKMBackupConfigParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ekmpassword** | **str** | Password for External Key Manager. | [optional] 
**ekmuser** | **str** | Username on External Key Manager. | [optional] 
**kmipprotocols** | **List[str]** | KMIP protocol. | [optional] 
**password** | **str** | Password for the encryption SetEKMBackup operation. | [optional] 
**port** | **str** | Connection port number for External Key Managers. | [optional] 
**serverlist** | **List[str]** | List of External Key Management servers. | [optional] 

## Example

```python
from dscc.models.device_type4_set_ekm_backup_config_params import DeviceType4SetEKMBackupConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SetEKMBackupConfigParams from a JSON string
device_type4_set_ekm_backup_config_params_instance = DeviceType4SetEKMBackupConfigParams.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SetEKMBackupConfigParams.to_json())

# convert the object into a dict
device_type4_set_ekm_backup_config_params_dict = device_type4_set_ekm_backup_config_params_instance.to_dict()
# create an instance of DeviceType4SetEKMBackupConfigParams from a dict
device_type4_set_ekm_backup_config_params_from_dict = DeviceType4SetEKMBackupConfigParams.from_dict(device_type4_set_ekm_backup_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


