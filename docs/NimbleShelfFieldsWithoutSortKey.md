# NimbleShelfFieldsWithoutSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | ID of array the shelf belongs to. | [optional] 
**array_name** | **str** | Name of array the shelf belongs to. | [optional] 
**id** | **str** | Identifier of the shelf. | [optional] 
**model** | **str** | Model of the shelf or head unit. | [optional] 
**serial** | **str** | The serial number of the chassis. | [optional] 

## Example

```python
from dscc.models.nimble_shelf_fields_without_sort_key import NimbleShelfFieldsWithoutSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleShelfFieldsWithoutSortKey from a JSON string
nimble_shelf_fields_without_sort_key_instance = NimbleShelfFieldsWithoutSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleShelfFieldsWithoutSortKey.to_json())

# convert the object into a dict
nimble_shelf_fields_without_sort_key_dict = nimble_shelf_fields_without_sort_key_instance.to_dict()
# create an instance of NimbleShelfFieldsWithoutSortKey from a dict
nimble_shelf_fields_without_sort_key_from_dict = NimbleShelfFieldsWithoutSortKey.from_dict(nimble_shelf_fields_without_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


