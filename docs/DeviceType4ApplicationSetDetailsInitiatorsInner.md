# DeviceType4ApplicationSetDetailsInitiatorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_discovered_name** | **str** | Host/HostGroup name on device. | [optional] 
**id** | **str** | Resource id | [optional] 
**resource_uri** | **str** | Resource URI | [optional] 
**type** | **str** | Resource Name | [optional] 

## Example

```python
from dscc.models.device_type4_application_set_details_initiators_inner import DeviceType4ApplicationSetDetailsInitiatorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ApplicationSetDetailsInitiatorsInner from a JSON string
device_type4_application_set_details_initiators_inner_instance = DeviceType4ApplicationSetDetailsInitiatorsInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ApplicationSetDetailsInitiatorsInner.to_json())

# convert the object into a dict
device_type4_application_set_details_initiators_inner_dict = device_type4_application_set_details_initiators_inner_instance.to_dict()
# create an instance of DeviceType4ApplicationSetDetailsInitiatorsInner from a dict
device_type4_application_set_details_initiators_inner_from_dict = DeviceType4ApplicationSetDetailsInitiatorsInner.from_dict(device_type4_application_set_details_initiators_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


