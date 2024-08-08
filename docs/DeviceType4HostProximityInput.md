# DeviceType4HostProximityInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | Name of the host of which proximity setting is getting changed. | 
**proximity** | **str** | Host proximity setting for Active Peer Persistence configuration. Supported values are - PRIMARY, SECONDARY and ALL | 

## Example

```python
from dscc.models.device_type4_host_proximity_input import DeviceType4HostProximityInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostProximityInput from a JSON string
device_type4_host_proximity_input_instance = DeviceType4HostProximityInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostProximityInput.to_json())

# convert the object into a dict
device_type4_host_proximity_input_dict = device_type4_host_proximity_input_instance.to_dict()
# create an instance of DeviceType4HostProximityInput from a dict
device_type4_host_proximity_input_from_dict = DeviceType4HostProximityInput.from_dict(device_type4_host_proximity_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


