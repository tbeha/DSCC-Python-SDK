# UnExportInput

Nimble volume  UnExport input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_groups** | [**List[UnExportInputHostGroupsInner]**](UnExportInputHostGroupsInner.md) | list of host_groups | [optional] 

## Example

```python
from dscc.models.un_export_input import UnExportInput

# TODO update the JSON string below
json = "{}"
# create an instance of UnExportInput from a JSON string
un_export_input_instance = UnExportInput.from_json(json)
# print the JSON string representation of the object
print(UnExportInput.to_json())

# convert the object into a dict
un_export_input_dict = un_export_input_instance.to_dict()
# create an instance of UnExportInput from a dict
un_export_input_from_dict = UnExportInput.from_dict(un_export_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


