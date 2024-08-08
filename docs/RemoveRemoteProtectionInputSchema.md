# RemoveRemoteProtectionInputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** | Replication partner ID where remote protection is created | 

## Example

```python
from dscc.models.remove_remote_protection_input_schema import RemoveRemoteProtectionInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveRemoteProtectionInputSchema from a JSON string
remove_remote_protection_input_schema_instance = RemoveRemoteProtectionInputSchema.from_json(json)
# print the JSON string representation of the object
print(RemoveRemoteProtectionInputSchema.to_json())

# convert the object into a dict
remove_remote_protection_input_schema_dict = remove_remote_protection_input_schema_instance.to_dict()
# create an instance of RemoveRemoteProtectionInputSchema from a dict
remove_remote_protection_input_schema_from_dict = RemoveRemoteProtectionInputSchema.from_dict(remove_remote_protection_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


