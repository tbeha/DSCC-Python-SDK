# NimbleShelfListDetails

List of Shelves that requires activation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driveset_list** | [**List[NimbleDriveSetDetails]**](NimbleDriveSetDetails.md) | List of driveset details. | 
**shelf_id** | **str** | ID of shelf. A 42 digit hexadecimal number. | 

## Example

```python
from dscc.models.nimble_shelf_list_details import NimbleShelfListDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleShelfListDetails from a JSON string
nimble_shelf_list_details_instance = NimbleShelfListDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleShelfListDetails.to_json())

# convert the object into a dict
nimble_shelf_list_details_dict = nimble_shelf_list_details_instance.to_dict()
# create an instance of NimbleShelfListDetails from a dict
nimble_shelf_list_details_from_dict = NimbleShelfListDetails.from_dict(nimble_shelf_list_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


