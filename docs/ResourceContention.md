# ResourceContention

Resource contention response structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**cpu_contention** | [**ResourceContentionData**](ResourceContentionData.md) |  | [optional] 
**customer_id** | **str** | CustomerId | [optional] 
**disk_contention** | [**ResourceContentionData**](ResourceContentionData.md) |  | [optional] 
**end_time** | **float** | End time of the interval for which resource contention is computed | [optional] 
**request_uri** | **str** | requestUri for HPE Alletra Storage MP insights resource contention | [optional] 
**start_time** | **float** | Start time of the interval for which resource contention is computed | [optional] 
**system_id** | **str** | Serial number of the array | [optional] 

## Example

```python
from dscc.models.resource_contention import ResourceContention

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceContention from a JSON string
resource_contention_instance = ResourceContention.from_json(json)
# print the JSON string representation of the object
print(ResourceContention.to_json())

# convert the object into a dict
resource_contention_dict = resource_contention_instance.to_dict()
# create an instance of ResourceContention from a dict
resource_contention_from_dict = ResourceContention.from_dict(resource_contention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


