# CreateVolume

Create a new volume for clone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_cpg** | **str** | Name of the User CPG | [optional] 
**destination_snapshot_cpg** | **str** | Name of the Snapshot CPG | [optional] 

## Example

```python
from dscc.models.create_volume import CreateVolume

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVolume from a JSON string
create_volume_instance = CreateVolume.from_json(json)
# print the JSON string representation of the object
print(CreateVolume.to_json())

# convert the object into a dict
create_volume_dict = create_volume_instance.to_dict()
# create an instance of CreateVolume from a dict
create_volume_from_dict = CreateVolume.from_dict(create_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


