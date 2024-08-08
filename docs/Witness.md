# Witness


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the replication partner on which quorum witness is configured. &#x60;Filter,Sort&#x60; | [optional] 
**associated_links** | [**List[DeviceType4ReplicationPartnerCommonFieldsAssociatedLinksInner]**](DeviceType4ReplicationPartnerCommonFieldsAssociatedLinksInner.md) | Associated Links | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**is_remote_array_support_replication** | **bool** | Boolean value to indicate if remote array OS version supports replication | [optional] 
**name** | **str** | Name of replication partner on which quorum witness is configured | [optional] 
**quorum_atf_timeout** | **int** | Automatic Transparent Failover quorum partner failure timeout. | [optional] 
**quorum_ip_address** | **str** | Quorum IP Address associated with the partner. Set to &#39;NA&#39; if not available. | [optional] 
**quorum_ssl_port** | **int** | Quorum SSL port number. | [optional] 
**quorum_status** | **str** | Quorum status of the partner. Possible values - Uninitialized, Initializing,Started, Not-started, Standby, Active, Failsafe, Failover or Restarting. Null if unset. | [optional] 
**quorum_status_qual** | **str** | Quorum status qualifier. Set to &#39;NA&#39; if not available. | [optional] 
**quorum_version** | **str** | Quorum version. | [optional] 
**remote_id** | **str** | Id of the remote replication partner on which quorum witness is configured | [optional] 
**remote_name** | **str** | Name of the remote replication partner on which quorum witness is configured | [optional] 
**remote_system_id** | **str** | Unique ID or serial number of the remote system. | [optional] 
**remote_system_name** | **str** | Name of the remote system. | [optional] 
**resource_uri** | **str** | resourceUri for quorum witness object | [optional] 
**system_id** | **str** | Unique ID or serial number of the system. | [optional] 
**system_name** | **str** | Name of the source system. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.witness import Witness

# TODO update the JSON string below
json = "{}"
# create an instance of Witness from a JSON string
witness_instance = Witness.from_json(json)
# print the JSON string representation of the object
print(Witness.to_json())

# convert the object into a dict
witness_dict = witness_instance.to_dict()
# create an instance of Witness from a dict
witness_from_dict = Witness.from_dict(witness_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


