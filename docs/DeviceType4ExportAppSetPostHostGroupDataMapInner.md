# DeviceType4ExportAppSetPostHostGroupDataMapInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_group_id** | **str** | Host group Id | [optional] 
**nvme_transport_type** | **str** | Transport type of the protocol. Configuration of the transport type is only supported for NVMe protocol starting from the system OS version 10.3.0 and the default transport type value is FC. | [optional] 

## Example

```python
from dscc.models.device_type4_export_app_set_post_host_group_data_map_inner import DeviceType4ExportAppSetPostHostGroupDataMapInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ExportAppSetPostHostGroupDataMapInner from a JSON string
device_type4_export_app_set_post_host_group_data_map_inner_instance = DeviceType4ExportAppSetPostHostGroupDataMapInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ExportAppSetPostHostGroupDataMapInner.to_json())

# convert the object into a dict
device_type4_export_app_set_post_host_group_data_map_inner_dict = device_type4_export_app_set_post_host_group_data_map_inner_instance.to_dict()
# create an instance of DeviceType4ExportAppSetPostHostGroupDataMapInner from a dict
device_type4_export_app_set_post_host_group_data_map_inner_from_dict = DeviceType4ExportAppSetPostHostGroupDataMapInner.from_dict(device_type4_export_app_set_post_host_group_data_map_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


