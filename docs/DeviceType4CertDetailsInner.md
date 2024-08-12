# DeviceType4CertDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retain_flag** | **str** | Flag of the vasa certificate | [optional] 
**subject** | **str** | Subject of the vasa certificate | [optional] 
**thumbprint** | **str** | Thumbprint of the vasa certificate | [optional] 
**vc_guid** | **str** | vcGuid of the vasa certificate | [optional] 

## Example

```python
from dscc.models.device_type4_cert_details_inner import DeviceType4CertDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CertDetailsInner from a JSON string
device_type4_cert_details_inner_instance = DeviceType4CertDetailsInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CertDetailsInner.to_json())

# convert the object into a dict
device_type4_cert_details_inner_dict = device_type4_cert_details_inner_instance.to_dict()
# create an instance of DeviceType4CertDetailsInner from a dict
device_type4_cert_details_inner_from_dict = DeviceType4CertDetailsInner.from_dict(device_type4_cert_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


