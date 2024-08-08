# DeviceType4NetworkServicesCim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**DeviceType4cimDetails**](DeviceType4cimDetails.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 

## Example

```python
from dscc.models.device_type4_network_services_cim import DeviceType4NetworkServicesCim

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4NetworkServicesCim from a JSON string
device_type4_network_services_cim_instance = DeviceType4NetworkServicesCim.from_json(json)
# print the JSON string representation of the object
print(DeviceType4NetworkServicesCim.to_json())

# convert the object into a dict
device_type4_network_services_cim_dict = device_type4_network_services_cim_instance.to_dict()
# create an instance of DeviceType4NetworkServicesCim from a dict
device_type4_network_services_cim_from_dict = DeviceType4NetworkServicesCim.from_dict(device_type4_network_services_cim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


