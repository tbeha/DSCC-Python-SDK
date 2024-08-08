# HostProximityDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_remote_array_support_replication** | **bool** | Boolean value to indicate if remote array OS version supports replication | [optional] 
**is_source_array_support_replication** | **bool** | Boolean value to indicate if source array OS version supports replication | [optional] 
**local_system** | **str** | Local system where host I/O path is Active optimized | [optional] 
**proximity_value** | **str** | Host proximity to determine the Asymmetric Logical path access state | [optional] 
**remote_system** | **str** | Remote system where host I/O path is Active Non-optimized | [optional] 

## Example

```python
from dscc.models.host_proximity_detail import HostProximityDetail

# TODO update the JSON string below
json = "{}"
# create an instance of HostProximityDetail from a JSON string
host_proximity_detail_instance = HostProximityDetail.from_json(json)
# print the JSON string representation of the object
print(HostProximityDetail.to_json())

# convert the object into a dict
host_proximity_detail_dict = host_proximity_detail_instance.to_dict()
# create an instance of HostProximityDetail from a dict
host_proximity_detail_from_dict = HostProximityDetail.from_dict(host_proximity_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


