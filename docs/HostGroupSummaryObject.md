# HostGroupSummaryObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for host group. | [optional] 
**is_mergable** | **bool** | Indicates whether host group has a duplicate. This field is applicable only when isMergable &#x60;Filter&#x60; is set to true on the GET All else will be set to false always. | [optional] 
**marked_for_delete** | **bool** | Indicates whether host group is marked for deletion or not | [optional] 
**name** | **str** | Name of the host group | [optional] 
**systems** | **List[str]** | system IDs to which the host group belongs to | [optional] 
**user_created** | **bool** | Idicates whether user created host or discovered host | [optional] 

## Example

```python
from dscc.models.host_group_summary_object import HostGroupSummaryObject

# TODO update the JSON string below
json = "{}"
# create an instance of HostGroupSummaryObject from a JSON string
host_group_summary_object_instance = HostGroupSummaryObject.from_json(json)
# print the JSON string representation of the object
print(HostGroupSummaryObject.to_json())

# convert the object into a dict
host_group_summary_object_dict = host_group_summary_object_instance.to_dict()
# create an instance of HostGroupSummaryObject from a dict
host_group_summary_object_from_dict = HostGroupSummaryObject.from_dict(host_group_summary_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


