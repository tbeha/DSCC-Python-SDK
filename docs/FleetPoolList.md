# FleetPoolList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_used** | **int** | Capacity Used | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**id** | **str** | Unique Identifier of the resource           | [optional] 
**name** | **str** | Name of the resource | [optional] 
**resource_uri** | **str** | resourceUri for detailed storage-pool object        | [optional] 
**system_id** | **str** | SystemID of the array | [optional] 
**type** | **str** | The type of resource. | [optional] 

## Example

```python
from dscc.models.fleet_pool_list import FleetPoolList

# TODO update the JSON string below
json = "{}"
# create an instance of FleetPoolList from a JSON string
fleet_pool_list_instance = FleetPoolList.from_json(json)
# print the JSON string representation of the object
print(FleetPoolList.to_json())

# convert the object into a dict
fleet_pool_list_dict = fleet_pool_list_instance.to_dict()
# create an instance of FleetPoolList from a dict
fleet_pool_list_from_dict = FleetPoolList.from_dict(fleet_pool_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


