# DeviceType4ServicePortsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4servicePorts]**](DeviceType4servicePorts.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed volume set object | [optional] 
**total** | **int** | Number of serviceports. | [optional] 

## Example

```python
from dscc.models.device_type4_service_ports_list import DeviceType4ServicePortsList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ServicePortsList from a JSON string
device_type4_service_ports_list_instance = DeviceType4ServicePortsList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ServicePortsList.to_json())

# convert the object into a dict
device_type4_service_ports_list_dict = device_type4_service_ports_list_instance.to_dict()
# create an instance of DeviceType4ServicePortsList from a dict
device_type4_service_ports_list_from_dict = DeviceType4ServicePortsList.from_dict(device_type4_service_ports_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


