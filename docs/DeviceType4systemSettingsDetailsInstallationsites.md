# DeviceType4systemSettingsDetailsInstallationsites


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City of the installation site | [optional] 
**company** | **str** | Company name of the installation site | [optional] 
**country** | **str** | Country of the installation site | [optional] 
**hpe_passport_id** | **str** | HPE passport ID | [optional] 
**hpe_password** | **str** | Password of an HPE passport ID | [optional] 
**id** | **str** | Unique identifier of the installation site | [optional] 
**postal_code** | **str** | Postal code of the installation site | [optional] 
**set_system_location** | **bool** | Apply system location to the system descriptor property | [optional] 
**state** | **str** | State of the installation site | [optional] 
**street_address** | **str** | Street address of the installation site | [optional] 
**support_provider** | **str** | Support provider of the installation site | [optional] 
**system_id** | **str** | SystemId/serialNumber of the array. | [optional] 

## Example

```python
from dscc.models.device_type4system_settings_details_installationsites import DeviceType4systemSettingsDetailsInstallationsites

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4systemSettingsDetailsInstallationsites from a JSON string
device_type4system_settings_details_installationsites_instance = DeviceType4systemSettingsDetailsInstallationsites.from_json(json)
# print the JSON string representation of the object
print(DeviceType4systemSettingsDetailsInstallationsites.to_json())

# convert the object into a dict
device_type4system_settings_details_installationsites_dict = device_type4system_settings_details_installationsites_instance.to_dict()
# create an instance of DeviceType4systemSettingsDetailsInstallationsites from a dict
device_type4system_settings_details_installationsites_from_dict = DeviceType4systemSettingsDetailsInstallationsites.from_dict(device_type4system_settings_details_installationsites_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


