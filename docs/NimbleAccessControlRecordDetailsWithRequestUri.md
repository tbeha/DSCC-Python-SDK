# NimbleAccessControlRecordDetailsWithRequestUri


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str** | requestUri for detailed access-control-record object | [optional] 
**access_protocol** | **str** | Access protocol of the volume. Possible values:&#39;iscsi&#39;, &#39;fc&#39;. | [optional] 
**chap_user_id** | **str** | Identifier for the CHAP user. | [optional] 
**chap_user_name** | **str** | Flag denoting if data in the associated volume should be compressed. | [optional] 
**creation_time** | **int** | Time when this access control record was created. | [optional] 
**id** | **str** | Identifier for the access control record. | [optional] 
**initiator_group_id** | **str** | Identifier for the initiator group. | [optional] 
**initiator_group_name** | **str** | Name of the initiator group. (this argument is deprecated) | [optional] 
**last_modified** | **int** | Time when this access control record was last modified. | [optional] 
**lun** | **int** | If this access control record applies to a regular volume, this attribute is the volume&#39;s LUN (Logical Unit Number). If the access protocol is iSCSI, the LUN will be 0. However, if the access protocol is Fibre Channel, the LUN will be in the range from 0 to 2047. If this record applies to a Virtual Volume, this attribute is the volume&#39;s secondary LUN in the range from 0 to 399999, for both iSCSI and Fibre Channel. If the record applies to a OpenstackV2 volume, the LUN will be in the range from 0 to 2047, for both iSCSI and Fibre Channel. If this record applies to a protocol endpoint or only a snapshot, this attribute is not meaningful and is set to null. | [optional] 
**pe_id** | **str** | Identifier for the protocol endpoint this access control record applies to. | [optional] 
**pe_lun** | **int** | LUN (Logical Unit Number) to associate with this protocol endpoint. Valid LUNs are in the 0-2047 range. | [optional] 
**pe_name** | **str** | Name of the protocol endpoint this access control record applies to. | [optional] 
**snap_id** | **str** | Identifier for the snapshot this access control record applies to. | [optional] 
**snap_name** | **str** | Name of the snapshot this access control record applies to. | [optional] 
**vol_id** | **str** | Identifier for the volume this access control record applies to. | [optional] 
**vol_name** | **str** | Name of the volume this access control record applies to. | [optional] 
**apply_to** | **str** | External management agent type. Possible values:&#39;volume&#39;, &#39;pe&#39;, &#39;vvol_volume&#39;, &#39;vvol_snapshot&#39;, &#39;snapshot&#39;, &#39;both&#39;. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**pe_ids** | **List[Optional[str]]** | List of candidate protocol endpoints that may be used to access the Virtual Volume. One of them will be selected for the access control record. This field is required only when creating an access control record for a Virtual Volume. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**snapluns** | [**List[NimbleNsSnapLunInfo]**](NimbleNsSnapLunInfo.md) | Information about the snapshot LUNs associated with this access control record. This field is meaningful when the online snapshot can be accessed as a LUN in the group. | [optional] 
**type** | **str** | type | [optional] 
**vol_agent_type** | **str** | External management agent type. Possible values:&#39;smis&#39;, &#39;vvol&#39;, &#39;openstack&#39;, &#39;openstackv2&#39;, &#39;none&#39;. | [optional] 

## Example

```python
from dscc.models.nimble_access_control_record_details_with_request_uri import NimbleAccessControlRecordDetailsWithRequestUri

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleAccessControlRecordDetailsWithRequestUri from a JSON string
nimble_access_control_record_details_with_request_uri_instance = NimbleAccessControlRecordDetailsWithRequestUri.from_json(json)
# print the JSON string representation of the object
print(NimbleAccessControlRecordDetailsWithRequestUri.to_json())

# convert the object into a dict
nimble_access_control_record_details_with_request_uri_dict = nimble_access_control_record_details_with_request_uri_instance.to_dict()
# create an instance of NimbleAccessControlRecordDetailsWithRequestUri from a dict
nimble_access_control_record_details_with_request_uri_from_dict = NimbleAccessControlRecordDetailsWithRequestUri.from_dict(nimble_access_control_record_details_with_request_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


