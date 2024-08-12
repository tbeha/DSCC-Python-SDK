# AdmitTime

admission time of disk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | time in millisecond | [optional] 
**tz** | **str** | timezone | [optional] 

## Example

```python
from dscc.models.admit_time import AdmitTime

# TODO update the JSON string below
json = "{}"
# create an instance of AdmitTime from a JSON string
admit_time_instance = AdmitTime.from_json(json)
# print the JSON string representation of the object
print(AdmitTime.to_json())

# convert the object into a dict
admit_time_dict = admit_time_instance.to_dict()
# create an instance of AdmitTime from a dict
admit_time_from_dict = AdmitTime.from_dict(admit_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


