# NimbleFolderFieldsWithoutSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the folder. | [optional] 
**name** | **str** | Name of the folder. | [optional] 
**pool_id** | **str** | ID of the pool where the folder resides. | [optional] 
**pool_name** | **str** | Name of the pool where the folder resides. | [optional] 

## Example

```python
from dscc.models.nimble_folder_fields_without_sort_key import NimbleFolderFieldsWithoutSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFolderFieldsWithoutSortKey from a JSON string
nimble_folder_fields_without_sort_key_instance = NimbleFolderFieldsWithoutSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleFolderFieldsWithoutSortKey.to_json())

# convert the object into a dict
nimble_folder_fields_without_sort_key_dict = nimble_folder_fields_without_sort_key_instance.to_dict()
# create an instance of NimbleFolderFieldsWithoutSortKey from a dict
nimble_folder_fields_without_sort_key_from_dict = NimbleFolderFieldsWithoutSortKey.from_dict(nimble_folder_fields_without_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


