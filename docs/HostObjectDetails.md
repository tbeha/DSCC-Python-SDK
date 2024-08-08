# HostObjectDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[ScAssociatedLinksInner]**](ScAssociatedLinksInner.md) | Associated Links Details | [optional] 
**associated_systems** | **List[Optional[str]]** | system IDs to which the host belongs to. | [optional] 
**comment** | **str** | Comment | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**contact** | **str** | Contact information | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**edit_status** | **str** | Host Update or Delete progress status. Possible status are: Update_In_Progress,Update_Success,Update_Failed,Delete_In_Progress,Delete_Failed,Not_Applicable,Merge_Success,Merge_In_Progress,Merge_Failed,Convert_In_Progress,Convert_Failed,Convert_Success. | [optional] 
**fqdn** | **str** | Fully qualified domain name of the host. | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**host_groups** | [**List[HostGroupSummaryObjectDetails]**](HostGroupSummaryObjectDetails.md) | Host group to which the host belongs to. | [optional] 
**id** | **str** | Identifier for host. | [optional] 
**initiators** | [**List[InitiatorObjectDetails]**](InitiatorObjectDetails.md) | Host initiator list this host is associated with. | [optional] 
**ip_address** | **str** | IP address of the host. | [optional] 
**is_mergable** | **bool** | Indicates whether host has a duplicate. This field is applicable only when isMergable &#x60;Filter&#x60; is set to true on the GET All else will be set to false always. | [optional] 
**is_vvol_host** | **bool** | Indicates if this host is created with NVMe initiator to be used by VASA vvol or not | [optional] 
**location** | **str** | location. | [optional] 
**marked_for_delete** | **bool** | Indicates whether host is marked for deletion or not | [optional] 
**model** | **str** | Model | [optional] 
**name** | **str** | Name of the host. | [optional] 
**operating_system** | **str** | Host operating system. | [optional] 
**persona** | **str** | Host persona details. | [optional] 
**protocol** | **str** | protocol supported are : FC ,iSCSI or NVMe | [optional] 
**subnet** | **str** | subnet. | [optional] 
**systems** | **List[Optional[str]]** | system IDs to which the host belongs to. | [optional] 
**type** | **str** | The type of resource. | [optional] 
**user_created** | **bool** | Indicates whether user created host or discovered host | [optional] 

## Example

```python
from dscc.models.host_object_details import HostObjectDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostObjectDetails from a JSON string
host_object_details_instance = HostObjectDetails.from_json(json)
# print the JSON string representation of the object
print(HostObjectDetails.to_json())

# convert the object into a dict
host_object_details_dict = host_object_details_instance.to_dict()
# create an instance of HostObjectDetails from a dict
host_object_details_from_dict = HostObjectDetails.from_dict(host_object_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


