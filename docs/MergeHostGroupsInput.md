# MergeHostGroupsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_group_ids** | **List[str]** | Array of host group ids          | 
**name** | **str** | Name of the host Group. | 

## Example

```python
from dscc.models.merge_host_groups_input import MergeHostGroupsInput

# TODO update the JSON string below
json = "{}"
# create an instance of MergeHostGroupsInput from a JSON string
merge_host_groups_input_instance = MergeHostGroupsInput.from_json(json)
# print the JSON string representation of the object
print(MergeHostGroupsInput.to_json())

# convert the object into a dict
merge_host_groups_input_dict = merge_host_groups_input_instance.to_dict()
# create an instance of MergeHostGroupsInput from a dict
merge_host_groups_input_from_dict = MergeHostGroupsInput.from_dict(merge_host_groups_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


