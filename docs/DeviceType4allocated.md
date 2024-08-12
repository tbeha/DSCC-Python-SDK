# DeviceType4allocated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpgs** | **float** |  | [optional] 
**cpgs_free** | **float** |  | [optional] 
**cpgs_private** | **float** |  | [optional] 
**cpgs_private_base** | [**DeviceType4private**](DeviceType4private.md) |  | [optional] 
**cpgs_private_snap** | [**DeviceType4allocatedCpgsPrivateSnap**](DeviceType4allocatedCpgsPrivateSnap.md) |  | [optional] 
**cpgs_shared** | **float** |  | [optional] 
**legacy_volumes** | **float** |  | [optional] 
**legacy_volumes_snap** | **float** |  | [optional] 
**legacy_volumes_user** | **float** |  | [optional] 
**system** | **float** |  | [optional] 
**system_admin** | **float** |  | [optional] 
**system_internal** | **float** |  | [optional] 
**system_spare** | **float** |  | [optional] 
**system_spare_unused** | **float** |  | [optional] 
**system_spare_used** | **float** |  | [optional] 
**total** | **float** | Total allocated percentage | [optional] 
**unmapped** | **float** |  | [optional] 

## Example

```python
from dscc.models.device_type4allocated import DeviceType4allocated

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4allocated from a JSON string
device_type4allocated_instance = DeviceType4allocated.from_json(json)
# print the JSON string representation of the object
print(DeviceType4allocated.to_json())

# convert the object into a dict
device_type4allocated_dict = device_type4allocated_instance.to_dict()
# create an instance of DeviceType4allocated from a dict
device_type4allocated_from_dict = DeviceType4allocated.from_dict(device_type4allocated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


