# SysLocateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locate_enabled** | **bool** | Indicates if the locate beacon should be enabled or not | [optional] 

## Example

```python
from dscc.models.sys_locate_input import SysLocateInput

# TODO update the JSON string below
json = "{}"
# create an instance of SysLocateInput from a JSON string
sys_locate_input_instance = SysLocateInput.from_json(json)
# print the JSON string representation of the object
print(SysLocateInput.to_json())

# convert the object into a dict
sys_locate_input_dict = sys_locate_input_instance.to_dict()
# create an instance of SysLocateInput from a dict
sys_locate_input_from_dict = SysLocateInput.from_dict(sys_locate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


