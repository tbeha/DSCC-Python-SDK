# DeviceType4systemSettingsDetailsEncryption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_saved** | **bool** | Encryption settings and/or key backed up | [optional] 
**dar_state** | **str** | DAR state | [optional] 
**enabled** | **bool** | Encryption enabled | [optional] 
**failed_disks** | **float** | Number of failed disks | [optional] 
**fips_compliant** | **str** | FIPS compliant | [optional] 
**key_location** | **str** | Location of encyption key Local or External key management | [optional] 
**kmpi_protocols** | **List[str]** | KMIP protocols set | [optional] 
**licensed** | **bool** | Encryption licensed | [optional] 
**not_fipspd** | **float** | Number of non FIPS compliant physical disks | [optional] 
**not_node_sed** | **float** | Number of non SED node drives | [optional] 
**not_sedpd** | **float** | Number of non SED physical disks | [optional] 
**seq_num** | **float** | Sequence number | [optional] 
**server_count** | **float** | Count of External Key Management servers | [optional] 
**server_names** | **List[str]** | List of External Key Management servers | [optional] 
**server_port** | **float** | Connection port number for External Key Managers | [optional] 
**server_user** | **str** | Username on External Key Manager | [optional] 

## Example

```python
from dscc.models.device_type4system_settings_details_encryption import DeviceType4systemSettingsDetailsEncryption

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4systemSettingsDetailsEncryption from a JSON string
device_type4system_settings_details_encryption_instance = DeviceType4systemSettingsDetailsEncryption.from_json(json)
# print the JSON string representation of the object
print(DeviceType4systemSettingsDetailsEncryption.to_json())

# convert the object into a dict
device_type4system_settings_details_encryption_dict = device_type4system_settings_details_encryption_instance.to_dict()
# create an instance of DeviceType4systemSettingsDetailsEncryption from a dict
device_type4system_settings_details_encryption_from_dict = DeviceType4systemSettingsDetailsEncryption.from_dict(device_type4system_settings_details_encryption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


