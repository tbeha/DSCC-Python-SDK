# NimbleSnapshotCollectionDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str** | requestUri for detailed volume snapshot objects | [optional] 
**has_locked_snapshots** | **bool** | To verify a snapshot collection has any immutable snapshot or not. | [optional] 
**id** | **str** | Identifier for the snapshot collection. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of snapshot. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. &#x60;Filter, Sort&#x60; | [optional] 
**online_status** | **str** | Online status of snapshot collection. This is based on the online status of the individual snapshots. Online status based on that of the constituent entities. Possible values: &#39;online&#39;, &#39;offline&#39; or &#39;partial&#39;. | [optional] 
**schedule_id** | **str** | Identifier of protection schedule. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**srep_owner_id** | **str** | ID of the partner where snapshots for this snapshot collection reside which were created by synchronous replication. Field will be null if no peer snapshot_collection was created by synchronous replication. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**volcoll_id** | **str** | Parent volume collection ID. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**allow_writes** | **bool** | Allow applications to write to created snapshot(s). Mandatory and must be set to &#39;true&#39; for VSS application synchronized snapshots. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**creation_time** | **int** | Time when this snapshot collection was created. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**description** | **str** | Text description of snapshot collection. String of up to 255 printable ASCII characters. | [optional] 
**generation** | **int** | generation | [optional] 
**is_complete** | **bool** | Is complete. | [optional] 
**is_external_trigger** | **bool** | Is externally triggered. | [optional] 
**is_manual** | **bool** | Is manual. | [optional] 
**is_manually_managed** | **bool** | Is snapshot collection manually managed, i.e., snapshot collection is manually or third party created or created by system at the time of volume restore or resize. | [optional] 
**is_mfa_protected** | **bool** | Protected by multi-factor authentication. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**is_replica** | **bool** | Snapshot collection is a replica from upstream replication partner. | [optional] 
**is_unmanaged** | **bool** | Indicates whether a snapshot collection is unmanaged. This is based on the state of individual snapshots. | [optional] 
**last_modified** | **int** | Time when this snapshot collection was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**metadata** | [**List[KeyValue]**](KeyValue.md) | Key-value pairs that augment a snapshot collection&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. | [optional] 
**origin_name** | **str** | Origination group name/ID. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**peer_snapcoll_id** | **str** | ID of the peer snapshot collection created by synchronous replication. Field will be null if no peer snapshot_collection was created by synchronous replication. A 42 digit hexadecimal number. | [optional] 
**repl_status** | **str** | Replication status of snapshot collection | [optional] 
**replicate_to** | **str** | Specifies the partner name that the snapshots in this snapshot collection are replicated to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**snapshots_list** | [**List[NimbleSnapCollSnapshot]**](NimbleSnapCollSnapshot.md) | Snapshot list for a SnapshotCollection | [optional] 
**type** | **str** | type | [optional] 
**volcoll_creator_id** | **str** | Originator id for the volume collection. | [optional] 
**volcoll_creator_name** | **str** | Originator name for the volume collection. | [optional] 

## Example

```python
from dscc.models.nimble_snapshot_collection_details import NimbleSnapshotCollectionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleSnapshotCollectionDetails from a JSON string
nimble_snapshot_collection_details_instance = NimbleSnapshotCollectionDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleSnapshotCollectionDetails.to_json())

# convert the object into a dict
nimble_snapshot_collection_details_dict = nimble_snapshot_collection_details_instance.to_dict()
# create an instance of NimbleSnapshotCollectionDetails from a dict
nimble_snapshot_collection_details_from_dict = NimbleSnapshotCollectionDetails.from_dict(nimble_snapshot_collection_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


