# HostGroupSummaryObjectDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_systems** | **List[Optional[str]]** | system IDs to which the host group belongs to. | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**id** | **str** | Identifier for host group. | [optional] 
**is_mergable** | **bool** | Indicates whether host has a duplicate. This field is applicable only when isMergable &#x60;Filter&#x60; is set to true on the GET All else will be set to false always. | [optional] 
**marked_for_delete** | **bool** | Indicates whether host group is marked for deletion or not | [optional] 
**name** | **str** | Name of the host group | [optional] 
**systems** | **List[Optional[str]]** | system IDs to which the host group belongs to. (This field is deprecated) | [optional] 
**type** | **str** | The type of resource. | [optional] 
**user_created** | **bool** | Idicates whether user created host group or discovered host group. (This field is deprecated) | [optional] 

## Example

```python
from dscc.models.host_group_summary_object_details import HostGroupSummaryObjectDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostGroupSummaryObjectDetails from a JSON string
host_group_summary_object_details_instance = HostGroupSummaryObjectDetails.from_json(json)
# print the JSON string representation of the object
print(HostGroupSummaryObjectDetails.to_json())

# convert the object into a dict
host_group_summary_object_details_dict = host_group_summary_object_details_instance.to_dict()
# create an instance of HostGroupSummaryObjectDetails from a dict
host_group_summary_object_details_from_dict = HostGroupSummaryObjectDetails.from_dict(host_group_summary_object_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


