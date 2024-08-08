# DeviceType4CreatevVolSCInput

Request body for creating VMware Storage Container

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain that the resource belongs to | [optional] 
**host_ids** | **List[str]** | Host IDs | [optional] 
**host_set_ids** | **List[str]** | Host Set IDs | [optional] 
**name** | **str** | Storage Container Name. | 
**sc_type** | **str** | Field is supported from 10.4.0 and above. Indicates the type of the VMware VASA storage container that would get created in the system. Valid values are NVMe and SCSI. | [optional] 

## Example

```python
from dscc.models.device_type4_createv_vol_sc_input import DeviceType4CreatevVolSCInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CreatevVolSCInput from a JSON string
device_type4_createv_vol_sc_input_instance = DeviceType4CreatevVolSCInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CreatevVolSCInput.to_json())

# convert the object into a dict
device_type4_createv_vol_sc_input_dict = device_type4_createv_vol_sc_input_instance.to_dict()
# create an instance of DeviceType4CreatevVolSCInput from a dict
device_type4_createv_vol_sc_input_from_dict = DeviceType4CreatevVolSCInput.from_dict(device_type4_createv_vol_sc_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


