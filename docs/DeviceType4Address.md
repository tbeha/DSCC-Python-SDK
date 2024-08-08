# DeviceType4Address


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_node** | **int** | Active node ID | [optional] 
**auto_sense** | **bool** | Specifies if the autosense is enabled for network port | [optional] 
**full_duplex** | **bool** | Is network port full duplex | [optional] 
**ip_address** | **str** | IP Address of the network port | [optional] 
**net_mask** | **str** | Net mask of the network port | [optional] 
**speed** | **int** | Speed of the network port | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**status** | **str** | Status of the network port | [optional] 

## Example

```python
from dscc.models.device_type4_address import DeviceType4Address

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4Address from a JSON string
device_type4_address_instance = DeviceType4Address.from_json(json)
# print the JSON string representation of the object
print(DeviceType4Address.to_json())

# convert the object into a dict
device_type4_address_dict = device_type4_address_instance.to_dict()
# create an instance of DeviceType4Address from a dict
device_type4_address_from_dict = DeviceType4Address.from_dict(device_type4_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


