# DeviceType4CertMgmt

Certificate management mode of the VASA Provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Text in the default language | [optional] 
**key** | **str** | Key of the message | [optional] 

## Example

```python
from dscc.models.device_type4_cert_mgmt import DeviceType4CertMgmt

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CertMgmt from a JSON string
device_type4_cert_mgmt_instance = DeviceType4CertMgmt.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CertMgmt.to_json())

# convert the object into a dict
device_type4_cert_mgmt_dict = device_type4_cert_mgmt_instance.to_dict()
# create an instance of DeviceType4CertMgmt from a dict
device_type4_cert_mgmt_from_dict = DeviceType4CertMgmt.from_dict(device_type4_cert_mgmt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


