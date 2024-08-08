# DeviceType4dc4dataSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hpl_led** | [**DeviceType4HPLLEDSINGLE**](DeviceType4HPLLEDSINGLE.md) |  | [optional] 
**left** | **bool** |  | [optional] 
**right** | **bool** |  | [optional] 
**system_led** | [**DeviceType4SYSTEMLEDSINGLE**](DeviceType4SYSTEMLEDSINGLE.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4dc4data_single import DeviceType4dc4dataSingle

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4dc4dataSingle from a JSON string
device_type4dc4data_single_instance = DeviceType4dc4dataSingle.from_json(json)
# print the JSON string representation of the object
print(DeviceType4dc4dataSingle.to_json())

# convert the object into a dict
device_type4dc4data_single_dict = device_type4dc4data_single_instance.to_dict()
# create an instance of DeviceType4dc4dataSingle from a dict
device_type4dc4data_single_from_dict = DeviceType4dc4dataSingle.from_dict(device_type4dc4data_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


