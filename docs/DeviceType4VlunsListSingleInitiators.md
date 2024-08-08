# DeviceType4VlunsListSingleInitiators

Initiator details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_discovered_name** | **str** | Host/HostGroup name on device. | [optional] 
**id** | **str** | Resource id | [optional] 
**resource_uri** | **str** | Resource URI | [optional] 
**type** | **str** | Resource Name | [optional] 

## Example

```python
from dscc.models.device_type4_vluns_list_single_initiators import DeviceType4VlunsListSingleInitiators

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VlunsListSingleInitiators from a JSON string
device_type4_vluns_list_single_initiators_instance = DeviceType4VlunsListSingleInitiators.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VlunsListSingleInitiators.to_json())

# convert the object into a dict
device_type4_vluns_list_single_initiators_dict = device_type4_vluns_list_single_initiators_instance.to_dict()
# create an instance of DeviceType4VlunsListSingleInitiators from a dict
device_type4_vluns_list_single_initiators_from_dict = DeviceType4VlunsListSingleInitiators.from_dict(device_type4_vluns_list_single_initiators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


