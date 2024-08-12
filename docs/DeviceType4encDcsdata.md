# DeviceType4encDcsdata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fw_status** | **str** |  | [optional] 
**fw_version** | **str** |  | [optional] 

## Example

```python
from dscc.models.device_type4enc_dcsdata import DeviceType4encDcsdata

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4encDcsdata from a JSON string
device_type4enc_dcsdata_instance = DeviceType4encDcsdata.from_json(json)
# print the JSON string representation of the object
print(DeviceType4encDcsdata.to_json())

# convert the object into a dict
device_type4enc_dcsdata_dict = device_type4enc_dcsdata_instance.to_dict()
# create an instance of DeviceType4encDcsdata from a dict
device_type4enc_dcsdata_from_dict = DeviceType4encDcsdata.from_dict(device_type4enc_dcsdata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


