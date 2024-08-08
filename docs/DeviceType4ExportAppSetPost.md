# DeviceType4ExportAppSetPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_group_data_map** | [**List[DeviceType4ExportAppSetPostHostGroupDataMapInner]**](DeviceType4ExportAppSetPostHostGroupDataMapInner.md) | Host Group IDs and the corresponding attributes for each host group ID. NVMe transport type for each host Group ID is defined in this map and it is applicable if all the hosts of this host group are associated with the NVMe protocol. | [optional] 
**host_group_ids** | **List[Optional[str]]** | HostGroups | 
**proximity** | **str** | Host proximity setting for Active Peer Persistence configuration. Supported values are - PRIMARY, SECONDARY and ALL. Default proximity is PRIMARY. | [optional] 

## Example

```python
from dscc.models.device_type4_export_app_set_post import DeviceType4ExportAppSetPost

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ExportAppSetPost from a JSON string
device_type4_export_app_set_post_instance = DeviceType4ExportAppSetPost.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ExportAppSetPost.to_json())

# convert the object into a dict
device_type4_export_app_set_post_dict = device_type4_export_app_set_post_instance.to_dict()
# create an instance of DeviceType4ExportAppSetPost from a dict
device_type4_export_app_set_post_from_dict = DeviceType4ExportAppSetPost.from_dict(device_type4_export_app_set_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


