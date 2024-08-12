# NimbleControllerFieldsWithSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | Rest ID of the array containing this controller. &#x60;Filter, Sort&#x60; | [optional] 
**array_name** | **str** | Name of the array containing this controller. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Identifier of the controller. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of the controller. &#x60;Filter, Sort&#x60; | [optional] 
**serial** | **str** | Serial number for this controller. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.nimble_controller_fields_with_sort_key import NimbleControllerFieldsWithSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleControllerFieldsWithSortKey from a JSON string
nimble_controller_fields_with_sort_key_instance = NimbleControllerFieldsWithSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleControllerFieldsWithSortKey.to_json())

# convert the object into a dict
nimble_controller_fields_with_sort_key_dict = nimble_controller_fields_with_sort_key_instance.to_dict()
# create an instance of NimbleControllerFieldsWithSortKey from a dict
nimble_controller_fields_with_sort_key_from_dict = NimbleControllerFieldsWithSortKey.from_dict(nimble_controller_fields_with_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


