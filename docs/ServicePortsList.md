# ServicePortsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ServicePorts]**](ServicePorts.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed volume set object | [optional] 
**total** | **int** | Number of serviceports. | [optional] 

## Example

```python
from dscc.models.service_ports_list import ServicePortsList

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePortsList from a JSON string
service_ports_list_instance = ServicePortsList.from_json(json)
# print the JSON string representation of the object
print(ServicePortsList.to_json())

# convert the object into a dict
service_ports_list_dict = service_ports_list_instance.to_dict()
# create an instance of ServicePortsList from a dict
service_ports_list_from_dict = ServicePortsList.from_dict(service_ports_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


