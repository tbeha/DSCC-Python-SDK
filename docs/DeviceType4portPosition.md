# DeviceType4portPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** | Port position node number &#x60;Filter, Sort&#x60; | [optional] 
**port** | **int** | Port position port number &#x60;Filter, Sort&#x60; | [optional] 
**slot** | **int** | Port position slot number &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.device_type4port_position import DeviceType4portPosition

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4portPosition from a JSON string
device_type4port_position_instance = DeviceType4portPosition.from_json(json)
# print the JSON string representation of the object
print(DeviceType4portPosition.to_json())

# convert the object into a dict
device_type4port_position_dict = device_type4port_position_instance.to_dict()
# create an instance of DeviceType4portPosition from a dict
device_type4port_position_from_dict = DeviceType4portPosition.from_dict(device_type4port_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


