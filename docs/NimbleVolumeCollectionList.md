# NimbleVolumeCollectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleVolumeCollectionListItemsInner]**](NimbleVolumeCollectionListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for volumeCollection objects | [optional] 
**total** | **int** | Total number of Volume Collections. | [optional] 

## Example

```python
from dscc.models.nimble_volume_collection_list import NimbleVolumeCollectionList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleVolumeCollectionList from a JSON string
nimble_volume_collection_list_instance = NimbleVolumeCollectionList.from_json(json)
# print the JSON string representation of the object
print(NimbleVolumeCollectionList.to_json())

# convert the object into a dict
nimble_volume_collection_list_dict = nimble_volume_collection_list_instance.to_dict()
# create an instance of NimbleVolumeCollectionList from a dict
nimble_volume_collection_list_from_dict = NimbleVolumeCollectionList.from_dict(nimble_volume_collection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


