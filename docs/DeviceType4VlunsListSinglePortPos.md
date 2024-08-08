# DeviceType4VlunsListSinglePortPos

System port VLUN is exported through. It includes node number, slot number, and port number

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** |  | [optional] 
**port** | **int** |  | [optional] 
**slot** | **int** |  | [optional] 

## Example

```python
from dscc.models.device_type4_vluns_list_single_port_pos import DeviceType4VlunsListSinglePortPos

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VlunsListSinglePortPos from a JSON string
device_type4_vluns_list_single_port_pos_instance = DeviceType4VlunsListSinglePortPos.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VlunsListSinglePortPos.to_json())

# convert the object into a dict
device_type4_vluns_list_single_port_pos_dict = device_type4_vluns_list_single_port_pos_instance.to_dict()
# create an instance of DeviceType4VlunsListSinglePortPos from a dict
device_type4_vluns_list_single_port_pos_from_dict = DeviceType4VlunsListSinglePortPos.from_dict(device_type4_vluns_list_single_port_pos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


