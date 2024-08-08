# DeviceType4SecondaryRemoteInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | TenantId of resource | [optional] 
**is_remote_array_support_replication** | **bool** | Boolean value to indicate if remote array OS version supports replication | [optional] 
**over_period_alert** | **bool** | This field is valid only for 3DC remote replication. If synchronization of an asynchronous periodic Remote Copy group takes longer to complete than its synchronization period, an alert is generated. This property is not valid in case of synchronous policy and will always be false in that case. | [optional] 
**partner_id** | **str** | Id of replication partner | [optional] 
**partner_name** | **str** | Name of replication partner | [optional] 
**replication_partner_user_cpg** | **str** | User CPG in which the target volumes would get created in the replication partner system. | [optional] 
**replication_type** | **str** | Mode of replication. Can be periodic only | [optional] 
**resource_uri** | **str** | resource Uri of replication partner object | [optional] 

## Example

```python
from dscc.models.device_type4_secondary_remote_info import DeviceType4SecondaryRemoteInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SecondaryRemoteInfo from a JSON string
device_type4_secondary_remote_info_instance = DeviceType4SecondaryRemoteInfo.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SecondaryRemoteInfo.to_json())

# convert the object into a dict
device_type4_secondary_remote_info_dict = device_type4_secondary_remote_info_instance.to_dict()
# create an instance of DeviceType4SecondaryRemoteInfo from a dict
device_type4_secondary_remote_info_from_dict = DeviceType4SecondaryRemoteInfo.from_dict(device_type4_secondary_remote_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


