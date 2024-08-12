# BulkMergeCandidatesHosts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BulkMergeCandidatesObject]**](BulkMergeCandidatesObject.md) |  | [optional] 
**request_uri** | **str** | requestUri for host initiators | [optional] 
**total** | **int** | Number of duplicates | [optional] 

## Example

```python
from dscc.models.bulk_merge_candidates_hosts import BulkMergeCandidatesHosts

# TODO update the JSON string below
json = "{}"
# create an instance of BulkMergeCandidatesHosts from a JSON string
bulk_merge_candidates_hosts_instance = BulkMergeCandidatesHosts.from_json(json)
# print the JSON string representation of the object
print(BulkMergeCandidatesHosts.to_json())

# convert the object into a dict
bulk_merge_candidates_hosts_dict = bulk_merge_candidates_hosts_instance.to_dict()
# create an instance of BulkMergeCandidatesHosts from a dict
bulk_merge_candidates_hosts_from_dict = BulkMergeCandidatesHosts.from_dict(bulk_merge_candidates_hosts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


