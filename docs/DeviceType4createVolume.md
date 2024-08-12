# DeviceType4createVolume

Create a new volume for clone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_cpg** | **str** | Name of the User CPG | [optional] 

## Example

```python
from dscc.models.device_type4create_volume import DeviceType4createVolume

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4createVolume from a JSON string
device_type4create_volume_instance = DeviceType4createVolume.from_json(json)
# print the JSON string representation of the object
print(DeviceType4createVolume.to_json())

# convert the object into a dict
device_type4create_volume_dict = device_type4create_volume_instance.to_dict()
# create an instance of DeviceType4createVolume from a dict
device_type4create_volume_from_dict = DeviceType4createVolume.from_dict(device_type4create_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


