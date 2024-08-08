# NimbleFolderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleFolderListItemsInner]**](NimbleFolderListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for folder objects | [optional] 
**total** | **int** | Total number of folders. | [optional] 

## Example

```python
from dscc.models.nimble_folder_list import NimbleFolderList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFolderList from a JSON string
nimble_folder_list_instance = NimbleFolderList.from_json(json)
# print the JSON string representation of the object
print(NimbleFolderList.to_json())

# convert the object into a dict
nimble_folder_list_dict = nimble_folder_list_instance.to_dict()
# create an instance of NimbleFolderList from a dict
nimble_folder_list_from_dict = NimbleFolderList.from_dict(nimble_folder_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


