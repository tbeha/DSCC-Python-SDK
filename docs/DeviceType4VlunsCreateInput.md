# DeviceType4VlunsCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun** | [**List[DeviceType4VlunsCreateInputLUNInner]**](DeviceType4VlunsCreateInputLUNInner.md) | Custom LUN Id for multiple host groups | [optional] 
**auto_lun** | **bool** | Auto Lun | [optional] 
**host_group_ids** | **List[Optional[str]]** | HostGroups | 
**max_auto_lun** | **int** | Number of volumes. | [optional] 
**no_vcn** | **bool** | No VCN | [optional] 
**override** | **bool** | Override | [optional] 
**position** | **str** | Position. This field is deprecated. | [optional] 
**proximity** | **str** | Host proximity setting for Active Peer Persistence configuration. Supported values are - PRIMARY, SECONDARY and ALL. Default proximity is PRIMARY. | [optional] 

## Example

```python
from dscc.models.device_type4_vluns_create_input import DeviceType4VlunsCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VlunsCreateInput from a JSON string
device_type4_vluns_create_input_instance = DeviceType4VlunsCreateInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VlunsCreateInput.to_json())

# convert the object into a dict
device_type4_vluns_create_input_dict = device_type4_vluns_create_input_instance.to_dict()
# create an instance of DeviceType4VlunsCreateInput from a dict
device_type4_vluns_create_input_from_dict = DeviceType4VlunsCreateInput.from_dict(device_type4_vluns_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


