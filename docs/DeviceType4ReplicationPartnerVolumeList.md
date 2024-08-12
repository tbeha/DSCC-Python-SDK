# DeviceType4ReplicationPartnerVolumeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**display_name** | **str** | Volume display name | [optional] 
**domain** | **str** | Domain that the resource belongs to. | [optional] 
**generation** | **int** | generation | [optional] 
**group_id** | **str** | Unique id of replication partner remote group. | [optional] 
**group_name** | **str** | Replication partner remote group name. | [optional] 
**group_object_id** | **int** | Replication partner group ID. | [optional] 
**id** | **str** | Unique Identifier of the volume. | [optional] 
**is_remote_array_support_replication** | **bool** | Boolean value to indicate if remote array OS version supports replication | [optional] 
**local_volume_id** | **int** | Volume ID. | [optional] 
**local_volume_name** | **str** | Volume name. | [optional] 
**remote_volume** | [**DeviceType4ReplicationPartnerVolumeListRemoteVolume**](DeviceType4ReplicationPartnerVolumeListRemoteVolume.md) |  | [optional] 
**resource_uri** | **str** | resourceUri for detailed volume object | [optional] 
**system_id** | **str** | Unique ID or serial number of the system. | [optional] 
**system_wwn** | **str** | WWN of the system. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.device_type4_replication_partner_volume_list import DeviceType4ReplicationPartnerVolumeList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ReplicationPartnerVolumeList from a JSON string
device_type4_replication_partner_volume_list_instance = DeviceType4ReplicationPartnerVolumeList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ReplicationPartnerVolumeList.to_json())

# convert the object into a dict
device_type4_replication_partner_volume_list_dict = device_type4_replication_partner_volume_list_instance.to_dict()
# create an instance of DeviceType4ReplicationPartnerVolumeList from a dict
device_type4_replication_partner_volume_list_from_dict = DeviceType4ReplicationPartnerVolumeList.from_dict(device_type4_replication_partner_volume_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


