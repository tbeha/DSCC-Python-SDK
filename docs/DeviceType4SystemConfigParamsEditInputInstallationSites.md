# DeviceType4SystemConfigParamsEditInputInstallationSites


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City of the installation site | [optional] 
**company** | **str** | Company name of the installation site | [optional] 
**country** | **str** | Country of the installation site | [optional] 
**postal_code** | **str** | Postal code of the installation site | [optional] 
**set_system_location** | **bool** | Apply system location to the system descriptor property | [optional] 
**state** | **str** | State of the installation site | [optional] 
**street_address** | **str** | Street address of the installation site | [optional] 
**support_provider** | **str** | Support provider of the installation site | [optional] 

## Example

```python
from dscc.models.device_type4_system_config_params_edit_input_installation_sites import DeviceType4SystemConfigParamsEditInputInstallationSites

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SystemConfigParamsEditInputInstallationSites from a JSON string
device_type4_system_config_params_edit_input_installation_sites_instance = DeviceType4SystemConfigParamsEditInputInstallationSites.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SystemConfigParamsEditInputInstallationSites.to_json())

# convert the object into a dict
device_type4_system_config_params_edit_input_installation_sites_dict = device_type4_system_config_params_edit_input_installation_sites_instance.to_dict()
# create an instance of DeviceType4SystemConfigParamsEditInputInstallationSites from a dict
device_type4_system_config_params_edit_input_installation_sites_from_dict = DeviceType4SystemConfigParamsEditInputInstallationSites.from_dict(device_type4_system_config_params_edit_input_installation_sites_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


