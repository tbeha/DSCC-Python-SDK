# RemoveProtectionPoliciesInputSchema

Request body to remove protection policies

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[RemoveProtectionPolicyInputSchema]**](RemoveProtectionPolicyInputSchema.md) | List of protection policies to be removed | 

## Example

```python
from dscc.models.remove_protection_policies_input_schema import RemoveProtectionPoliciesInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveProtectionPoliciesInputSchema from a JSON string
remove_protection_policies_input_schema_instance = RemoveProtectionPoliciesInputSchema.from_json(json)
# print the JSON string representation of the object
print(RemoveProtectionPoliciesInputSchema.to_json())

# convert the object into a dict
remove_protection_policies_input_schema_dict = remove_protection_policies_input_schema_instance.to_dict()
# create an instance of RemoveProtectionPoliciesInputSchema from a dict
remove_protection_policies_input_schema_from_dict = RemoveProtectionPoliciesInputSchema.from_dict(remove_protection_policies_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


