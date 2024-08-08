# Nodeuptime

The time that the system has been up since

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch time in milliseconds | [optional] 
**tz** | **str** | Time zone name | [optional] 

## Example

```python
from dscc.models.nodeuptime import Nodeuptime

# TODO update the JSON string below
json = "{}"
# create an instance of Nodeuptime from a JSON string
nodeuptime_instance = Nodeuptime.from_json(json)
# print the JSON string representation of the object
print(Nodeuptime.to_json())

# convert the object into a dict
nodeuptime_dict = nodeuptime_instance.to_dict()
# create an instance of Nodeuptime from a dict
nodeuptime_from_dict = Nodeuptime.from_dict(nodeuptime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


