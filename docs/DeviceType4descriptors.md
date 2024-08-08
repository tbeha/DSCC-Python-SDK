# DeviceType4descriptors

System descriptors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | CommeUser-specified comment for the system | [optional] 
**contact** | **str** | User-specified contact for the system | [optional] 
**location** | **str** | User-specified location of the system | [optional] 
**owner** | **str** | User-specified owner for the system | [optional] 

## Example

```python
from dscc.models.device_type4descriptors import DeviceType4descriptors

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4descriptors from a JSON string
device_type4descriptors_instance = DeviceType4descriptors.from_json(json)
# print the JSON string representation of the object
print(DeviceType4descriptors.to_json())

# convert the object into a dict
device_type4descriptors_dict = device_type4descriptors_instance.to_dict()
# create an instance of DeviceType4descriptors from a dict
device_type4descriptors_from_dict = DeviceType4descriptors.from_dict(device_type4descriptors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


