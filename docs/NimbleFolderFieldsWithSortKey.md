# NimbleFolderFieldsWithSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the folder. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of the folder. &#x60;Filter, Sort&#x60; | [optional] 
**pool_id** | **str** | ID of the pool where the folder resides.&#x60;Filter, Sort&#x60; | [optional] 
**pool_name** | **str** | Name of the pool where the folder resides.&#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.nimble_folder_fields_with_sort_key import NimbleFolderFieldsWithSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFolderFieldsWithSortKey from a JSON string
nimble_folder_fields_with_sort_key_instance = NimbleFolderFieldsWithSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleFolderFieldsWithSortKey.to_json())

# convert the object into a dict
nimble_folder_fields_with_sort_key_dict = nimble_folder_fields_with_sort_key_instance.to_dict()
# create an instance of NimbleFolderFieldsWithSortKey from a dict
nimble_folder_fields_with_sort_key_from_dict = NimbleFolderFieldsWithSortKey.from_dict(nimble_folder_fields_with_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


