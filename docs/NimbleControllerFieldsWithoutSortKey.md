# NimbleControllerFieldsWithoutSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | Rest ID of the array containing this controller. | [optional] 
**array_name** | **str** | Name of the array containing this controller. | [optional] 
**id** | **str** | Identifier of the controller. | [optional] 
**name** | **str** | Name of the controller. | [optional] 
**serial** | **str** | Serial number for this controller. | [optional] 

## Example

```python
from dscc.models.nimble_controller_fields_without_sort_key import NimbleControllerFieldsWithoutSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleControllerFieldsWithoutSortKey from a JSON string
nimble_controller_fields_without_sort_key_instance = NimbleControllerFieldsWithoutSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleControllerFieldsWithoutSortKey.to_json())

# convert the object into a dict
nimble_controller_fields_without_sort_key_dict = nimble_controller_fields_without_sort_key_instance.to_dict()
# create an instance of NimbleControllerFieldsWithoutSortKey from a dict
nimble_controller_fields_without_sort_key_from_dict = NimbleControllerFieldsWithoutSortKey.from_dict(nimble_controller_fields_without_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


