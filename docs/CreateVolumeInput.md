# CreateVolumeInput

Request body for creating volumes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | test | [optional] 
**count** | **int** | Volumes count | [optional] 
**data_reduction** | **bool** | Data Reduction | [optional] 
**name** | **str** | Name of the volume | 
**size_mib** | **int** | Size in MB | 
**snap_cpg** | **str** | Snap CPG | [optional] 
**snapshot_alloc_warning** | **int** | Snapshot Alloc Warning | [optional] 
**user_alloc_warning** | **int** | User Alloc Warning | [optional] 
**user_cpg** | **str** | User CPG of the volume to be created | 

## Example

```python
from dscc.models.create_volume_input import CreateVolumeInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVolumeInput from a JSON string
create_volume_input_instance = CreateVolumeInput.from_json(json)
# print the JSON string representation of the object
print(CreateVolumeInput.to_json())

# convert the object into a dict
create_volume_input_dict = create_volume_input_instance.to_dict()
# create an instance of CreateVolumeInput from a dict
create_volume_input_from_dict = CreateVolumeInput.from_dict(create_volume_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


