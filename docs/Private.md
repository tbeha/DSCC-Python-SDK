# Private


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reserved** | **float** |  | [optional] 
**reserved_v_vols** | **float** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from dscc.models.private import Private

# TODO update the JSON string below
json = "{}"
# create an instance of Private from a JSON string
private_instance = Private.from_json(json)
# print the JSON string representation of the object
print(Private.to_json())

# convert the object into a dict
private_dict = private_instance.to_dict()
# create an instance of Private from a dict
private_from_dict = Private.from_dict(private_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


