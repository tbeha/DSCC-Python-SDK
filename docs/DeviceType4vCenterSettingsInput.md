# DeviceType4vCenterSettingsInput

Request body to add vCenter Settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_chain_pem** | **str** | Certificate chain of the VCenter server as PEM data | [optional] 
**description** | **str** | Description of the vCenter setting | [optional] 
**inetaddress** | **str** | Host name or IP address of vCenter server | 
**name** | **str** | Name of the vCenter setting | 
**password** | **str** | Password to login to the vCenter server | 
**port** | **int** | Port number of the vCenter server. | 
**username** | **str** | Username to login to the vCenter server | 

## Example

```python
from dscc.models.device_type4v_center_settings_input import DeviceType4vCenterSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4vCenterSettingsInput from a JSON string
device_type4v_center_settings_input_instance = DeviceType4vCenterSettingsInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4vCenterSettingsInput.to_json())

# convert the object into a dict
device_type4v_center_settings_input_dict = device_type4v_center_settings_input_instance.to_dict()
# create an instance of DeviceType4vCenterSettingsInput from a dict
device_type4v_center_settings_input_from_dict = DeviceType4vCenterSettingsInput.from_dict(device_type4v_center_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


