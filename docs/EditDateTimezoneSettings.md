# EditDateTimezoneSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **int** | Unix epoch time local to the group. Seconds since last epoch i.e. 00:00 January 1, 1970. Setting this along with ntp_server causes ntp_server to be reset. | [optional] 
**ntp_server** | **str** | Either IP address or hostname of the NTP server for this group. | [optional] 
**timezone** | **str** | Timezone in which this group is located. Plain string. | [optional] 

## Example

```python
from dscc.models.edit_date_timezone_settings import EditDateTimezoneSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EditDateTimezoneSettings from a JSON string
edit_date_timezone_settings_instance = EditDateTimezoneSettings.from_json(json)
# print the JSON string representation of the object
print(EditDateTimezoneSettings.to_json())

# convert the object into a dict
edit_date_timezone_settings_dict = edit_date_timezone_settings_instance.to_dict()
# create an instance of EditDateTimezoneSettings from a dict
edit_date_timezone_settings_from_dict = EditDateTimezoneSettings.from_dict(edit_date_timezone_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


