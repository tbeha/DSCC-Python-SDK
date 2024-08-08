# HostVolumes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | customerId | [optional] 
**iops** | **float** | IOPS | [optional] 
**latency_ms** | **float** | Latency in ms | [optional] 
**lun_id** | **int** | lunid | [optional] 
**path_count** | **int** | The number of connections from that volume | [optional] 
**resource_uri** | **str** | resourceUri of the volume | [optional] 
**system_id** | **str** | SystemUid of the system associated with the volume | [optional] 
**throughput_kbps** | **float** | The throughput in kbps | [optional] 
**volume_name** | **str** | The name of the volume | [optional] 

## Example

```python
from dscc.models.host_volumes import HostVolumes

# TODO update the JSON string below
json = "{}"
# create an instance of HostVolumes from a JSON string
host_volumes_instance = HostVolumes.from_json(json)
# print the JSON string representation of the object
print(HostVolumes.to_json())

# convert the object into a dict
host_volumes_dict = host_volumes_instance.to_dict()
# create an instance of HostVolumes from a dict
host_volumes_from_dict = HostVolumes.from_dict(host_volumes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


