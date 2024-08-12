# SystemSettingsDetailsSrinfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percent_used** | **float** | Used Percentage | [optional] 
**total_capacity_mi_b** | **float** | Total Capacity in MiB | [optional] 
**used_capacity_mi_b** | **float** | Used Capacity in MiB, this attribute will be updated at most once in 24 hours | [optional] 

## Example

```python
from dscc.models.system_settings_details_srinfo import SystemSettingsDetailsSrinfo

# TODO update the JSON string below
json = "{}"
# create an instance of SystemSettingsDetailsSrinfo from a JSON string
system_settings_details_srinfo_instance = SystemSettingsDetailsSrinfo.from_json(json)
# print the JSON string representation of the object
print(SystemSettingsDetailsSrinfo.to_json())

# convert the object into a dict
system_settings_details_srinfo_dict = system_settings_details_srinfo_instance.to_dict()
# create an instance of SystemSettingsDetailsSrinfo from a dict
system_settings_details_srinfo_from_dict = SystemSettingsDetailsSrinfo.from_dict(system_settings_details_srinfo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


