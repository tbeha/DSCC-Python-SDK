# DeviceType4esDc4data


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hpl_led** | [**DeviceType4LED**](DeviceType4LED.md) |  | [optional] 
**left** | **bool** |  | [optional] 
**right** | **bool** |  | [optional] 
**system_led** | [**DeviceType4LED**](DeviceType4LED.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4es_dc4data import DeviceType4esDc4data

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4esDc4data from a JSON string
device_type4es_dc4data_instance = DeviceType4esDc4data.from_json(json)
# print the JSON string representation of the object
print(DeviceType4esDc4data.to_json())

# convert the object into a dict
device_type4es_dc4data_dict = device_type4es_dc4data_instance.to_dict()
# create an instance of DeviceType4esDc4data from a dict
device_type4es_dc4data_from_dict = DeviceType4esDc4data.from_dict(device_type4es_dc4data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


