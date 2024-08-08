# StorageTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceTypes]**](DeviceTypes.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of type of systems | [optional] 

## Example

```python
from dscc.models.storage_types import StorageTypes

# TODO update the JSON string below
json = "{}"
# create an instance of StorageTypes from a JSON string
storage_types_instance = StorageTypes.from_json(json)
# print the JSON string representation of the object
print(StorageTypes.to_json())

# convert the object into a dict
storage_types_dict = storage_types_instance.to_dict()
# create an instance of StorageTypes from a dict
storage_types_from_dict = StorageTypes.from_dict(storage_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


