# ResourceContentionContributors

Top volume contributors for resource contention response structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appset_type** | **str** | Appset Type | [optional] 
**prov_type** | **str** | Provisioning Type | [optional] 
**read_latency** | **float** | Read Latency | [optional] 
**read_throughput** | **float** | Read Throughput | [optional] 
**total_iops** | **float** | Total Iops | [optional] 
**volume_name** | **str** | VolumeName | [optional] 
**volume_status** | **str** | Volume Status | [optional] 
**volume_uid** | **str** | VolumeId | [optional] 
**volume_wwn** | **str** | VolumeWWN | [optional] 
**write_latency** | **float** | Write Latency | [optional] 
**write_throughput** | **float** | Write Throughput | [optional] 

## Example

```python
from dscc.models.resource_contention_contributors import ResourceContentionContributors

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceContentionContributors from a JSON string
resource_contention_contributors_instance = ResourceContentionContributors.from_json(json)
# print the JSON string representation of the object
print(ResourceContentionContributors.to_json())

# convert the object into a dict
resource_contention_contributors_dict = resource_contention_contributors_instance.to_dict()
# create an instance of ResourceContentionContributors from a dict
resource_contention_contributors_from_dict = ResourceContentionContributors.from_dict(resource_contention_contributors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


