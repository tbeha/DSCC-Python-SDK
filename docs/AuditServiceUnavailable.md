# AuditServiceUnavailable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **object** | Possible values: SERVICE_UNAVAILABLE | [optional] 
**error** | **str** | A user friendly error message | 
**trace_id** | **str** | A unique identifier for the request | 

## Example

```python
from dscc.models.audit_service_unavailable import AuditServiceUnavailable

# TODO update the JSON string below
json = "{}"
# create an instance of AuditServiceUnavailable from a JSON string
audit_service_unavailable_instance = AuditServiceUnavailable.from_json(json)
# print the JSON string representation of the object
print(AuditServiceUnavailable.to_json())

# convert the object into a dict
audit_service_unavailable_dict = audit_service_unavailable_instance.to_dict()
# create an instance of AuditServiceUnavailable from a dict
audit_service_unavailable_from_dict = AuditServiceUnavailable.from_dict(audit_service_unavailable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


