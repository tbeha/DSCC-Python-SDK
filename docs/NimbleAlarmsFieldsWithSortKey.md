# NimbleAlarmsFieldsWithSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ack_time** | **int** | Time when this alarm was acknowledged. Seconds since last epoch i.e. 00:00 January 1, 1970. &#x60;Filter, Sort&#x60; | [optional] 
**activity** | **str** | Description of activity performed and recorded in alarm. String of 1-1476 printable characters. &#x60;Filter, Sort&#x60; | [optional] 
**array** | **str** | The array name where the alarm is generated.  Possible values: array serial number, or &#39;-&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**category** | **str** | Category of the alarm. Possible values: &#39;unknown&#39;, &#39;hardware&#39;, &#39;service&#39;, &#39;replication&#39;, &#39;volume&#39;, &#39;update&#39;, &#39;configuration&#39;, &#39;test&#39;, &#39;security&#39;, &#39;array_upgrade&#39;,cloud_console &#x60;Filter, Sort&#x60; | [optional] 
**curr_onset_event_id** | **str** | Identifier for the current onset event. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Identifier for the alarm record. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**next_notification_time** | **int** | Time when next reminder for the alarm will be sent. Signed 64-bit integer. &#x60;Filter, Sort&#x60; | [optional] 
**object_id** | **str** | Identifier of object operated upon. A 42 digit hexadecimal number.  &#x60;Filter, Sort&#x60; | [optional] 
**object_name** | **str** | Name of object operated upon. String of up to 400 alphanumeric characters, - and . and : and \&quot; \&quot; are allowed after first character.  &#x60;Filter, Sort&#x60; | [optional] 
**object_type** | **str** | Type of the object being operated upon. Possible values: &#39;active_directory&#39;, &#39;group&#39;, &#39;chapuser&#39;, &#39;initiatorgrp&#39;, &#39;perfpolicy&#39;, &#39;snapshot&#39;, &#39;snapcoll&#39;, &#39;vol&#39;, &#39;volcoll&#39;, &#39;partner&#39;, &#39;array&#39;, &#39;pool&#39;, &#39;initiator&#39;, &#39;protsched&#39;, &#39;volacl&#39;, &#39;throttle&#39;, &#39;sshkey&#39;, &#39;user&#39;, &#39;protpol&#39;, &#39;prottmpl&#39;, &#39;branch&#39;, &#39;route&#39;, &#39;role&#39;, &#39;privilege&#39;, &#39;netconfig&#39;, &#39;events&#39;, &#39;session&#39;, &#39;subnet&#39;, &#39;array_netconfig&#39;, &#39;nic&#39;, &#39;initiatorgrp_subnet&#39;, &#39;fc_initiator_alias&#39;, &#39;fc_port&#39;, &#39;fc_interface_collection&#39;, &#39;fc&#39;, &#39;event_dipatcher&#39;, &#39;fc_target_port_group&#39;, &#39;encrypt_key&#39;, &#39;encrypt_config&#39;, &#39;snapshot_lun&#39;, &#39;syslog&#39;, &#39;async_job&#39;, &#39;application_server&#39;, &#39;audit_log&#39;, &#39;ip address&#39;, &#39;disk&#39;, &#39;shelf&#39;, &#39;protocol_endpoint&#39;, &#39;folder&#39;, &#39;pe_acl&#39;, &#39;vvol&#39;, &#39;vvol_acl&#39;, &#39;alarm&#39; ,&#39;folset&#39;,&#39;hc_cluster_config&#39;,&#39;user group&#39;, &#39;user_policy&#39;, &#39;witness&#39;, &#39;support&#39;, &#39;keymanager&#39;, &#39;trusted_oauth_issuer&#39;, &#39;client_credential&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**onset_time** | **int** | Time when this alarm was triggered. Seconds since last epoch i.e. 00:00 January 1, 1970. &#x60;Filter, Sort&#x60; | [optional] 
**remind_every** | **int** | Frequency of notification. This number and the remind_every_unit define how frequent one alarm notification is sent. &#x60;Filter, Sort&#x60; | [optional] 
**remind_every_unit** | **str** | Time unit over which to send the number of notification specified in &#39;remind_every&#39;. For example, a value of &#39;days&#39; with a &#39;remind_every&#39; of &#39;1&#39; results in one notification every day. Possible values: &#39;minutes&#39;, &#39;hours&#39;, &#39;days&#39;, &#39;weeks&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**severity** | **str** | Severity level of the event. Possible values: &#39;warning&#39;, &#39;critical&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**status** | **str** | Status of the operation -- open or acknowledged. Possible values: &#39;open&#39;, &#39;acknowledged&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**user_full_name** | **str** | Full name of the user who acknowledged the alarm. Alphanumeric string of up to 64 chars, starts with letter, can include space, apostrophe(&#39;), hyphen(-). &#x60;Filter, Sort&#x60; | [optional] 
**user_id** | **str** | Identifier of the user who acknowledged the alarm. A 42 digit hexadecimal number.  &#x60;Filter, Sort&#x60; | [optional] 
**user_name** | **str** | Username of the user who acknowledged the alarm. String of up to 80 alphanumeric characters, beginning with a letter. For Active Directory users, it can include backslash (\\), dash (-), period (.), underscore (_) and space.  &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.nimble_alarms_fields_with_sort_key import NimbleAlarmsFieldsWithSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleAlarmsFieldsWithSortKey from a JSON string
nimble_alarms_fields_with_sort_key_instance = NimbleAlarmsFieldsWithSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleAlarmsFieldsWithSortKey.to_json())

# convert the object into a dict
nimble_alarms_fields_with_sort_key_dict = nimble_alarms_fields_with_sort_key_instance.to_dict()
# create an instance of NimbleAlarmsFieldsWithSortKey from a dict
nimble_alarms_fields_with_sort_key_from_dict = NimbleAlarmsFieldsWithSortKey.from_dict(nimble_alarms_fields_with_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


