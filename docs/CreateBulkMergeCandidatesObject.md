# CreateBulkMergeCandidatesObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duplicate_ids** | **List[str]** | host/hostgroup ids of all avialable duplicates | 
**members** | **List[str]** | List of Initiator address/ List of Host names for the host group | 
**name** | **str** | Name of the host/host group. | 
**systems** | **List[str]** | system IDs to which the host/hostgroup belongs to. | 

## Example

```python
from dscc.models.create_bulk_merge_candidates_object import CreateBulkMergeCandidatesObject

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBulkMergeCandidatesObject from a JSON string
create_bulk_merge_candidates_object_instance = CreateBulkMergeCandidatesObject.from_json(json)
# print the JSON string representation of the object
print(CreateBulkMergeCandidatesObject.to_json())

# convert the object into a dict
create_bulk_merge_candidates_object_dict = create_bulk_merge_candidates_object_instance.to_dict()
# create an instance of CreateBulkMergeCandidatesObject from a dict
create_bulk_merge_candidates_object_from_dict = CreateBulkMergeCandidatesObject.from_dict(create_bulk_merge_candidates_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


