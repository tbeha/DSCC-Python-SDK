# DeviceType4RemoveRemoteProtectionInputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** | Replication partner ID where remote protection is created | 

## Example

```python
from dscc.models.device_type4_remove_remote_protection_input_schema import DeviceType4RemoveRemoteProtectionInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RemoveRemoteProtectionInputSchema from a JSON string
device_type4_remove_remote_protection_input_schema_instance = DeviceType4RemoveRemoteProtectionInputSchema.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RemoveRemoteProtectionInputSchema.to_json())

# convert the object into a dict
device_type4_remove_remote_protection_input_schema_dict = device_type4_remove_remote_protection_input_schema_instance.to_dict()
# create an instance of DeviceType4RemoveRemoteProtectionInputSchema from a dict
device_type4_remove_remote_protection_input_schema_from_dict = DeviceType4RemoveRemoteProtectionInputSchema.from_dict(device_type4_remove_remote_protection_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


