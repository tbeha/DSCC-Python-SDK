# DeviceType4edDc4data


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esi** | **bool** |  | [optional] 
**esi_status** | **str** |  | [optional] 
**system_led** | [**DeviceType4LED**](DeviceType4LED.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4ed_dc4data import DeviceType4edDc4data

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4edDc4data from a JSON string
device_type4ed_dc4data_instance = DeviceType4edDc4data.from_json(json)
# print the JSON string representation of the object
print(DeviceType4edDc4data.to_json())

# convert the object into a dict
device_type4ed_dc4data_dict = device_type4ed_dc4data_instance.to_dict()
# create an instance of DeviceType4edDc4data from a dict
device_type4ed_dc4data_from_dict = DeviceType4edDc4data.from_dict(device_type4ed_dc4data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


