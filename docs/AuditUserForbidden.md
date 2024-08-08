# AuditUserForbidden


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **object** | Possible values: FORBIDDEN | [optional] 
**error** | **str** | A user friendly error message | 
**trace_id** | **str** | A unique identifier for the request | 

## Example

```python
from dscc.models.audit_user_forbidden import AuditUserForbidden

# TODO update the JSON string below
json = "{}"
# create an instance of AuditUserForbidden from a JSON string
audit_user_forbidden_instance = AuditUserForbidden.from_json(json)
# print the JSON string representation of the object
print(AuditUserForbidden.to_json())

# convert the object into a dict
audit_user_forbidden_dict = audit_user_forbidden_instance.to_dict()
# create an instance of AuditUserForbidden from a dict
audit_user_forbidden_from_dict = AuditUserForbidden.from_dict(audit_user_forbidden_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


