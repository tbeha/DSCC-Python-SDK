# BulkMergeCandidatesObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duplicate_ids** | **List[str]** | host ids of all avialable duplicates | [optional] 
**id** | **str** | Identifier for duplicate host. | [optional] 
**members** | **List[str]** | initiator addresses of all initiaors | [optional] 
**name** | **str** | Name of the host. | [optional] 
**systems** | **List[str]** | system IDs to which the host belongs to. | [optional] 

## Example

```python
from dscc.models.bulk_merge_candidates_object import BulkMergeCandidatesObject

# TODO update the JSON string below
json = "{}"
# create an instance of BulkMergeCandidatesObject from a JSON string
bulk_merge_candidates_object_instance = BulkMergeCandidatesObject.from_json(json)
# print the JSON string representation of the object
print(BulkMergeCandidatesObject.to_json())

# convert the object into a dict
bulk_merge_candidates_object_dict = bulk_merge_candidates_object_instance.to_dict()
# create an instance of BulkMergeCandidatesObject from a dict
bulk_merge_candidates_object_from_dict = BulkMergeCandidatesObject.from_dict(bulk_merge_candidates_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


