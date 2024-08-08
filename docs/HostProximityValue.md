# HostProximityValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** | Replication Group Name | [optional] 
**group_uid** | **str** | Replication Group ID | [optional] 
**host_id** | **str** | Host ID | [optional] 
**host_name** | **str** | Host name | [optional] 
**proximity_system_name** | **str** | Host proximity value | [optional] 
**system_name** | **str** | Source system name | [optional] 
**system_uid** | **str** | Source system serial number | [optional] 
**target_name** | **str** | Target system name | [optional] 
**target_system_id** | **str** | Target system serial number | [optional] 

## Example

```python
from dscc.models.host_proximity_value import HostProximityValue

# TODO update the JSON string below
json = "{}"
# create an instance of HostProximityValue from a JSON string
host_proximity_value_instance = HostProximityValue.from_json(json)
# print the JSON string representation of the object
print(HostProximityValue.to_json())

# convert the object into a dict
host_proximity_value_dict = host_proximity_value_instance.to_dict()
# create an instance of HostProximityValue from a dict
host_proximity_value_from_dict = HostProximityValue.from_dict(host_proximity_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


