# DeviceType4friendlyCert

Certificate detail in readable format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_from** | [**DeviceType4validity**](DeviceType4validity.md) |  | [optional] 
**valid_until** | [**DeviceType4validity**](DeviceType4validity.md) |  | [optional] 
**issued_to** | **str** | Name of the certificate issued to | [optional] 
**issuer** | **str** | Name of Certificate issued to | [optional] 

## Example

```python
from dscc.models.device_type4friendly_cert import DeviceType4friendlyCert

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4friendlyCert from a JSON string
device_type4friendly_cert_instance = DeviceType4friendlyCert.from_json(json)
# print the JSON string representation of the object
print(DeviceType4friendlyCert.to_json())

# convert the object into a dict
device_type4friendly_cert_dict = device_type4friendly_cert_instance.to_dict()
# create an instance of DeviceType4friendlyCert from a dict
device_type4friendly_cert_from_dict = DeviceType4friendlyCert.from_dict(device_type4friendly_cert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


