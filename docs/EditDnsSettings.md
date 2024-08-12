# EditDnsSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_servers** | [**List[IPAddressObject]**](IPAddressObject.md) | IP addresses for this groups dns servers. List of IP Addresses. | [optional] 
**domain_name** | **str** | Domain name for this group. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character. | [optional] 

## Example

```python
from dscc.models.edit_dns_settings import EditDnsSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EditDnsSettings from a JSON string
edit_dns_settings_instance = EditDnsSettings.from_json(json)
# print the JSON string representation of the object
print(EditDnsSettings.to_json())

# convert the object into a dict
edit_dns_settings_dict = edit_dns_settings_instance.to_dict()
# create an instance of EditDnsSettings from a dict
edit_dns_settings_from_dict = EditDnsSettings.from_dict(edit_dns_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


