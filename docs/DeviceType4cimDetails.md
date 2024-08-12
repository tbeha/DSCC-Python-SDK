# DeviceType4cimDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**cim** | [**DeviceType4cim**](DeviceType4cim.md) |  | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**system_id** | **str** | SystemId of the storage system | [optional] 

## Example

```python
from dscc.models.device_type4cim_details import DeviceType4cimDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4cimDetails from a JSON string
device_type4cim_details_instance = DeviceType4cimDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4cimDetails.to_json())

# convert the object into a dict
device_type4cim_details_dict = device_type4cim_details_instance.to_dict()
# create an instance of DeviceType4cimDetails from a dict
device_type4cim_details_from_dict = DeviceType4cimDetails.from_dict(device_type4cim_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


