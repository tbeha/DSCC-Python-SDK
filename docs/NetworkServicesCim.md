# NetworkServicesCim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**CimDetails**](CimDetails.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 

## Example

```python
from dscc.models.network_services_cim import NetworkServicesCim

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkServicesCim from a JSON string
network_services_cim_instance = NetworkServicesCim.from_json(json)
# print the JSON string representation of the object
print(NetworkServicesCim.to_json())

# convert the object into a dict
network_services_cim_dict = network_services_cim_instance.to_dict()
# create an instance of NetworkServicesCim from a dict
network_services_cim_from_dict = NetworkServicesCim.from_dict(network_services_cim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


