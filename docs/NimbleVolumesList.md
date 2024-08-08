# NimbleVolumesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleVolume]**](NimbleVolume.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for volume objects | [optional] 
**total** | **int** | Total number of volumes. | [optional] 

## Example

```python
from dscc.models.nimble_volumes_list import NimbleVolumesList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleVolumesList from a JSON string
nimble_volumes_list_instance = NimbleVolumesList.from_json(json)
# print the JSON string representation of the object
print(NimbleVolumesList.to_json())

# convert the object into a dict
nimble_volumes_list_dict = nimble_volumes_list_instance.to_dict()
# create an instance of NimbleVolumesList from a dict
nimble_volumes_list_from_dict = NimbleVolumesList.from_dict(nimble_volumes_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


