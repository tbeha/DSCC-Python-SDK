# NimbleFolderSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqn** | **str** | Fully qualified name of folder. | [optional] 
**id** | **str** | Identifier of folder. A 42 digit hexadecimal number. | [optional] 

## Example

```python
from dscc.models.nimble_folder_summary import NimbleFolderSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFolderSummary from a JSON string
nimble_folder_summary_instance = NimbleFolderSummary.from_json(json)
# print the JSON string representation of the object
print(NimbleFolderSummary.to_json())

# convert the object into a dict
nimble_folder_summary_dict = nimble_folder_summary_instance.to_dict()
# create an instance of NimbleFolderSummary from a dict
nimble_folder_summary_from_dict = NimbleFolderSummary.from_dict(nimble_folder_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


