# Uptime

The time that the system has been up since

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch time in milliseconds | [optional] 
**tz** | **str** | Time zone name | [optional] 

## Example

```python
from dscc.models.uptime import Uptime

# TODO update the JSON string below
json = "{}"
# create an instance of Uptime from a JSON string
uptime_instance = Uptime.from_json(json)
# print the JSON string representation of the object
print(Uptime.to_json())

# convert the object into a dict
uptime_dict = uptime_instance.to_dict()
# create an instance of Uptime from a dict
uptime_from_dict = Uptime.from_dict(uptime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


