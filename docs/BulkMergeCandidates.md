# BulkMergeCandidates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BulkMergeCandidatesObjectHostGroup]**](BulkMergeCandidatesObjectHostGroup.md) |  | [optional] 
**request_uri** | **str** | requestUri for host initiator groups | [optional] 
**total** | **int** | Number of duplicates | [optional] 

## Example

```python
from dscc.models.bulk_merge_candidates import BulkMergeCandidates

# TODO update the JSON string below
json = "{}"
# create an instance of BulkMergeCandidates from a JSON string
bulk_merge_candidates_instance = BulkMergeCandidates.from_json(json)
# print the JSON string representation of the object
print(BulkMergeCandidates.to_json())

# convert the object into a dict
bulk_merge_candidates_dict = bulk_merge_candidates_instance.to_dict()
# create an instance of BulkMergeCandidates from a dict
bulk_merge_candidates_from_dict = BulkMergeCandidates.from_dict(bulk_merge_candidates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


