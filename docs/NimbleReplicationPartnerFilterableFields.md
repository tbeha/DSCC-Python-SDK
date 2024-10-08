# NimbleReplicationPartnerFilterableFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_serial** | **str** | Serial number of group leader array of the partner. Plain string. &#x60;Filter, Sort&#x60; | [optional] 
**cfg_sync_status** | **str** | Indicates whether all volumes and volume collections have been synced to the partner. Possible values: N/A, Yes, No &#x60;Filter, Sort&#x60; | [optional] 
**creation_time** | **int** | Time when this replication partner was created. Seconds since last epoch i.e. 00:00 January 1, 1970. &#x60;Filter, Sort&#x60; | [optional] 
**folder_id** | **str** | The Folder ID within the pool where volumes replicated from this partner will be created. This is not supported for pool partners. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**folder_name** | **str** | The Folder name within the pool where volumes replicated from this partner will be created. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. &#x60;Filter, Sort&#x60; | [optional] 
**hostname** | **str** | IP address or hostname of partner interface. This must be the partners Group Management IP address. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Identifier for a replication partner. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**is_alive** | **bool** | Whether the partner is available, and responding to pings. Possible values: true, false &#x60;Filter, Sort&#x60; | [optional] 
**name** | **str** | Name of replication partner. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.&#x60;Filter, Sort&#x60; | [optional] 
**partner_type** | **str** | Type of the partner, Possible values: &#39;group&#39; or &#39;pool&#39;.&#x60;Filter, Sort&#x60; | [optional] 
**paused** | **bool** | Indicates whether replication traffic from/to this partner has been halted. Possible values: true, false &#x60;Filter, Sort&#x60; | [optional] 
**pool_id** | **str** | The pool ID where volumes replicated from this partner will be created. Replica volumes created as clones ignore this parameter and are always created in the same pool as their parent volume. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**pool_name** | **str** | The pool name where volumes replicated from this partner will be created. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. &#x60;Filter, Sort&#x60; | [optional] 
**repl_hostname** | **str** | IP address or hostname of partner data interface. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. &#x60;Filter, Sort&#x60; | [optional] 
**subnet_label** | **str** | Label of the subnet used to replicate to this partner. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. &#x60;Filter, Sort&#x60; | [optional] 
**subnet_netmask** | **str** | Subnet mask used to replicate to this partner. A netmask expressed as a 32 bit binary value must have the highest bit set (2^31) and the lowest bit clear (2^0) with the first zero followed by only zeros. &#x60;Filter, Sort&#x60; | [optional] 
**subnet_network** | **str** | Subnet used to replicate to this partner. Four numbers in the range [0,255] separated by periods. &#x60;Filter, Sort&#x60; | [optional] 
**subnet_type** | **str** | Type of the subnet used to replicate to this partner. Possible values: invalid, unconfigured, mgmt, data, mgmt_data &#x60;Filter, Sort&#x60; | [optional] 
**system_id** | **str** | Identifier for a system or array. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**version** | **int** | Replication version of the partner. Signed 64-bit integer. &#x60;Filter, Sort&#x60; | [optional] 
**volume_collection_list_count** | **int** | Count of volume collections that are replicating from/to this partner. Unsigned 64-bit integer. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.nimble_replication_partner_filterable_fields import NimbleReplicationPartnerFilterableFields

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleReplicationPartnerFilterableFields from a JSON string
nimble_replication_partner_filterable_fields_instance = NimbleReplicationPartnerFilterableFields.from_json(json)
# print the JSON string representation of the object
print(NimbleReplicationPartnerFilterableFields.to_json())

# convert the object into a dict
nimble_replication_partner_filterable_fields_dict = nimble_replication_partner_filterable_fields_instance.to_dict()
# create an instance of NimbleReplicationPartnerFilterableFields from a dict
nimble_replication_partner_filterable_fields_from_dict = NimbleReplicationPartnerFilterableFields.from_dict(nimble_replication_partner_filterable_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


