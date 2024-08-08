# NimbleSnapcollSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapcoll_creation_time** | **str** | Creation time of snapshot collection. | [optional] 
**snapcoll_id** | **str** | ID of snapshot collection. | [optional] 
**snapcoll_name** | **str** | Name of snapshot collection. | [optional] 

## Example

```python
from dscc.models.nimble_snapcoll_summary import NimbleSnapcollSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleSnapcollSummary from a JSON string
nimble_snapcoll_summary_instance = NimbleSnapcollSummary.from_json(json)
# print the JSON string representation of the object
print(NimbleSnapcollSummary.to_json())

# convert the object into a dict
nimble_snapcoll_summary_dict = nimble_snapcoll_summary_instance.to_dict()
# create an instance of NimbleSnapcollSummary from a dict
nimble_snapcoll_summary_from_dict = NimbleSnapcollSummary.from_dict(nimble_snapcoll_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


