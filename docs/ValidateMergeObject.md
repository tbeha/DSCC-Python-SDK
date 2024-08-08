# ValidateMergeObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_ids** | **List[str]** | host IDs of hosts which are needed to be merged. | 
**name** | **str** | Name of the host being created. | 
**operating_system** | **str** | Host operating system. Possible Values are: - AIX - Apple - Citrix Hypervisor(XenServer) - HP-UX - IBM VIO Server - InForm - NetApp/ONTAP - OE Linux UEK - OpenVMS - Oracle VM x86 - RHE Linux - RHE Virtualization - Solaris - SuSE Linux - SuSE Virtualization - Ubuntu - VMware (ESXi) - Windows Server | 

## Example

```python
from dscc.models.validate_merge_object import ValidateMergeObject

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateMergeObject from a JSON string
validate_merge_object_instance = ValidateMergeObject.from_json(json)
# print the JSON string representation of the object
print(ValidateMergeObject.to_json())

# convert the object into a dict
validate_merge_object_dict = validate_merge_object_instance.to_dict()
# create an instance of ValidateMergeObject from a dict
validate_merge_object_from_dict = ValidateMergeObject.from_dict(validate_merge_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


