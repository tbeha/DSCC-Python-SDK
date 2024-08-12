# DeviceType4capacityByTier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fc_free** | **float** | fc free capacity | [optional] 
**fc_used** | **float** | fc used capacity | [optional] 
**nl_free** | **float** | nl free capacity | [optional] 
**nl_used** | **float** | nl used capacity | [optional] 
**ssd_free** | **float** | ssd free capacity | [optional] 
**ssd_used** | **float** | ssd used capacity | [optional] 
**total_used** | **float** | usable capacity | [optional] 
**usable_capacity** | **float** | usable capacity | [optional] 

## Example

```python
from dscc.models.device_type4capacity_by_tier import DeviceType4capacityByTier

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4capacityByTier from a JSON string
device_type4capacity_by_tier_instance = DeviceType4capacityByTier.from_json(json)
# print the JSON string representation of the object
print(DeviceType4capacityByTier.to_json())

# convert the object into a dict
device_type4capacity_by_tier_dict = device_type4capacity_by_tier_instance.to_dict()
# create an instance of DeviceType4capacityByTier from a dict
device_type4capacity_by_tier_from_dict = DeviceType4capacityByTier.from_dict(device_type4capacity_by_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


