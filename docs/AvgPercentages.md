# AvgPercentages

Average percentage of performance histogram

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read** | [**List[PercentageBucketSetInner]**](PercentageBucketSetInner.md) | List of histogram size buckets and respective average percentage of I/O throughout the interval | [optional] 
**write** | [**List[PercentageBucketSetInner]**](PercentageBucketSetInner.md) | List of histogram size buckets and respective average percentage of I/O throughout the interval | [optional] 

## Example

```python
from dscc.models.avg_percentages import AvgPercentages

# TODO update the JSON string below
json = "{}"
# create an instance of AvgPercentages from a JSON string
avg_percentages_instance = AvgPercentages.from_json(json)
# print the JSON string representation of the object
print(AvgPercentages.to_json())

# convert the object into a dict
avg_percentages_dict = avg_percentages_instance.to_dict()
# create an instance of AvgPercentages from a dict
avg_percentages_from_dict = AvgPercentages.from_dict(avg_percentages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


