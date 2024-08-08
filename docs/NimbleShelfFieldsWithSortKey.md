# NimbleShelfFieldsWithSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | ID of array the shelf belongs to. &#x60;Filter, Sort&#x60; | [optional] 
**array_name** | **str** | Name of array the shelf belongs to. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Identifier of the shelf. &#x60;Filter&#x60; | [optional] 
**model** | **str** | Model of the shelf or head unit. &#x60;Filter, Sort&#x60; | [optional] 
**serial** | **str** | The serial number of the chassis. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.nimble_shelf_fields_with_sort_key import NimbleShelfFieldsWithSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleShelfFieldsWithSortKey from a JSON string
nimble_shelf_fields_with_sort_key_instance = NimbleShelfFieldsWithSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleShelfFieldsWithSortKey.to_json())

# convert the object into a dict
nimble_shelf_fields_with_sort_key_dict = nimble_shelf_fields_with_sort_key_instance.to_dict()
# create an instance of NimbleShelfFieldsWithSortKey from a dict
nimble_shelf_fields_with_sort_key_from_dict = NimbleShelfFieldsWithSortKey.from_dict(nimble_shelf_fields_with_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


