# NimbleChanges

Changes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**newly_created** | **bool** | Newly created information | [optional] 
**warning** | **str** |  | [optional] 

## Example

```python
from dscc.models.nimble_changes import NimbleChanges

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleChanges from a JSON string
nimble_changes_instance = NimbleChanges.from_json(json)
# print the JSON string representation of the object
print(NimbleChanges.to_json())

# convert the object into a dict
nimble_changes_dict = nimble_changes_instance.to_dict()
# create an instance of NimbleChanges from a dict
nimble_changes_from_dict = NimbleChanges.from_dict(nimble_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


