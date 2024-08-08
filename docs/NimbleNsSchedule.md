# NimbleNsSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | A schedule is active only if it is owned by the same owner as the volume collection. Only active schedules of a volume collection participate in the creation of snapshots and replication. | [optional] 
**at_time** | **int** | Time of day when snapshot should be taken. | [optional] 
**days** | **str** | Which days snapshots should be taken. | [optional] 
**disable_appsync** | **bool** | Disables application synchronized snapshots and creates crash consistent snapshots instead. | [optional] 
**downstream_partner** | **str** | Partner name if snapshots created by this schedule should be replicated. | [optional] 
**downstream_partner_id** | **str** | Partner ID if snapshots created by this schedule should be replicated. | [optional] 
**downstream_partner_name** | **str** | Partner name if snapshots created by this schedule should be replicated. | [optional] 
**id** | **str** | ID of protection schedule. | [optional] 
**mfa_protected** | **bool** | Protected by multi-factor authentication. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**name** | **str** | Name of protection schedule. | [optional] 
**num_retain** | **int** | Number of snapshots to retain. | [optional] 
**num_retain_replica** | **int** | Number of snapshots to retain on the replica. | [optional] 
**period** | **int** | Frequency of snapshots. | [optional] 
**period_unit** | **str** | Units for repeat frequency -- minutes, hours, days or weeks. Possible values: &#39;hours&#39;, &#39;weeks&#39;, &#39;minutes&#39;, &#39;days&#39;. | [optional] 
**repl_alert_thres** | **int** | Replication alert threshold. | [optional] 
**replicate_every** | **int** | Which snapshots should be replicated. | [optional] 
**schedule_id** | **str** | ID of protection schedule. | [optional] 
**schedule_name** | **str** | Name of protection schedule. | [optional] 
**schedule_type** | **str** | regular or external_trigger. Possible values: &#39;external_trigger&#39;, &#39;regular&#39;. | [optional] 
**skip_db_consistency_check** | **bool** | Skip consistency check for database files on snapshots created by this schedule. | [optional] 
**snap_verify** | **bool** | Run verification tool on snapshot created by this schedule. | [optional] 
**until_time** | **int** | Time of day to stop taking snapshots. | [optional] 

## Example

```python
from dscc.models.nimble_ns_schedule import NimbleNsSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNsSchedule from a JSON string
nimble_ns_schedule_instance = NimbleNsSchedule.from_json(json)
# print the JSON string representation of the object
print(NimbleNsSchedule.to_json())

# convert the object into a dict
nimble_ns_schedule_dict = nimble_ns_schedule_instance.to_dict()
# create an instance of NimbleNsSchedule from a dict
nimble_ns_schedule_from_dict = NimbleNsSchedule.from_dict(nimble_ns_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


