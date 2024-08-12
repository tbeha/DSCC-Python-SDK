# NimbleShelvesActivateInput

Request body for  shelves activation workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shelf_list** | [**List[NimbleShelfListDetails]**](NimbleShelfListDetails.md) | List of shelves details. | 

## Example

```python
from dscc.models.nimble_shelves_activate_input import NimbleShelvesActivateInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleShelvesActivateInput from a JSON string
nimble_shelves_activate_input_instance = NimbleShelvesActivateInput.from_json(json)
# print the JSON string representation of the object
print(NimbleShelvesActivateInput.to_json())

# convert the object into a dict
nimble_shelves_activate_input_dict = nimble_shelves_activate_input_instance.to_dict()
# create an instance of NimbleShelvesActivateInput from a dict
nimble_shelves_activate_input_from_dict = NimbleShelvesActivateInput.from_dict(nimble_shelves_activate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


