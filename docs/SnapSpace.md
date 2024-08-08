# SnapSpace

snapSpace information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ld_count** | **float** | Number of Logical Disks | [optional] 
**total_mi_b** | **float** | Total logical capacity (MiB) | [optional] 
**total_raw_mi_b** | **float** | Total physical (raw) capacity (MiB) | [optional] 
**used_mi_b** | **float** | Used logical capacity (MiB). Updated in Cloud Data Store at most once per 30 minutes. | [optional] 
**used_raw_mi_b** | **float** | Used physical (raw) capacity (MiB). Updated in Cloud Data Store at most once per 30 minutes. | [optional] 

## Example

```python
from dscc.models.snap_space import SnapSpace

# TODO update the JSON string below
json = "{}"
# create an instance of SnapSpace from a JSON string
snap_space_instance = SnapSpace.from_json(json)
# print the JSON string representation of the object
print(SnapSpace.to_json())

# convert the object into a dict
snap_space_dict = snap_space_instance.to_dict()
# create an instance of SnapSpace from a dict
snap_space_from_dict = SnapSpace.from_dict(snap_space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


