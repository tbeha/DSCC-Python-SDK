# CreateBulkMergeCandidates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CreateBulkMergeCandidatesObject]**](CreateBulkMergeCandidatesObject.md) |  | [optional] 

## Example

```python
from dscc.models.create_bulk_merge_candidates import CreateBulkMergeCandidates

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBulkMergeCandidates from a JSON string
create_bulk_merge_candidates_instance = CreateBulkMergeCandidates.from_json(json)
# print the JSON string representation of the object
print(CreateBulkMergeCandidates.to_json())

# convert the object into a dict
create_bulk_merge_candidates_dict = create_bulk_merge_candidates_instance.to_dict()
# create an instance of CreateBulkMergeCandidates from a dict
create_bulk_merge_candidates_from_dict = CreateBulkMergeCandidates.from_dict(create_bulk_merge_candidates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


