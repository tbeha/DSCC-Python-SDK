# AuditResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of any associated resource (e.g. device, volume, etc.) | 
**name** | **str** | Name of any associated resource | 
**type** | **str** | Type of any associated resource | 

## Example

```python
from dscc.models.audit_resource import AuditResource

# TODO update the JSON string below
json = "{}"
# create an instance of AuditResource from a JSON string
audit_resource_instance = AuditResource.from_json(json)
# print the JSON string representation of the object
print(AuditResource.to_json())

# convert the object into a dict
audit_resource_dict = audit_resource_instance.to_dict()
# create an instance of AuditResource from a dict
audit_resource_from_dict = AuditResource.from_dict(audit_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


