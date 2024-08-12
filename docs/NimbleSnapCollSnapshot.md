# NimbleSnapCollSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_time** | **int** | Unix timestamp indicating that the snapshot is considered expired by Snapshot Time-to-live(TTL). A value of 0 indicates that snapshot never expires. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**id** | **str** | Identifier for the snapshot. A 42 digit hexadecimal number. | [optional] 
**name** | **str** | Name of snapshot. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. | [optional] 
**schedule_id** | **str** | Identifier of protection schedule. A 42 digit hexadecimal number. | [optional] 
**schedule_name** | **str** | Name of protection schedule. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**snap_collection_id** | **str** | Identifier of snapshot collection. A 42 digit hexadecimal number. | [optional] 
**snap_collection_name** | **str** | Name of snapshot collection. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints. | [optional] 
**vol_id** | **str** | Parent volume ID. A 42 digit hexadecimal number. | [optional] 
**vol_name** | **str** | Name of the parent volume in which the snapshot belongs to. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints. | [optional] 
**volume_creator_id** | **str** | Originator id for the volume. | [optional] 
**volume_creator_name** | **str** | Originator name for the volume. | [optional] 

## Example

```python
from dscc.models.nimble_snap_coll_snapshot import NimbleSnapCollSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleSnapCollSnapshot from a JSON string
nimble_snap_coll_snapshot_instance = NimbleSnapCollSnapshot.from_json(json)
# print the JSON string representation of the object
print(NimbleSnapCollSnapshot.to_json())

# convert the object into a dict
nimble_snap_coll_snapshot_dict = nimble_snap_coll_snapshot_instance.to_dict()
# create an instance of NimbleSnapCollSnapshot from a dict
nimble_snap_coll_snapshot_from_dict = NimbleSnapCollSnapshot.from_dict(nimble_snap_coll_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


