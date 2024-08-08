# DeviceType4vlunsListPortPos

System port VLUN is exported through. It includes node number, slot number, and port number

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** | &#x60;Filter, Sort&#x60; | [optional] 
**port** | **int** | &#x60;Filter, Sort&#x60; | [optional] 
**slot** | **int** | &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.device_type4vluns_list_port_pos import DeviceType4vlunsListPortPos

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4vlunsListPortPos from a JSON string
device_type4vluns_list_port_pos_instance = DeviceType4vlunsListPortPos.from_json(json)
# print the JSON string representation of the object
print(DeviceType4vlunsListPortPos.to_json())

# convert the object into a dict
device_type4vluns_list_port_pos_dict = device_type4vluns_list_port_pos_instance.to_dict()
# create an instance of DeviceType4vlunsListPortPos from a dict
device_type4vluns_list_port_pos_from_dict = DeviceType4vlunsListPortPos.from_dict(device_type4vluns_list_port_pos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


