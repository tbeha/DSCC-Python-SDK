# Allocation

Device allocation settings such as RAID and device type information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ha** | [**DeviceType4allocationHA**](DeviceType4allocationHA.md) |  | [optional] 
**raid_type** | **str** | RAID type | [optional] 
**chunklet_pos_pref** | **str** | Chunklets position | [optional] 
**device_speed** | [**DeviceType4allocationDeviceSpeed**](DeviceType4allocationDeviceSpeed.md) |  | [optional] 
**device_type** | **str** | Device type | [optional] 
**disk_filter** | **str** | Disk filter | [optional] 
**requested_ha** | [**DeviceType4allocationHA**](DeviceType4allocationHA.md) |  | [optional] 
**set_size** | **str** | Set size | [optional] 
**step_size** | **float** | Step size | [optional] 

## Example

```python
from dscc.models.allocation import Allocation

# TODO update the JSON string below
json = "{}"
# create an instance of Allocation from a JSON string
allocation_instance = Allocation.from_json(json)
# print the JSON string representation of the object
print(Allocation.to_json())

# convert the object into a dict
allocation_dict = allocation_instance.to_dict()
# create an instance of Allocation from a dict
allocation_from_dict = Allocation.from_dict(allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


