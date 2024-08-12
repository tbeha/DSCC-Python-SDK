# DeviceType4vcenterStatus

Status of the vcenter setting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Default status value | [optional] 
**key** | **str** | Status key of vcenter | [optional] 

## Example

```python
from dscc.models.device_type4vcenter_status import DeviceType4vcenterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4vcenterStatus from a JSON string
device_type4vcenter_status_instance = DeviceType4vcenterStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceType4vcenterStatus.to_json())

# convert the object into a dict
device_type4vcenter_status_dict = device_type4vcenter_status_instance.to_dict()
# create an instance of DeviceType4vcenterStatus from a dict
device_type4vcenter_status_from_dict = DeviceType4vcenterStatus.from_dict(device_type4vcenter_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


