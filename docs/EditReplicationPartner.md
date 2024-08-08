# EditReplicationPartner

The request body for replication partner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_port** | **int** | Port number of partner control interface. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**data_port** | **int** | Port number of partner data interface. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**description** | **str** | Description of replication partner. String of up to 255 printable ASCII characters. | [optional] 
**remote_partner_id** | **str** | Remote replication partner ID | [optional] 
**repl_hostname** | **str** | IP address or hostname of partner data interface. String of up to 64 alphanumeric characters, - and . and colon are allowed after first character. | [optional] 
**source** | [**EditSourcePartner**](EditSourcePartner.md) |  | [optional] 
**subnet_label** | **str** | Label of the subnet used to replicate to this partner. String of up to 64 alphanumeric characters, - and . and colon are allowed after first character. | [optional] 
**subnet_type** | **str** | Type of the subnet used to replicate to this partner. Possible values are &#39;invalid&#39;, &#39;unconfigured&#39;, &#39;mgmt&#39;, &#39;data&#39;, &#39;mgmt_data&#39;. | [optional] 
**target** | [**EditTargetPartner**](EditTargetPartner.md) |  | [optional] 
**target_system_id** | **str** | Target system ID | [optional] 
**throttles** | [**List[ReplicationThrottle]**](ReplicationThrottle.md) | Throttles used while replicating from/to this partner. All the throttles for the partner. | [optional] 

## Example

```python
from dscc.models.edit_replication_partner import EditReplicationPartner

# TODO update the JSON string below
json = "{}"
# create an instance of EditReplicationPartner from a JSON string
edit_replication_partner_instance = EditReplicationPartner.from_json(json)
# print the JSON string representation of the object
print(EditReplicationPartner.to_json())

# convert the object into a dict
edit_replication_partner_dict = edit_replication_partner_instance.to_dict()
# create an instance of EditReplicationPartner from a dict
edit_replication_partner_from_dict = EditReplicationPartner.from_dict(edit_replication_partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


