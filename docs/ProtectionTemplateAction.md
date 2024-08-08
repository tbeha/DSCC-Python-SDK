# ProtectionTemplateAction

Protection Template input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_template_id** | **str** | The ID of the protection template. A 42 digit hexadecimal number. | [optional] 

## Example

```python
from dscc.models.protection_template_action import ProtectionTemplateAction

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionTemplateAction from a JSON string
protection_template_action_instance = ProtectionTemplateAction.from_json(json)
# print the JSON string representation of the object
print(ProtectionTemplateAction.to_json())

# convert the object into a dict
protection_template_action_dict = protection_template_action_instance.to_dict()
# create an instance of ProtectionTemplateAction from a dict
protection_template_action_from_dict = ProtectionTemplateAction.from_dict(protection_template_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


