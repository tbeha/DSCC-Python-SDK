# LocateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locate** | **bool** | Indicates if the locate beacon should be enabled or not | [optional] 

## Example

```python
from dscc.models.locate_input import LocateInput

# TODO update the JSON string below
json = "{}"
# create an instance of LocateInput from a JSON string
locate_input_instance = LocateInput.from_json(json)
# print the JSON string representation of the object
print(LocateInput.to_json())

# convert the object into a dict
locate_input_dict = locate_input_instance.to_dict()
# create an instance of LocateInput from a dict
locate_input_from_dict = LocateInput.from_dict(locate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


