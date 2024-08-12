# DeviceType4partnerPortPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** | Port position node number | [optional] 
**port** | **int** | Port position port number | [optional] 
**slot** | **int** | Port position slot number | [optional] 

## Example

```python
from dscc.models.device_type4partner_port_position import DeviceType4partnerPortPosition

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4partnerPortPosition from a JSON string
device_type4partner_port_position_instance = DeviceType4partnerPortPosition.from_json(json)
# print the JSON string representation of the object
print(DeviceType4partnerPortPosition.to_json())

# convert the object into a dict
device_type4partner_port_position_dict = device_type4partner_port_position_instance.to_dict()
# create an instance of DeviceType4partnerPortPosition from a dict
device_type4partner_port_position_from_dict = DeviceType4partnerPortPosition.from_dict(device_type4partner_port_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


