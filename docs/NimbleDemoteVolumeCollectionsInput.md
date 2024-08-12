# NimbleDemoteVolumeCollectionsInput

Perform demote action on a volume collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoke_on_upstream_partner** | **bool** | Invoke demote request on upstream partner. Default: &#39;false&#39;. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**replication_partner_id** | **str** | Replication partner ID of the new owner. A 42 digit hexadecimal number. | 

## Example

```python
from dscc.models.nimble_demote_volume_collections_input import NimbleDemoteVolumeCollectionsInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleDemoteVolumeCollectionsInput from a JSON string
nimble_demote_volume_collections_input_instance = NimbleDemoteVolumeCollectionsInput.from_json(json)
# print the JSON string representation of the object
print(NimbleDemoteVolumeCollectionsInput.to_json())

# convert the object into a dict
nimble_demote_volume_collections_input_dict = nimble_demote_volume_collections_input_instance.to_dict()
# create an instance of NimbleDemoteVolumeCollectionsInput from a dict
nimble_demote_volume_collections_input_from_dict = NimbleDemoteVolumeCollectionsInput.from_dict(nimble_demote_volume_collections_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


