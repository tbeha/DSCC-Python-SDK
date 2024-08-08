# NetworkServicesVvolscs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[VvolscDetails]**](VvolscDetails.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**total** | **int** | Number of storage container | [optional] 

## Example

```python
from dscc.models.network_services_vvolscs import NetworkServicesVvolscs

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkServicesVvolscs from a JSON string
network_services_vvolscs_instance = NetworkServicesVvolscs.from_json(json)
# print the JSON string representation of the object
print(NetworkServicesVvolscs.to_json())

# convert the object into a dict
network_services_vvolscs_dict = network_services_vvolscs_instance.to_dict()
# create an instance of NetworkServicesVvolscs from a dict
network_services_vvolscs_from_dict = NetworkServicesVvolscs.from_dict(network_services_vvolscs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


