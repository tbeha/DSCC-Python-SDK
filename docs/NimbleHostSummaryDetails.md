# NimbleHostSummaryDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_protocol** | **str** | Access protocol of the volume. Possible values:&#39;iscsi&#39;, &#39;fc&#39;. | [optional] 
**acr_id** | **str** | Identifier of the access control record. | [optional] 
**apply_to** | **str** | Type of object this access control record applies to. Possible values: &#39;volume&#39;. &#39;pe&#39;, &#39;vvol_volume&#39;, &#39;vvol_snapshot&#39;, &#39;snapshot&#39;, &#39;both&#39;. | [optional] 
**chap_user_id** | **str** | Identifier for the CHAP user. | [optional] 
**chap_user_name** | **str** | Flag denoting if data in the associated volume should be compressed. | [optional] 
**fc_initiators** | [**List[FCInitiatorList]**](FCInitiatorList.md) | list of FC Initiators | [optional] 
**fc_target_ports** | [**List[FCPortList]**](FCPortList.md) | list of FC Ports | [optional] 
**host_type** | **str** | type of Host. | [optional] 
**id** | **str** | Identifier for the host id | [optional] 
**initiator_group_id** | **str** | Identifier for the initiator group. &#x60;Filter, Sort&#x60; | [optional] 
**initiator_group_name** | **str** | Name of the initiator group. | [optional] 
**iscsi_initiators** | [**List[IscsiInitiatorList]**](IscsiInitiatorList.md) | list of iscsi Initiators | [optional] 
**lun** | **int** | If this access control record applies to a regular volume, this attribute is the volume&#39;s LUN (Logical Unit Number). If the access protocol is iSCSI, the LUN will be 0. However, if the access protocol is Fibre Channel, the LUN will be in the range from 0 to 2047. If this record applies to a Virtual Volume, this attribute is the volume&#39;s secondary LUN in the range from 0 to 399999, for both iSCSI and Fibre Channel. If the record applies to a OpenstackV2 volume, the LUN will be in the range from 0 to 2047, for both iSCSI and Fibre Channel. If this record applies to a protocol endpoint or only a snapshot, this attribute is not meaningful and is set to null. | [optional] 
**name** | **str** | Name of the host group in the Data Services Cloud Console (DSCC) | [optional] 
**num_connections** | **int** | Number of Connections | [optional] 
**sc_host_id** | **str** | Identifier for the initiator group in the Data Services Cloud Console (DSCC) | [optional] 
**snap_id** | **str** | Identifier for the snapshot this access control record applies to. &#x60;Filter, Sort&#x60; | [optional] 
**user_created** | **bool** | Indicates whether it is user created host or discovered host. | [optional] 

## Example

```python
from dscc.models.nimble_host_summary_details import NimbleHostSummaryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleHostSummaryDetails from a JSON string
nimble_host_summary_details_instance = NimbleHostSummaryDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleHostSummaryDetails.to_json())

# convert the object into a dict
nimble_host_summary_details_dict = nimble_host_summary_details_instance.to_dict()
# create an instance of NimbleHostSummaryDetails from a dict
nimble_host_summary_details_from_dict = NimbleHostSummaryDetails.from_dict(nimble_host_summary_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


