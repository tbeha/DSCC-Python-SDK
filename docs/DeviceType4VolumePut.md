# DeviceType4VolumePut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion_type** | **str** | conversion type (this argument is depricated, use dataReduction instead) | [optional] 
**data_reduction** | **bool** | Data Reduction on Volume. | [optional] 
**name** | **str** | volume name | [optional] 
**size_mib** | **float** | Size of the volume to be edited. | [optional] 
**snapshot_alloc_warning** | **int** | snapshot alloc space allocation warning | [optional] 
**user_alloc_warning** | **int** | User alloc space limit warning | [optional] 
**user_cpg_name** | **str** | user cpg name | [optional] 

## Example

```python
from dscc.models.device_type4_volume_put import DeviceType4VolumePut

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VolumePut from a JSON string
device_type4_volume_put_instance = DeviceType4VolumePut.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VolumePut.to_json())

# convert the object into a dict
device_type4_volume_put_dict = device_type4_volume_put_instance.to_dict()
# create an instance of DeviceType4VolumePut from a dict
device_type4_volume_put_from_dict = DeviceType4VolumePut.from_dict(device_type4_volume_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


