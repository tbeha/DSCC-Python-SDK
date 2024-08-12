# DeviceType4policy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_service** | **bool** |  | [optional] 
**host_dif3par** | **bool** | host Dif 3par. This field is deprecated. | [optional] 
**host_dif_std** | **bool** | host Dif Std. This field is deprecated. | [optional] 
**no_cache** | **bool** |  | [optional] 
**one_host** | **bool** |  | [optional] 
**stale_snapshot** | **bool** |  | [optional] 
**system** | **bool** |  | [optional] 
**zero_detect** | **bool** |  | [optional] 
**zero_fill** | **bool** |  | [optional] 

## Example

```python
from dscc.models.device_type4policy import DeviceType4policy

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4policy from a JSON string
device_type4policy_instance = DeviceType4policy.from_json(json)
# print the JSON string representation of the object
print(DeviceType4policy.to_json())

# convert the object into a dict
device_type4policy_dict = device_type4policy_instance.to_dict()
# create an instance of DeviceType4policy from a dict
device_type4policy_from_dict = DeviceType4policy.from_dict(device_type4policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


