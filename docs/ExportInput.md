# ExportInput

Nimble volume Export input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_to** | **str** | Type of object this access control record applies to. Possible values:&#39;volume&#39;, &#39;snapshot&#39;, &#39;both&#39;. | [optional] 
**force_apply_to** | **bool** | Forceful export of volume or snapshot as per the requested apply_to option. | [optional] 
**host_groups** | [**List[ExportInputHostGroupsInner]**](ExportInputHostGroupsInner.md) | list of host_groups | [optional] 

## Example

```python
from dscc.models.export_input import ExportInput

# TODO update the JSON string below
json = "{}"
# create an instance of ExportInput from a JSON string
export_input_instance = ExportInput.from_json(json)
# print the JSON string representation of the object
print(ExportInput.to_json())

# convert the object into a dict
export_input_dict = export_input_instance.to_dict()
# create an instance of ExportInput from a dict
export_input_from_dict = ExportInput.from_dict(export_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


