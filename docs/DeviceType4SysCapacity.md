# DeviceType4SysCapacity

system capacity details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**capacity_by_tier** | [**DeviceType4capacityByTier**](DeviceType4capacityByTier.md) |  | [optional] 
**capacity_detail** | [**DeviceType4SystemCapacityUsage**](DeviceType4SystemCapacityUsage.md) |  | [optional] 
**capacity_summary** | [**DeviceType4systemCapacitySummary**](DeviceType4systemCapacitySummary.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**fc_capacity_summary** | [**DeviceType4systemCapacitySummary**](DeviceType4systemCapacitySummary.md) |  | [optional] 
**id** | **str** | ID string uniquely identifying the object. | [optional] 
**nl_capacity_summary** | [**DeviceType4systemCapacitySummary**](DeviceType4systemCapacitySummary.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**resource_uri** | **str** | resourceUri for detailed storage object | [optional] 
**ssd_capacity_summary** | [**DeviceType4systemCapacitySummary**](DeviceType4systemCapacitySummary.md) |  | [optional] 
**system_id** | **str** | SystemId/serialNumber of the array. | [optional] 
**utilization_summary** | [**DeviceType4utilizationSummary**](DeviceType4utilizationSummary.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_sys_capacity import DeviceType4SysCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SysCapacity from a JSON string
device_type4_sys_capacity_instance = DeviceType4SysCapacity.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SysCapacity.to_json())

# convert the object into a dict
device_type4_sys_capacity_dict = device_type4_sys_capacity_instance.to_dict()
# create an instance of DeviceType4SysCapacity from a dict
device_type4_sys_capacity_from_dict = DeviceType4SysCapacity.from_dict(device_type4_sys_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


