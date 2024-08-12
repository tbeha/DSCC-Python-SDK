# AuditBadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **object** | Possible values: BAD_REQUEST, INVALID_PARAMETER | [optional] 
**error** | **str** | A user friendly error message | 
**trace_id** | **str** | A unique identifier for the request | 

## Example

```python
from dscc.models.audit_bad_request import AuditBadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuditBadRequest from a JSON string
audit_bad_request_instance = AuditBadRequest.from_json(json)
# print the JSON string representation of the object
print(AuditBadRequest.to_json())

# convert the object into a dict
audit_bad_request_dict = audit_bad_request_instance.to_dict()
# create an instance of AuditBadRequest from a dict
audit_bad_request_from_dict = AuditBadRequest.from_dict(audit_bad_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


