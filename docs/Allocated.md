# Allocated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpgs** | **float** |  | [optional] 
**cpgs_free** | **float** |  | [optional] 
**cpgs_private** | **float** |  | [optional] 
**cpgs_private_base** | [**Private**](Private.md) |  | [optional] 
**cpgs_private_snap** | [**Private**](Private.md) |  | [optional] 
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
from dscc.models.allocated import Allocated

# TODO update the JSON string below
json = "{}"
# create an instance of Allocated from a JSON string
allocated_instance = Allocated.from_json(json)
# print the JSON string representation of the object
print(Allocated.to_json())

# convert the object into a dict
allocated_dict = allocated_instance.to_dict()
# create an instance of Allocated from a dict
allocated_from_dict = Allocated.from_dict(allocated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


