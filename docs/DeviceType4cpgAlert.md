# DeviceType4cpgAlert

Information for posted alerts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fail** | **str** | Alert when there is a growth failure for admin/data space | [optional] 
**limit** | **str** | Alert corresponding to limit for admin/data space | [optional] 
**warn** | **str** | Alert corresponding to warning for admin/data space | [optional] 
**warn_percent** | **float** | Alert corresponding to warning percentage for admin/data space | [optional] 

## Example

```python
from dscc.models.device_type4cpg_alert import DeviceType4cpgAlert

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4cpgAlert from a JSON string
device_type4cpg_alert_instance = DeviceType4cpgAlert.from_json(json)
# print the JSON string representation of the object
print(DeviceType4cpgAlert.to_json())

# convert the object into a dict
device_type4cpg_alert_dict = device_type4cpg_alert_instance.to_dict()
# create an instance of DeviceType4cpgAlert from a dict
device_type4cpg_alert_from_dict = DeviceType4cpgAlert.from_dict(device_type4cpg_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


