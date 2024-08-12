# NwCimEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cim** | [**NwCimEditCim**](NwCimEditCim.md) |  | [optional] 

## Example

```python
from dscc.models.nw_cim_edit import NwCimEdit

# TODO update the JSON string below
json = "{}"
# create an instance of NwCimEdit from a JSON string
nw_cim_edit_instance = NwCimEdit.from_json(json)
# print the JSON string representation of the object
print(NwCimEdit.to_json())

# convert the object into a dict
nw_cim_edit_dict = nw_cim_edit_instance.to_dict()
# create an instance of NwCimEdit from a dict
nw_cim_edit_from_dict = NwCimEdit.from_dict(nw_cim_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


