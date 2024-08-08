# AccessControlRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_protocol** | **str** | Access protocol of snapshot or volume. Possible values: &#39;iscsi&#39;, &#39;fc&#39;. | [optional] 
**acl_id** | **str** | ID of access control record. | [optional] 
**apply_to** | **str** | State of apply to. Possible values: &#39;volume&#39;. &#39;pe&#39;, &#39;vvol_volume&#39;, &#39;vvol_snapshot&#39;, &#39;snapshot&#39;, &#39;both&#39;. | [optional] 
**chap_user_id** | **str** | ID of chap user. | [optional] 
**chap_user_name** | **str** | Name of chap user. | [optional] 
**id** | **str** | ID of access control record. | [optional] 
**initiator_group_id** | **str** | ID of initiator group. | [optional] 
**initiator_group_name** | **str** | Name of initiator group. | [optional] 
**lun** | **int** | LUN of snapshot or volume. Secondary LUN if this is Virtual Volume. | [optional] 
**pe_id** | **str** | ID of protocol endpoint. | [optional] 
**pe_lun** | **int** | LUN of protocol endpoint. | [optional] 
**pe_name** | **str** | Name of protocol endpoint. | [optional] 
**snap_id** | **str** | ID of snapshot. | [optional] 
**snap_name** | **str** | Name of snapshot. | [optional] 
**snapluns** | [**List[SnapshotLunInfo]**](SnapshotLunInfo.md) |  | [optional] 
**vol_id** | **str** | ID of volume. | [optional] 
**vol_name** | **str** | Name of volume. | [optional] 

## Example

```python
from dscc.models.access_control_record import AccessControlRecord

# TODO update the JSON string below
json = "{}"
# create an instance of AccessControlRecord from a JSON string
access_control_record_instance = AccessControlRecord.from_json(json)
# print the JSON string representation of the object
print(AccessControlRecord.to_json())

# convert the object into a dict
access_control_record_dict = access_control_record_instance.to_dict()
# create an instance of AccessControlRecord from a dict
access_control_record_from_dict = AccessControlRecord.from_dict(access_control_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


