# NimblePerfPolicySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the performance policy. | [optional] 

## Example

```python
from dscc.models.nimble_perf_policy_summary import NimblePerfPolicySummary

# TODO update the JSON string below
json = "{}"
# create an instance of NimblePerfPolicySummary from a JSON string
nimble_perf_policy_summary_instance = NimblePerfPolicySummary.from_json(json)
# print the JSON string representation of the object
print(NimblePerfPolicySummary.to_json())

# convert the object into a dict
nimble_perf_policy_summary_dict = nimble_perf_policy_summary_instance.to_dict()
# create an instance of NimblePerfPolicySummary from a dict
nimble_perf_policy_summary_from_dict = NimblePerfPolicySummary.from_dict(nimble_perf_policy_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


