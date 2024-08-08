# HostSummaryForHSObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for host. | [optional] 
**initiators** | [**List[InitiatorSummary]**](InitiatorSummary.md) | Initiator to which the host belongs to. | [optional] 
**ip_address** | **str** | IP address of the host. | [optional] 
**is_mergable** | **bool** | Indicates whether host group has a duplicate. This field is applicable only when isMergable &#x60;Filter&#x60; is set to true on the GET All else will be set to false always. | [optional] 
**is_vvol_host** | **bool** | Indicates if this host is created with NVMe initiator to be used by VASA vvol or not | [optional] 
**marked_for_delete** | **bool** | Indicates whether host is marked for deletion or not | [optional] 
**name** | **str** | Name of the host. | [optional] 
**systems** | **List[str]** | system IDs to which the host belongs to | [optional] 
**user_created** | **bool** | Indicates whether user created host or discovered host | [optional] 

## Example

```python
from dscc.models.host_summary_for_hs_object import HostSummaryForHSObject

# TODO update the JSON string below
json = "{}"
# create an instance of HostSummaryForHSObject from a JSON string
host_summary_for_hs_object_instance = HostSummaryForHSObject.from_json(json)
# print the JSON string representation of the object
print(HostSummaryForHSObject.to_json())

# convert the object into a dict
host_summary_for_hs_object_dict = host_summary_for_hs_object_instance.to_dict()
# create an instance of HostSummaryForHSObject from a dict
host_summary_for_hs_object_from_dict = HostSummaryForHSObject.from_dict(host_summary_for_hs_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


