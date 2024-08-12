# DeviceType4systemCapacitySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | [**DeviceType4allocated**](DeviceType4allocated.md) |  | [optional] 
**allocated_percentage** | **float** | Percentage of allocated capacity for the system | [optional] 
**compaction** | **float** | Compaction details | [optional] 
**compression** | **float** | Compression details | [optional] 
**data_reduction** | **float** | Data reduction | [optional] 
**dedup** | **float** | Dedup Details | [optional] 
**failed** | **float** | Failed capacity | [optional] 
**failed_percentage** | **float** | Percentage of failed capacity | [optional] 
**free** | **float** | Free capacity of the system | [optional] 
**free_initialized** | **float** | Intialized capacity out of the free capacity | [optional] 
**free_percentage** | **float** | Percentage of the free capacity | [optional] 
**free_uninitialized** | **float** | Uninitialized capacity out of the free capacity | [optional] 
**over_provisioning** | **float** | Over provisioning ratio | [optional] 
**total** | **float** | Total capacity of the system | [optional] 
**unavailable** | **float** | Unavailable storage | [optional] 
**unavailable_percentage** | **float** | Percentage of storage that is unavailable | [optional] 

## Example

```python
from dscc.models.device_type4system_capacity_summary import DeviceType4systemCapacitySummary

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4systemCapacitySummary from a JSON string
device_type4system_capacity_summary_instance = DeviceType4systemCapacitySummary.from_json(json)
# print the JSON string representation of the object
print(DeviceType4systemCapacitySummary.to_json())

# convert the object into a dict
device_type4system_capacity_summary_dict = device_type4system_capacity_summary_instance.to_dict()
# create an instance of DeviceType4systemCapacitySummary from a dict
device_type4system_capacity_summary_from_dict = DeviceType4systemCapacitySummary.from_dict(device_type4system_capacity_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


