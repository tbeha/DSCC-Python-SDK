# CapacitySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free** | **int** | Total free capacity | [optional] 
**total** | **int** | Total used capacity | [optional] 

## Example

```python
from dscc.models.capacity_summary import CapacitySummary

# TODO update the JSON string below
json = "{}"
# create an instance of CapacitySummary from a JSON string
capacity_summary_instance = CapacitySummary.from_json(json)
# print the JSON string representation of the object
print(CapacitySummary.to_json())

# convert the object into a dict
capacity_summary_dict = capacity_summary_instance.to_dict()
# create an instance of CapacitySummary from a dict
capacity_summary_from_dict = CapacitySummary.from_dict(capacity_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


