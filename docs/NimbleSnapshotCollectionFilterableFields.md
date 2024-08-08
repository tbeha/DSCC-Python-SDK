# NimbleSnapshotCollectionFilterableFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_locked_snapshots** | **bool** | To verify a snapshot collection has any immutable snapshot or not. | [optional] 
**id** | **str** | Identifier for the snapshot collection. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of snapshot. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. &#x60;Filter, Sort&#x60; | [optional] 
**online_status** | **str** | Online status of snapshot collection. This is based on the online status of the individual snapshots. Online status based on that of the constituent entities. Possible values: &#39;online&#39;, &#39;offline&#39; or &#39;partial&#39;. | [optional] 
**schedule_id** | **str** | Identifier of protection schedule. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**srep_owner_id** | **str** | ID of the partner where snapshots for this snapshot collection reside which were created by synchronous replication. Field will be null if no peer snapshot_collection was created by synchronous replication. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**volcoll_id** | **str** | Parent volume collection ID. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.nimble_snapshot_collection_filterable_fields import NimbleSnapshotCollectionFilterableFields

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleSnapshotCollectionFilterableFields from a JSON string
nimble_snapshot_collection_filterable_fields_instance = NimbleSnapshotCollectionFilterableFields.from_json(json)
# print the JSON string representation of the object
print(NimbleSnapshotCollectionFilterableFields.to_json())

# convert the object into a dict
nimble_snapshot_collection_filterable_fields_dict = nimble_snapshot_collection_filterable_fields_instance.to_dict()
# create an instance of NimbleSnapshotCollectionFilterableFields from a dict
nimble_snapshot_collection_filterable_fields_from_dict = NimbleSnapshotCollectionFilterableFields.from_dict(nimble_snapshot_collection_filterable_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


