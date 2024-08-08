# DeviceType4RemoveProtectionPoliciesInputSchema

Request body to remove protection policies

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[DeviceType4RemoveProtectionPolicyInputSchema]**](DeviceType4RemoveProtectionPolicyInputSchema.md) | List of protection policies to be removed | 

## Example

```python
from dscc.models.device_type4_remove_protection_policies_input_schema import DeviceType4RemoveProtectionPoliciesInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RemoveProtectionPoliciesInputSchema from a JSON string
device_type4_remove_protection_policies_input_schema_instance = DeviceType4RemoveProtectionPoliciesInputSchema.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RemoveProtectionPoliciesInputSchema.to_json())

# convert the object into a dict
device_type4_remove_protection_policies_input_schema_dict = device_type4_remove_protection_policies_input_schema_instance.to_dict()
# create an instance of DeviceType4RemoveProtectionPoliciesInputSchema from a dict
device_type4_remove_protection_policies_input_schema_from_dict = DeviceType4RemoveProtectionPoliciesInputSchema.from_dict(device_type4_remove_protection_policies_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


