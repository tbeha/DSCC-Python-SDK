# ReplicationPartnerObj

The request body for replication partner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_port** | **int** | Port number of partner control interface. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**data_port** | **int** | Port number of partner data interface. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**description** | **str** | Description of replication partner. String of up to 255 printable ASCII characters. | [optional] 
**repl_hostname** | **str** | IP address or hostname of partner data interface. String of up to 64 alphanumeric characters, - and . and colon are allowed after first character. | [optional] 
**source** | [**Source**](Source.md) |  | 
**subnet_label** | **str** | Label of the subnet used to replicate to this partner. String of up to 64 alphanumeric characters, - and . and colon are allowed after first character. | [optional] 
**subnet_type** | **str** | Type of the subnet used to replicate to this partner. Possible values are &#39;invalid&#39;, &#39;unconfigured&#39;, &#39;mgmt&#39;, &#39;data&#39;, &#39;mgmt_data&#39;. | [optional] 
**target** | [**Target**](Target.md) |  | 
**target_system_id** | **str** | Target system ID | 
**throttles** | [**List[ReplicationThrottle]**](ReplicationThrottle.md) | Throttles used while replicating from/to this partner. All the throttles for the partner. | [optional] 

## Example

```python
from dscc.models.replication_partner_obj import ReplicationPartnerObj

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationPartnerObj from a JSON string
replication_partner_obj_instance = ReplicationPartnerObj.from_json(json)
# print the JSON string representation of the object
print(ReplicationPartnerObj.to_json())

# convert the object into a dict
replication_partner_obj_dict = replication_partner_obj_instance.to_dict()
# create an instance of ReplicationPartnerObj from a dict
replication_partner_obj_from_dict = ReplicationPartnerObj.from_dict(replication_partner_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


