# DeviceType4EncryptionBackupRekeyRestoreParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password for the encryption Backup/Rekey/Restore operation. | [optional] 

## Example

```python
from dscc.models.device_type4_encryption_backup_rekey_restore_params import DeviceType4EncryptionBackupRekeyRestoreParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EncryptionBackupRekeyRestoreParams from a JSON string
device_type4_encryption_backup_rekey_restore_params_instance = DeviceType4EncryptionBackupRekeyRestoreParams.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EncryptionBackupRekeyRestoreParams.to_json())

# convert the object into a dict
device_type4_encryption_backup_rekey_restore_params_dict = device_type4_encryption_backup_rekey_restore_params_instance.to_dict()
# create an instance of DeviceType4EncryptionBackupRekeyRestoreParams from a dict
device_type4_encryption_backup_rekey_restore_params_from_dict = DeviceType4EncryptionBackupRekeyRestoreParams.from_dict(device_type4_encryption_backup_rekey_restore_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


