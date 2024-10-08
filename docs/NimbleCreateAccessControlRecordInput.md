# NimbleCreateAccessControlRecordInput

Create Nimble access-control record input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_to** | **str** | External management agent type. Possible values:&#39;volume&#39;, &#39;pe&#39;, &#39;vvol_volume&#39;, &#39;vvol_snapshot&#39;, &#39;snapshot&#39;, &#39;both&#39;. | [optional] 
**chap_user_id** | **str** | Identifier for the CHAP user. | [optional] 
**initiator_group_id** | **str** | Identifier for the initiator group. | [optional] 
**lun** | **int** | If this access control record applies to a regular volume, this attribute is the volume&#39;s LUN (Logical Unit Number). If the access protocol is iSCSI, the LUN will be 0. However, if the access protocol is Fibre Channel, the LUN will be in the range from 0 to 2047. If this record applies to a Virtual Volume, this attribute is the volume&#39;s secondary LUN in the range from 0 to 399999, for both iSCSI and Fibre Channel. If the record applies to a OpenstackV2 volume, the LUN will be in the range from 0 to 2047, for both iSCSI and Fibre Channel. If this record applies to a protocol endpoint or only a snapshot, this attribute is not meaningful and is set to null. | [optional] 
**pe_id** | **str** | Identifier for the protocol endpoint this access control record applies to. | [optional] 
**pe_ids** | **List[Optional[str]]** | List of candidate protocol endpoints that may be used to access the Virtual Volume. One of them will be selected for the access control record. This field is required only when creating an access control record for a Virtual Volume. | [optional] 
**snap_id** | **str** | Identifier for the snapshot this access control record applies to. | [optional] 
**system_uid** | **str** | Rest ID of the array containing this controller. &#x60;Filter, Sort&#x60;. This field is deprecated. | [optional] 
**vol_id** | **str** | Identifier for the volume this access control record applies to. | [optional] 

## Example

```python
from dscc.models.nimble_create_access_control_record_input import NimbleCreateAccessControlRecordInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleCreateAccessControlRecordInput from a JSON string
nimble_create_access_control_record_input_instance = NimbleCreateAccessControlRecordInput.from_json(json)
# print the JSON string representation of the object
print(NimbleCreateAccessControlRecordInput.to_json())

# convert the object into a dict
nimble_create_access_control_record_input_dict = nimble_create_access_control_record_input_instance.to_dict()
# create an instance of NimbleCreateAccessControlRecordInput from a dict
nimble_create_access_control_record_input_from_dict = NimbleCreateAccessControlRecordInput.from_dict(nimble_create_access_control_record_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


