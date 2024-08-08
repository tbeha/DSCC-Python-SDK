# PercentageBucketSetInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the histogram bucket | [optional] 
**percentage** | **float** | Average Percentage of I/O happened in size bucket throughout the interval | [optional] 

## Example

```python
from dscc.models.percentage_bucket_set_inner import PercentageBucketSetInner

# TODO update the JSON string below
json = "{}"
# create an instance of PercentageBucketSetInner from a JSON string
percentage_bucket_set_inner_instance = PercentageBucketSetInner.from_json(json)
# print the JSON string representation of the object
print(PercentageBucketSetInner.to_json())

# convert the object into a dict
percentage_bucket_set_inner_dict = percentage_bucket_set_inner_instance.to_dict()
# create an instance of PercentageBucketSetInner from a dict
percentage_bucket_set_inner_from_dict = PercentageBucketSetInner.from_dict(percentage_bucket_set_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


