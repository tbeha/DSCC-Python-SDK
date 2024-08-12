# EditThrottle

A single throttle for the partner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **str** | Comma separated list of days of the week or &#39;all&#39;. | [optional] 
**description** | **str** | Description of the throttle. | [optional] 
**thr_at_time** | **int** | Start time for the throttle. | [optional] 
**thr_bandwidth** | **int** | Bandwidth for the throttle in megabits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no limit. This attribute is superseded by thr_bandwidth_limit_kbps. Use either thr_bandwidth or thr_bandwidth_kbps to set throttle bandwidth. | [optional] 
**thr_bandwidth_kbps** | **int** | Bandwidth for the throttle in kilobits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no limit. This atttibute is superseded by thr_bandwidth_limit_kbps. Use either thr_bandwidth or thr_bandwidth_kbps to set throttle bandwidth. | [optional] 
**thr_bandwidth_limit_kbps** | **int** | Bandwidth for the throttle in kilobits per second or -1 to indicate that there is no limit. | [optional] 
**thr_until_time** | **int** | End time for the throttle. | [optional] 

## Example

```python
from dscc.models.edit_throttle import EditThrottle

# TODO update the JSON string below
json = "{}"
# create an instance of EditThrottle from a JSON string
edit_throttle_instance = EditThrottle.from_json(json)
# print the JSON string representation of the object
print(EditThrottle.to_json())

# convert the object into a dict
edit_throttle_dict = edit_throttle_instance.to_dict()
# create an instance of EditThrottle from a dict
edit_throttle_from_dict = EditThrottle.from_dict(edit_throttle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


