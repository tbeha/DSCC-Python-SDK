# AuditInternalServerError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **object** | Possible values: INTERNAL_ERROR | [optional] 
**error** | **str** | A user friendly error message | 
**trace_id** | **str** | A unique identifier for the request | 

## Example

```python
from dscc.models.audit_internal_server_error import AuditInternalServerError

# TODO update the JSON string below
json = "{}"
# create an instance of AuditInternalServerError from a JSON string
audit_internal_server_error_instance = AuditInternalServerError.from_json(json)
# print the JSON string representation of the object
print(AuditInternalServerError.to_json())

# convert the object into a dict
audit_internal_server_error_dict = audit_internal_server_error_instance.to_dict()
# create an instance of AuditInternalServerError from a dict
audit_internal_server_error_from_dict = AuditInternalServerError.from_dict(audit_internal_server_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


