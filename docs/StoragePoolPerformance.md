# StoragePoolPerformance

storage pool performance trends for given granularity and time range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**iops** | [**NimbleperfData**](NimbleperfData.md) |  | [optional] 
**latency** | [**NimbleperfData**](NimbleperfData.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage pool object | [optional] 
**throughput** | [**NimbleperfData**](NimbleperfData.md) |  | [optional] 

## Example

```python
from dscc.models.storage_pool_performance import StoragePoolPerformance

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePoolPerformance from a JSON string
storage_pool_performance_instance = StoragePoolPerformance.from_json(json)
# print the JSON string representation of the object
print(StoragePoolPerformance.to_json())

# convert the object into a dict
storage_pool_performance_dict = storage_pool_performance_instance.to_dict()
# create an instance of StoragePoolPerformance from a dict
storage_pool_performance_from_dict = StoragePoolPerformance.from_dict(storage_pool_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


