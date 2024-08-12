# OnlineClone

Online clone of a volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_lun** | **bool** | Specify to use auto lun number. | [optional] 
**destination_cpg** | **str** | Name of the User CPG | [optional] 
**destination_snapshot_cpg** | **str** | Name of the Snapshot CPG | [optional] 
**host_group_id** | **str** | Unique identifier of host group. | [optional] 
**lun** | **int** | LUN of volume. | [optional] 

## Example

```python
from dscc.models.online_clone import OnlineClone

# TODO update the JSON string below
json = "{}"
# create an instance of OnlineClone from a JSON string
online_clone_instance = OnlineClone.from_json(json)
# print the JSON string representation of the object
print(OnlineClone.to_json())

# convert the object into a dict
online_clone_dict = online_clone_instance.to_dict()
# create an instance of OnlineClone from a dict
online_clone_from_dict = OnlineClone.from_dict(online_clone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


