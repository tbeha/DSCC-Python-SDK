# DeviceType4NetworkServicesVasa


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**DeviceType4VasaDetails**](DeviceType4VasaDetails.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 

## Example

```python
from dscc.models.device_type4_network_services_vasa import DeviceType4NetworkServicesVasa

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4NetworkServicesVasa from a JSON string
device_type4_network_services_vasa_instance = DeviceType4NetworkServicesVasa.from_json(json)
# print the JSON string representation of the object
print(DeviceType4NetworkServicesVasa.to_json())

# convert the object into a dict
device_type4_network_services_vasa_dict = device_type4_network_services_vasa_instance.to_dict()
# create an instance of DeviceType4NetworkServicesVasa from a dict
device_type4_network_services_vasa_from_dict = DeviceType4NetworkServicesVasa.from_dict(device_type4_network_services_vasa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


