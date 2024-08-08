# Space


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free_mi_b** | **float** |  | [optional] 
**grown_mi_b** | **float** |  | [optional] 
**raw_reserved_mi_b** | **float** |  | [optional] 
**reclaimed_mi_b** | **float** |  | [optional] 
**reserved_mi_b** | **float** |  | [optional] 
**total_mi_b** | **float** |  | [optional] 
**used_mi_b** | **float** |  | [optional] 

## Example

```python
from dscc.models.space import Space

# TODO update the JSON string below
json = "{}"
# create an instance of Space from a JSON string
space_instance = Space.from_json(json)
# print the JSON string representation of the object
print(Space.to_json())

# convert the object into a dict
space_dict = space_instance.to_dict()
# create an instance of Space from a dict
space_from_dict = Space.from_dict(space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


