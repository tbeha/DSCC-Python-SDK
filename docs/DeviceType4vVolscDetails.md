# DeviceType4vVolscDetails

Storage container details for a device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[DeviceType4AssociatedLinksInner]**](DeviceType4AssociatedLinksInner.md) | Associated Links Details | [optional] 
**auto_dissmissed** | **int** | name of the resource | [optional] 
**comment** | **str** | comments | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**creation_time** | [**DeviceType4vVolscDetailsCreationTime**](DeviceType4vVolscDetailsCreationTime.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**display_name** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | domain of the storage container | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**growth_limit_mi_b** | **float** | Indicates that the auto-grow operation is limited to the specified storage amount. | [optional] 
**growth_size_mi_b** | **float** | Indicates the growth increment size, the amount of logical disk storage created on each auto-grow operation. | [optional] 
**growth_warn_mi_b** | **float** | Indicates that the threshold of used logical disk space, when exceeded, results in a warning alert. | [optional] 
**host_groups** | [**List[HostGroupDetails]**](HostGroupDetails.md) | Hosts | [optional] 
**host_list** | **List[str]** | vVols storage container host list | [optional] 
**hosts** | [**List[HostDetails]**](HostDetails.md) | Hosts | [optional] 
**id** | **str** | UID of the storage container | [optional] 
**in_use_mi_b** | **int** | space used by the storage container | [optional] 
**name** | **str** | name of the resource | [optional] 
**num_of_vms** | **int** | no. of VMs in storage container | [optional] 
**num_of_vvols** | **int** | no. of vVols in storage container | [optional] 
**pevvs** | **List[str]** | vVols storage container PEVV list | [optional] 
**provisioned_mi_b** | **int** | provisioned size of storage container | [optional] 
**resource_uri** | **str** | resourceUri for detailed snmpUsers object | [optional] 
**sc_id** | **str** | The ID of the vvset that represent the storage container | [optional] 
**sc_uuid** | **str** | sc_uuid of storage container | [optional] 
**sc_id** | **int** | ID of the storage container | [optional] 
**sc_type** | **str** | The type of the storage container. | [optional] 
**system_id** | **str** | systemId of the resource | [optional] 
**system_wwn** | **str** | systemWWN of the resource | [optional] 
**total_mi_b** | **int** | name of the resource | [optional] 
**type** | **str** | type of the resource | [optional] 
**uri** | **str** | uri for the storage container | [optional] 

## Example

```python
from dscc.models.device_type4v_volsc_details import DeviceType4vVolscDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4vVolscDetails from a JSON string
device_type4v_volsc_details_instance = DeviceType4vVolscDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4vVolscDetails.to_json())

# convert the object into a dict
device_type4v_volsc_details_dict = device_type4v_volsc_details_instance.to_dict()
# create an instance of DeviceType4vVolscDetails from a dict
device_type4v_volsc_details_from_dict = DeviceType4vVolscDetails.from_dict(device_type4v_volsc_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


