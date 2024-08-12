# DeviceType4SetLicenseParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_key** | **str** | License Key | [optional] 

## Example

```python
from dscc.models.device_type4_set_license_parameters import DeviceType4SetLicenseParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SetLicenseParameters from a JSON string
device_type4_set_license_parameters_instance = DeviceType4SetLicenseParameters.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SetLicenseParameters.to_json())

# convert the object into a dict
device_type4_set_license_parameters_dict = device_type4_set_license_parameters_instance.to_dict()
# create an instance of DeviceType4SetLicenseParameters from a dict
device_type4_set_license_parameters_from_dict = DeviceType4SetLicenseParameters.from_dict(device_type4_set_license_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


