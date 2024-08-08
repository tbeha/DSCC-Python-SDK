# ExportInputHostGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_group_id** | **str** | host group id. | [optional] 
**lun** | **int** | Lun number | [optional] 

## Example

```python
from dscc.models.export_input_host_groups_inner import ExportInputHostGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExportInputHostGroupsInner from a JSON string
export_input_host_groups_inner_instance = ExportInputHostGroupsInner.from_json(json)
# print the JSON string representation of the object
print(ExportInputHostGroupsInner.to_json())

# convert the object into a dict
export_input_host_groups_inner_dict = export_input_host_groups_inner_instance.to_dict()
# create an instance of ExportInputHostGroupsInner from a dict
export_input_host_groups_inner_from_dict = ExportInputHostGroupsInner.from_dict(export_input_host_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


