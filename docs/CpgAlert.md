# CpgAlert

Information for posted alerts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fail** | **str** | Alert when there is a growth failure for admin/data space | [optional] 
**limit** | **str** | Alert corresponding to limit for admin/data space | [optional] 
**warn** | **str** | Alert corresponding to warning for admin/data space | [optional] 
**warn_percent** | **float** | Alert corresponding to warning percentage for admin/data space | [optional] 

## Example

```python
from dscc.models.cpg_alert import CpgAlert

# TODO update the JSON string below
json = "{}"
# create an instance of CpgAlert from a JSON string
cpg_alert_instance = CpgAlert.from_json(json)
# print the JSON string representation of the object
print(CpgAlert.to_json())

# convert the object into a dict
cpg_alert_dict = cpg_alert_instance.to_dict()
# create an instance of CpgAlert from a dict
cpg_alert_from_dict = CpgAlert.from_dict(cpg_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


