# DeviceType4allocationHA

Requested High Availability setting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from dscc.models.device_type4allocation_ha import DeviceType4allocationHA

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4allocationHA from a JSON string
device_type4allocation_ha_instance = DeviceType4allocationHA.from_json(json)
# print the JSON string representation of the object
print(DeviceType4allocationHA.to_json())

# convert the object into a dict
device_type4allocation_ha_dict = device_type4allocation_ha_instance.to_dict()
# create an instance of DeviceType4allocationHA from a dict
device_type4allocation_ha_from_dict = DeviceType4allocationHA.from_dict(device_type4allocation_ha_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


