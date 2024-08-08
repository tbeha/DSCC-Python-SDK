# DeviceType4ReverseParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **bool** | Changes both the role and the direction of data flow between the protected volume sets. For example, if the roles of the protected volume sets are \&quot;primary\&quot; and \&quot;secondary\&quot;, issuing the -current option to the reverse operation will result in the roles of the protected volume set becoming \&quot;secondary-rev\&quot; and \&quot;primary-rev\&quot; respectively, and the direction data flows between the groups is reversed. Since the -current option actually reverses the direction of data replication, it requires the protected volume set be stopped.This option must be used with care to ensure the protected volume sets do not end up in a non-deterministic state (like \&quot;secondary\&quot;, \&quot;secondary-rev\&quot; for example) and to ensure data loss does not occur by inadvertently changing the direction of data flow and resyncing old data on top of newer data. | [optional] 
**local_group_direction** | **bool** | This option only applies to the reverse operation, and only when the -natural or -current options to the reverse operation are specified. Specifying this option with the reverse operation and an associated -natural or -current option will only affect the system where the reverse command is issued, and will not be mirrored to any other arrays in the Remote Copy configuration. | [optional] 
**natural** | **bool** | Changes the role of the protected volume sets but not the direction of data flow between the groups on the arrays. For example, if the role of the protected volume sets are \&quot;primary\&quot; and \&quot;secondary\&quot;, issuing the -natural option with the reverse operation will result in the role of the groups becoming \&quot;primary-rev\&quot; and \&quot;secondary-rev\&quot; respectively. The direction of data flow between the protected volume sets is not affected, only the roles. Since the -natural option does not change the direction of data flow between the protected volume sets, it does not require the protected volume sets be stopped. This option must be used with care to ensure the protected volume sets do not end up in a non-deterministic state (like \&quot;secondary\&quot;, \&quot;secondary-rev\&quot; for example) and to ensure data loss does not occur by inadvertently changing the direction of data flow and resyncing old data on top of newer data. | [optional] 
**no_snapshot** | **bool** | Specifies that snapshots are not taken of the protected volume sets that are switched from secondary to primary. Additionally, existing snapshots are deleted if the protected volume sets are switched from primary to secondary. The use of this option may result in a full synchronization of the secondary volumes. | [optional] 
**skip_promote** | **bool** | Specifies that the synchronized snapshots of the protected volume set that are switched from primary to secondary should not be promoted to the base volume. The incorrect use of this option can lead to the primary and secondary volumes not being consistent. | [optional] 
**stop_groups** | **bool** | Specifies that the system stops the replication before performing the reverse action. | [optional] 
**target_name** | **str** | Replication partner name (target name) on which the reverse action to be performed. | [optional] 

## Example

```python
from dscc.models.device_type4_reverse_params import DeviceType4ReverseParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ReverseParams from a JSON string
device_type4_reverse_params_instance = DeviceType4ReverseParams.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ReverseParams.to_json())

# convert the object into a dict
device_type4_reverse_params_dict = device_type4_reverse_params_instance.to_dict()
# create an instance of DeviceType4ReverseParams from a dict
device_type4_reverse_params_from_dict = DeviceType4ReverseParams.from_dict(device_type4_reverse_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


