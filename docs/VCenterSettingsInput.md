# VCenterSettingsInput

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
from dscc.models.v_center_settings_input import VCenterSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of VCenterSettingsInput from a JSON string
v_center_settings_input_instance = VCenterSettingsInput.from_json(json)
# print the JSON string representation of the object
print(VCenterSettingsInput.to_json())

# convert the object into a dict
v_center_settings_input_dict = v_center_settings_input_instance.to_dict()
# create an instance of VCenterSettingsInput from a dict
v_center_settings_input_from_dict = VCenterSettingsInput.from_dict(v_center_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


