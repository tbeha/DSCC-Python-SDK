# DeviceType4CapacityTimeUntilFull

capacity time until full for a given systemId

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | input customer id | [optional] 
**device_type** | **str** | device type of the system | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**system_id** | **str** | input system id | [optional] 
**time_until_full** | **int** | epoch timestamp in millisecond denoting the estimated tuf of the system | [optional] 

## Example

```python
from dscc.models.device_type4_capacity_time_until_full import DeviceType4CapacityTimeUntilFull

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CapacityTimeUntilFull from a JSON string
device_type4_capacity_time_until_full_instance = DeviceType4CapacityTimeUntilFull.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CapacityTimeUntilFull.to_json())

# convert the object into a dict
device_type4_capacity_time_until_full_dict = device_type4_capacity_time_until_full_instance.to_dict()
# create an instance of DeviceType4CapacityTimeUntilFull from a dict
device_type4_capacity_time_until_full_from_dict = DeviceType4CapacityTimeUntilFull.from_dict(device_type4_capacity_time_until_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


