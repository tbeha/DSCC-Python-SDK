# DeviceType4HostDescriptors

Host Descriptors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_addr** | **str** | Ip Address | [optional] 
**comment** | **str** | Comment | [optional] 
**contact** | **str** | Contact | [optional] 
**location** | **str** | Location | [optional] 
**model** | **str** | Model | [optional] 
**os** | **str** | Operating System Name | [optional] 

## Example

```python
from dscc.models.device_type4_host_descriptors import DeviceType4HostDescriptors

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostDescriptors from a JSON string
device_type4_host_descriptors_instance = DeviceType4HostDescriptors.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostDescriptors.to_json())

# convert the object into a dict
device_type4_host_descriptors_dict = device_type4_host_descriptors_instance.to_dict()
# create an instance of DeviceType4HostDescriptors from a dict
device_type4_host_descriptors_from_dict = DeviceType4HostDescriptors.from_dict(device_type4_host_descriptors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


