# CapacityByTier


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
from dscc.models.capacity_by_tier import CapacityByTier

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityByTier from a JSON string
capacity_by_tier_instance = CapacityByTier.from_json(json)
# print the JSON string representation of the object
print(CapacityByTier.to_json())

# convert the object into a dict
capacity_by_tier_dict = capacity_by_tier_instance.to_dict()
# create an instance of CapacityByTier from a dict
capacity_by_tier_from_dict = CapacityByTier.from_dict(capacity_by_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


