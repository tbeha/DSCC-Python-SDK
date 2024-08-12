# DeviceType4RecoveryPoint

Shows last data sync time

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch time in milliseconds | [optional] 
**tz** | **str** | Time zone name | [optional] 

## Example

```python
from dscc.models.device_type4_recovery_point import DeviceType4RecoveryPoint

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RecoveryPoint from a JSON string
device_type4_recovery_point_instance = DeviceType4RecoveryPoint.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RecoveryPoint.to_json())

# convert the object into a dict
device_type4_recovery_point_dict = device_type4_recovery_point_instance.to_dict()
# create an instance of DeviceType4RecoveryPoint from a dict
device_type4_recovery_point_from_dict = DeviceType4RecoveryPoint.from_dict(device_type4_recovery_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


