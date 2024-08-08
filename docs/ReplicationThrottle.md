# ReplicationThrottle

A single throttle for the partner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **str** | List of days that the throttle operates. | [optional] 
**description** | **str** | Description of the throttle. | [optional] 
**name** | **str** | Name of the throttle. | [optional] 
**thr_at_time** | **int** | Start time set for the throttle. | [optional] 
**thr_bandwidth** | **int** | Bandwidth set for the throttle in megabits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no limit. This attribute is superseded by thr_bandwidth_limit_kbps. | [optional] 
**thr_until_time** | **int** | End time set for the throttle. | [optional] 

## Example

```python
from dscc.models.replication_throttle import ReplicationThrottle

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationThrottle from a JSON string
replication_throttle_instance = ReplicationThrottle.from_json(json)
# print the JSON string representation of the object
print(ReplicationThrottle.to_json())

# convert the object into a dict
replication_throttle_dict = replication_throttle_instance.to_dict()
# create an instance of ReplicationThrottle from a dict
replication_throttle_from_dict = ReplicationThrottle.from_dict(replication_throttle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


