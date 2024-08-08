# DeviceType4maintenanceModeInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comments | [optional] 
**end_time** | [**DeviceType4maintenanceModeInnerEndTime**](DeviceType4maintenanceModeInnerEndTime.md) |  | [optional] 
**instances** | **int** | Instances | [optional] 
**reason_code** | **str** | Reason code | [optional] 
**start_time** | [**DeviceType4maintenanceModeInnerStartTime**](DeviceType4maintenanceModeInnerStartTime.md) |  | [optional] 
**user** | **str** | User | [optional] 

## Example

```python
from dscc.models.device_type4maintenance_mode_inner import DeviceType4maintenanceModeInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4maintenanceModeInner from a JSON string
device_type4maintenance_mode_inner_instance = DeviceType4maintenanceModeInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4maintenanceModeInner.to_json())

# convert the object into a dict
device_type4maintenance_mode_inner_dict = device_type4maintenance_mode_inner_instance.to_dict()
# create an instance of DeviceType4maintenanceModeInner from a dict
device_type4maintenance_mode_inner_from_dict = DeviceType4maintenanceModeInner.from_dict(device_type4maintenance_mode_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


