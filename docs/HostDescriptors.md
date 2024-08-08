# HostDescriptors

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
from dscc.models.host_descriptors import HostDescriptors

# TODO update the JSON string below
json = "{}"
# create an instance of HostDescriptors from a JSON string
host_descriptors_instance = HostDescriptors.from_json(json)
# print the JSON string representation of the object
print(HostDescriptors.to_json())

# convert the object into a dict
host_descriptors_dict = host_descriptors_instance.to_dict()
# create an instance of HostDescriptors from a dict
host_descriptors_from_dict = HostDescriptors.from_dict(host_descriptors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


