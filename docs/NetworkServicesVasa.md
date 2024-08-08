# NetworkServicesVasa


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**VasaDetails**](VasaDetails.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object        | [optional] 

## Example

```python
from dscc.models.network_services_vasa import NetworkServicesVasa

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkServicesVasa from a JSON string
network_services_vasa_instance = NetworkServicesVasa.from_json(json)
# print the JSON string representation of the object
print(NetworkServicesVasa.to_json())

# convert the object into a dict
network_services_vasa_dict = network_services_vasa_instance.to_dict()
# create an instance of NetworkServicesVasa from a dict
network_services_vasa_from_dict = NetworkServicesVasa.from_dict(network_services_vasa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


