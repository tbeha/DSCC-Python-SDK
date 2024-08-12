# DeviceType4ecDcsdata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fw_status** | **str** |  | [optional] 
**fw_version** | **str** |  | [optional] 
**master** | **bool** |  | [optional] 
**sas_status** | **str** |  | [optional] 

## Example

```python
from dscc.models.device_type4ec_dcsdata import DeviceType4ecDcsdata

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ecDcsdata from a JSON string
device_type4ec_dcsdata_instance = DeviceType4ecDcsdata.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ecDcsdata.to_json())

# convert the object into a dict
device_type4ec_dcsdata_dict = device_type4ec_dcsdata_instance.to_dict()
# create an instance of DeviceType4ecDcsdata from a dict
device_type4ec_dcsdata_from_dict = DeviceType4ecDcsdata.from_dict(device_type4ec_dcsdata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


