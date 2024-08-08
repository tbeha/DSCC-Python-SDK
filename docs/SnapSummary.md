# SnapSummary

Last snapshot for this volume. Select fields containing snapshot information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_creation_time** | **int** | Creation time of snapshot. | [optional] 
**snap_id** | **str** | ID of snapshot. | [optional] 
**snap_name** | **str** | Name of snapshot. | [optional] 

## Example

```python
from dscc.models.snap_summary import SnapSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SnapSummary from a JSON string
snap_summary_instance = SnapSummary.from_json(json)
# print the JSON string representation of the object
print(SnapSummary.to_json())

# convert the object into a dict
snap_summary_dict = snap_summary_instance.to_dict()
# create an instance of SnapSummary from a dict
snap_summary_from_dict = SnapSummary.from_dict(snap_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


