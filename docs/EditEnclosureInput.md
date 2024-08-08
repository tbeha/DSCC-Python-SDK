# EditEnclosureInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | New Id of the enclosure | [optional] 
**location** | **str** | Location of the enclosure in the datacenter | [optional] 

## Example

```python
from dscc.models.edit_enclosure_input import EditEnclosureInput

# TODO update the JSON string below
json = "{}"
# create an instance of EditEnclosureInput from a JSON string
edit_enclosure_input_instance = EditEnclosureInput.from_json(json)
# print the JSON string representation of the object
print(EditEnclosureInput.to_json())

# convert the object into a dict
edit_enclosure_input_dict = edit_enclosure_input_instance.to_dict()
# create an instance of EditEnclosureInput from a dict
edit_enclosure_input_from_dict = EditEnclosureInput.from_dict(edit_enclosure_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


