# NimbleVolumeSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_type** | **str** | Agent type of the volume. Possible values: &#39;none&#39;, &#39;smis&#39;, &#39;vvol&#39;, &#39;openstack&#39;. | [optional] 
**has_locked_snapshots** | **bool** | To verify a volume has an immutable snapshot or not. | [optional] 
**id** | **str** | Identifier of volume. A 42 digit hexadecimal number. | [optional] 
**name** | **str** | Name of volume. | [optional] 
**vol_id** | **str** | Identifier of volume. A 42 digit hexadecimal number. | [optional] 
**vol_name** | **str** | Name of volume. | [optional] 
**volume_creator_id** | **str** | Originator id for the associated volume. | [optional] 
**volume_creator_name** | **str** | Originator name for the associated volume. | [optional] 

## Example

```python
from dscc.models.nimble_volume_summary import NimbleVolumeSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleVolumeSummary from a JSON string
nimble_volume_summary_instance = NimbleVolumeSummary.from_json(json)
# print the JSON string representation of the object
print(NimbleVolumeSummary.to_json())

# convert the object into a dict
nimble_volume_summary_dict = nimble_volume_summary_instance.to_dict()
# create an instance of NimbleVolumeSummary from a dict
nimble_volume_summary_from_dict = NimbleVolumeSummary.from_dict(nimble_volume_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


