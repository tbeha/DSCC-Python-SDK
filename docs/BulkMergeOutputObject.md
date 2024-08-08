# BulkMergeOutputObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duplicate_ids** | **List[str]** | host/hostgroup ids of all merged duplicates | [optional] 
**id** | **str** | Id of the created host/hostgroup | [optional] 

## Example

```python
from dscc.models.bulk_merge_output_object import BulkMergeOutputObject

# TODO update the JSON string below
json = "{}"
# create an instance of BulkMergeOutputObject from a JSON string
bulk_merge_output_object_instance = BulkMergeOutputObject.from_json(json)
# print the JSON string representation of the object
print(BulkMergeOutputObject.to_json())

# convert the object into a dict
bulk_merge_output_object_dict = bulk_merge_output_object_instance.to_dict()
# create an instance of BulkMergeOutputObject from a dict
bulk_merge_output_object_from_dict = BulkMergeOutputObject.from_dict(bulk_merge_output_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


