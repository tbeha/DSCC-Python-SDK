# DeviceType4hostProximityDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_remote_array_support_replication** | **bool** | Boolean value to indicate if remote array OS version supports replication | [optional] 
**is_source_array_support_replication** | **bool** | Boolean value to indicate if source array OS version supports replication | [optional] 
**local_system** | **str** | Local system where host I/O path is Active optimized | [optional] 
**proximity_value** | **str** | Host proximity to determine the Asymmetric Logical path access state | [optional] 
**remote_system** | **str** | Remote system where host I/O path is Active Non-optimized | [optional] 

## Example

```python
from dscc.models.device_type4host_proximity_detail import DeviceType4hostProximityDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4hostProximityDetail from a JSON string
device_type4host_proximity_detail_instance = DeviceType4hostProximityDetail.from_json(json)
# print the JSON string representation of the object
print(DeviceType4hostProximityDetail.to_json())

# convert the object into a dict
device_type4host_proximity_detail_dict = device_type4host_proximity_detail_instance.to_dict()
# create an instance of DeviceType4hostProximityDetail from a dict
device_type4host_proximity_detail_from_dict = DeviceType4hostProximityDetail.from_dict(device_type4host_proximity_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


