# BulkMergeOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BulkMergeOutputObject]**](BulkMergeOutputObject.md) |  | [optional] 

## Example

```python
from dscc.models.bulk_merge_output import BulkMergeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of BulkMergeOutput from a JSON string
bulk_merge_output_instance = BulkMergeOutput.from_json(json)
# print the JSON string representation of the object
print(BulkMergeOutput.to_json())

# convert the object into a dict
bulk_merge_output_dict = bulk_merge_output_instance.to_dict()
# create an instance of BulkMergeOutput from a dict
bulk_merge_output_from_dict = BulkMergeOutput.from_dict(bulk_merge_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


