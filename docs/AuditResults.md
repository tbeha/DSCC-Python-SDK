# AuditResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AuditData]**](AuditData.md) | If query yields results, they will be reported here | 
**page_limit** | **int** | The limit specified in the limit query parameter. | 
**page_offset** | **int** | The offset specified in the offset query parameter. | 
**total** | **int** | Total number of documents matching filter criteria. | 

## Example

```python
from dscc.models.audit_results import AuditResults

# TODO update the JSON string below
json = "{}"
# create an instance of AuditResults from a JSON string
audit_results_instance = AuditResults.from_json(json)
# print the JSON string representation of the object
print(AuditResults.to_json())

# convert the object into a dict
audit_results_dict = audit_results_instance.to_dict()
# create an instance of AuditResults from a dict
audit_results_from_dict = AuditResults.from_dict(audit_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


