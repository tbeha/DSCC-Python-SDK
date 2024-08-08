# NetworkSettings

Network-Settings details for a device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_management** | [**SysPortManagement**](SysPortManagement.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object  | [optional] 

## Example

```python
from dscc.models.network_settings import NetworkSettings

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkSettings from a JSON string
network_settings_instance = NetworkSettings.from_json(json)
# print the JSON string representation of the object
print(NetworkSettings.to_json())

# convert the object into a dict
network_settings_dict = network_settings_instance.to_dict()
# create an instance of NetworkSettings from a dict
network_settings_from_dict = NetworkSettings.from_dict(network_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


