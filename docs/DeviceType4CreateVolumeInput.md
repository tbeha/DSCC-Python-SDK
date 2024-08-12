# DeviceType4CreateVolumeInput

Request body for creating volumes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | test | [optional] 
**count** | **int** | Volumes count | [optional] 
**data_reduction** | **bool** | Data Reduction | [optional] 
**name** | **str** | Name of the volume | 
**size_mib** | **int** | Size of the volume to be created. | 
**snapshot_alloc_warning** | **int** | Snapshot Alloc Warning | [optional] 
**user_alloc_warning** | **int** | User Alloc Warning | [optional] 
**user_cpg** | **str** | User CPG | 

## Example

```python
from dscc.models.device_type4_create_volume_input import DeviceType4CreateVolumeInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CreateVolumeInput from a JSON string
device_type4_create_volume_input_instance = DeviceType4CreateVolumeInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CreateVolumeInput.to_json())

# convert the object into a dict
device_type4_create_volume_input_dict = device_type4_create_volume_input_instance.to_dict()
# create an instance of DeviceType4CreateVolumeInput from a dict
device_type4_create_volume_input_from_dict = DeviceType4CreateVolumeInput.from_dict(device_type4_create_volume_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


