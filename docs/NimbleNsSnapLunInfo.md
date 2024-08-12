# NimbleNsSnapLunInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Snapshot ID. | [optional] 
**lun** | **int** | Snapshot LUN. | [optional] 
**name** | **str** | Snapshot name. | [optional] 

## Example

```python
from dscc.models.nimble_ns_snap_lun_info import NimbleNsSnapLunInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNsSnapLunInfo from a JSON string
nimble_ns_snap_lun_info_instance = NimbleNsSnapLunInfo.from_json(json)
# print the JSON string representation of the object
print(NimbleNsSnapLunInfo.to_json())

# convert the object into a dict
nimble_ns_snap_lun_info_dict = nimble_ns_snap_lun_info_instance.to_dict()
# create an instance of NimbleNsSnapLunInfo from a dict
nimble_ns_snap_lun_info_from_dict = NimbleNsSnapLunInfo.from_dict(nimble_ns_snap_lun_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


