# DeviceType4softwareVersionsSolo

Software versions of the product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_version** | **str** | Base Version | [optional] 
**components** | [**List[DeviceType4softwareVersionsSoloComponentsInner]**](DeviceType4softwareVersionsSoloComponentsInner.md) |  | [optional] 
**full_version** | **str** | Full Version | [optional] 
**patches** | **str** | Set of Patches | [optional] 
**release** | **str** | Release Version | [optional] 

## Example

```python
from dscc.models.device_type4software_versions_solo import DeviceType4softwareVersionsSolo

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4softwareVersionsSolo from a JSON string
device_type4software_versions_solo_instance = DeviceType4softwareVersionsSolo.from_json(json)
# print the JSON string representation of the object
print(DeviceType4softwareVersionsSolo.to_json())

# convert the object into a dict
device_type4software_versions_solo_dict = device_type4software_versions_solo_instance.to_dict()
# create an instance of DeviceType4softwareVersionsSolo from a dict
device_type4software_versions_solo_from_dict = DeviceType4softwareVersionsSolo.from_dict(device_type4software_versions_solo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


