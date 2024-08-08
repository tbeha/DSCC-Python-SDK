# SystemDetailedCapacity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_space** | **float** | Total snap capacity | [optional] 
**volume_space** | **float** | Total volume capacity | [optional] 

## Example

```python
from dscc.models.system_detailed_capacity import SystemDetailedCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of SystemDetailedCapacity from a JSON string
system_detailed_capacity_instance = SystemDetailedCapacity.from_json(json)
# print the JSON string representation of the object
print(SystemDetailedCapacity.to_json())

# convert the object into a dict
system_detailed_capacity_dict = system_detailed_capacity_instance.to_dict()
# create an instance of SystemDetailedCapacity from a dict
system_detailed_capacity_from_dict = SystemDetailedCapacity.from_dict(system_detailed_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


