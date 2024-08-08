# DeviceType4HostStateDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **List[Optional[str]]** | system ntp addresses | [optional] 
**default** | **str** | Default Name | [optional] 
**key** | **str** | Key of the Host Name | [optional] 
**localized_text** | **str** | Localized Text  | [optional] 

## Example

```python
from dscc.models.device_type4_host_state_detailed import DeviceType4HostStateDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostStateDetailed from a JSON string
device_type4_host_state_detailed_instance = DeviceType4HostStateDetailed.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostStateDetailed.to_json())

# convert the object into a dict
device_type4_host_state_detailed_dict = device_type4_host_state_detailed_instance.to_dict()
# create an instance of DeviceType4HostStateDetailed from a dict
device_type4_host_state_detailed_from_dict = DeviceType4HostStateDetailed.from_dict(device_type4_host_state_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


