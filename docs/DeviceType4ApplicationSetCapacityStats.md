# DeviceType4ApplicationSetCapacityStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**capacity_summary** | [**DeviceType4ApplicationSetCapacityStatsCapacitySummary**](DeviceType4ApplicationSetCapacityStatsCapacitySummary.md) |  | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**id** | **str** | Uid of the applicationset | [optional] 
**members** | **List[Optional[str]]** | Volume Names | [optional] 
**name** | **str** | Name of the application set | [optional] 
**request_uri** | **str** | RequestUri for applicationsets resources | [optional] 
**system_id** | **str** | SystemId/serialNumber of the array. | [optional] 

## Example

```python
from dscc.models.device_type4_application_set_capacity_stats import DeviceType4ApplicationSetCapacityStats

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ApplicationSetCapacityStats from a JSON string
device_type4_application_set_capacity_stats_instance = DeviceType4ApplicationSetCapacityStats.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ApplicationSetCapacityStats.to_json())

# convert the object into a dict
device_type4_application_set_capacity_stats_dict = device_type4_application_set_capacity_stats_instance.to_dict()
# create an instance of DeviceType4ApplicationSetCapacityStats from a dict
device_type4_application_set_capacity_stats_from_dict = DeviceType4ApplicationSetCapacityStats.from_dict(device_type4_application_set_capacity_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


