# ReplicationVolumeCollectionSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of volume collection | [optional] 

## Example

```python
from dscc.models.replication_volume_collection_summary import ReplicationVolumeCollectionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationVolumeCollectionSummary from a JSON string
replication_volume_collection_summary_instance = ReplicationVolumeCollectionSummary.from_json(json)
# print the JSON string representation of the object
print(ReplicationVolumeCollectionSummary.to_json())

# convert the object into a dict
replication_volume_collection_summary_dict = replication_volume_collection_summary_instance.to_dict()
# create an instance of ReplicationVolumeCollectionSummary from a dict
replication_volume_collection_summary_from_dict = ReplicationVolumeCollectionSummary.from_dict(replication_volume_collection_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


