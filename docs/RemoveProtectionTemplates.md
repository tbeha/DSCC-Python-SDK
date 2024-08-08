# RemoveProtectionTemplates

Request body for deleting protection templates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_templates** | [**List[ProtectionTemplateAction]**](ProtectionTemplateAction.md) | List of protection templates  to be deleted | 

## Example

```python
from dscc.models.remove_protection_templates import RemoveProtectionTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveProtectionTemplates from a JSON string
remove_protection_templates_instance = RemoveProtectionTemplates.from_json(json)
# print the JSON string representation of the object
print(RemoveProtectionTemplates.to_json())

# convert the object into a dict
remove_protection_templates_dict = remove_protection_templates_instance.to_dict()
# create an instance of RemoveProtectionTemplates from a dict
remove_protection_templates_from_dict = RemoveProtectionTemplates.from_dict(remove_protection_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


