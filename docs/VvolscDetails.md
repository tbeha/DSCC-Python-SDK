# VvolscDetails

Storage container details for a device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**auto_dissmissed** | **int** | name of the resource | [optional] 
**comment** | **str** | name of the resource | [optional] 
**console_uri** | **str** | consoleUri for detailed storage container object | [optional] 
**creation_time** | [**DeviceType4vVolscDetailsCreationTime**](DeviceType4vVolscDetailsCreationTime.md) |  | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | domain of the storage container | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**id** | **str** | UID of the storage container | [optional] 
**in_use_mi_b** | **int** | space used by the storage container | [optional] 
**last_modified_epoch** | **int** | Last Modified time of the resource | [optional] 
**name** | **str** | name of the resource | [optional] 
**num_of_vms** | **int** | no. of VMs in storage container | [optional] 
**num_of_vvols** | **int** | no. of vVols in storage container | [optional] 
**provisioned_mi_b** | **int** | provisioned size of storage container | [optional] 
**resource_uri** | **str** | resourceUri for detailed storage container object | [optional] 
**sc_uuid** | **str** | sc_uuid of storage container | [optional] 
**system_id** | **str** | systemId of the resource | [optional] 
**system_wwn** | **str** | systemWWN of the resource | [optional] 
**total_mi_b** | **int** | name of the resource | [optional] 
**type** | **str** | type of the resource | [optional] 
**uri** | **str** | uri for the storage container | [optional] 
**vv_set_id** | **int** | vvSetId of the storage container | [optional] 

## Example

```python
from dscc.models.vvolsc_details import VvolscDetails

# TODO update the JSON string below
json = "{}"
# create an instance of VvolscDetails from a JSON string
vvolsc_details_instance = VvolscDetails.from_json(json)
# print the JSON string representation of the object
print(VvolscDetails.to_json())

# convert the object into a dict
vvolsc_details_dict = vvolsc_details_instance.to_dict()
# create an instance of VvolscDetails from a dict
vvolsc_details_from_dict = VvolscDetails.from_dict(vvolsc_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


