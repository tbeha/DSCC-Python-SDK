# VcenterStatus

Status of the vcenter setting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Default status value | [optional] 
**key** | **str** | Status key of vcenter | [optional] 

## Example

```python
from dscc.models.vcenter_status import VcenterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of VcenterStatus from a JSON string
vcenter_status_instance = VcenterStatus.from_json(json)
# print the JSON string representation of the object
print(VcenterStatus.to_json())

# convert the object into a dict
vcenter_status_dict = vcenter_status_instance.to_dict()
# create an instance of VcenterStatus from a dict
vcenter_status_from_dict = VcenterStatus.from_dict(vcenter_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


