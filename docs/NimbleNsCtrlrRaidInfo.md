# NimbleNsCtrlrRaidInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cur_copies** | **int** | Current number of copies. | [optional] 
**is_resyncing** | **bool** | Is this raid array resynchronizing. | [optional] 
**max_copies** | **int** | Maximum number of copies. | [optional] 
**raid_id** | **int** | Raid ID for this raid array. | [optional] 
**raid_type** | **str** | Type of raid for this array. | [optional] 

## Example

```python
from dscc.models.nimble_ns_ctrlr_raid_info import NimbleNsCtrlrRaidInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNsCtrlrRaidInfo from a JSON string
nimble_ns_ctrlr_raid_info_instance = NimbleNsCtrlrRaidInfo.from_json(json)
# print the JSON string representation of the object
print(NimbleNsCtrlrRaidInfo.to_json())

# convert the object into a dict
nimble_ns_ctrlr_raid_info_dict = nimble_ns_ctrlr_raid_info_instance.to_dict()
# create an instance of NimbleNsCtrlrRaidInfo from a dict
nimble_ns_ctrlr_raid_info_from_dict = NimbleNsCtrlrRaidInfo.from_dict(nimble_ns_ctrlr_raid_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


