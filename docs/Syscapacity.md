# Syscapacity

system capacity details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**capacity_by_tier** | [**CapacityByTier**](CapacityByTier.md) |  | [optional] 
**capacity_detail** | [**SystemDetailedCapacity**](SystemDetailedCapacity.md) |  | [optional] 
**capacity_summary** | [**SystemCapacitySummary**](SystemCapacitySummary.md) |  | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**fc_capacity_summary** | [**SystemCapacitySummary**](SystemCapacitySummary.md) |  | [optional] 
**id** | **str** | ID string uniquely identifying the object. | [optional] 
**nl_capacity_summary** | [**SystemCapacitySummary**](SystemCapacitySummary.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**resource_uri** | **str** | resourceUri for detailed storage object | [optional] 
**ssd_capacity_summary** | [**SystemCapacitySummary**](SystemCapacitySummary.md) |  | [optional] 
**system_id** | **str** | SystemId/serialNumber of the array. | [optional] 
**utilization_summary** | [**UtilizationSummary**](UtilizationSummary.md) |  | [optional] 

## Example

```python
from dscc.models.syscapacity import Syscapacity

# TODO update the JSON string below
json = "{}"
# create an instance of Syscapacity from a JSON string
syscapacity_instance = Syscapacity.from_json(json)
# print the JSON string representation of the object
print(Syscapacity.to_json())

# convert the object into a dict
syscapacity_dict = syscapacity_instance.to_dict()
# create an instance of Syscapacity from a dict
syscapacity_from_dict = Syscapacity.from_dict(syscapacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


