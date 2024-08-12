# DeviceType4systemSettingsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**auth_mode** | **str** | Password Authentication Mode | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object  | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**encryption** | [**DeviceType4systemSettingsDetailsEncryption**](DeviceType4systemSettingsDetailsEncryption.md) |  | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**installationsites** | [**DeviceType4systemSettingsDetailsInstallationsites**](DeviceType4systemSettingsDetailsInstallationsites.md) |  | [optional] 
**is_fips_enabled** | **bool** | Apply FIPS Standard | [optional] 
**name** | **str** | system name | [optional] 
**ntp_server** | **str** | ntp server | [optional] 
**remote_syslog_settings** | [**DeviceType4systemSettingsDetailsRemoteSyslogSettings**](DeviceType4systemSettingsDetailsRemoteSyslogSettings.md) |  | [optional] 
**srinfo** | [**DeviceType4systemSettingsDetailsSrinfo**](DeviceType4systemSettingsDetailsSrinfo.md) |  | [optional] 
**supportcontact** | [**DeviceType4ContactsDetails**](DeviceType4ContactsDetails.md) |  | [optional] 
**system_date** | **int** | system date time | [optional] 
**system_id** | **str** | SystemId/serialNumber of the array. | [optional] 
**system_parameters** | [**DeviceType4systemSettingsDetailsSystemParameters**](DeviceType4systemSettingsDetailsSystemParameters.md) |  | [optional] 
**timezone** | **str** | system time zone | [optional] 
**type** | **str** | The type of resource. | [optional] 

## Example

```python
from dscc.models.device_type4system_settings_details import DeviceType4systemSettingsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4systemSettingsDetails from a JSON string
device_type4system_settings_details_instance = DeviceType4systemSettingsDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4systemSettingsDetails.to_json())

# convert the object into a dict
device_type4system_settings_details_dict = device_type4system_settings_details_instance.to_dict()
# create an instance of DeviceType4systemSettingsDetails from a dict
device_type4system_settings_details_from_dict = DeviceType4systemSettingsDetails.from_dict(device_type4system_settings_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


