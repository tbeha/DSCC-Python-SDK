# BulkMergeCandidatesObjectHostGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duplicate_ids** | **List[str]** | host group ids of all avialable duplicates | [optional] 
**id** | **str** | Identifier for duplicate host group. | [optional] 
**members** | **List[str]** | Host names of all hosts associated to the host group | [optional] 
**name** | **str** | Name of the host group. | [optional] 
**systems** | **List[str]** | system IDs to which the host group belongs to. | [optional] 

## Example

```python
from dscc.models.bulk_merge_candidates_object_host_group import BulkMergeCandidatesObjectHostGroup

# TODO update the JSON string below
json = "{}"
# create an instance of BulkMergeCandidatesObjectHostGroup from a JSON string
bulk_merge_candidates_object_host_group_instance = BulkMergeCandidatesObjectHostGroup.from_json(json)
# print the JSON string representation of the object
print(BulkMergeCandidatesObjectHostGroup.to_json())

# convert the object into a dict
bulk_merge_candidates_object_host_group_dict = bulk_merge_candidates_object_host_group_instance.to_dict()
# create an instance of BulkMergeCandidatesObjectHostGroup from a dict
bulk_merge_candidates_object_host_group_from_dict = BulkMergeCandidatesObjectHostGroup.from_dict(bulk_merge_candidates_object_host_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


