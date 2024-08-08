# AppsetPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment if any | [optional] 
**expire_secs** | **int** | Expiration time in seconds | [optional] 
**read_only** | **bool** | Read only or Read/Write | [optional] 
**retain_secs** | **int** | Reatain time in seconds | [optional] 
**snapshot_name** | **str** | Name for snapshot | 
**vv_name_pattern** | [**VvNamePattern**](VvNamePattern.md) |  | 

## Example

```python
from dscc.models.appset_post import AppsetPost

# TODO update the JSON string below
json = "{}"
# create an instance of AppsetPost from a JSON string
appset_post_instance = AppsetPost.from_json(json)
# print the JSON string representation of the object
print(AppsetPost.to_json())

# convert the object into a dict
appset_post_dict = appset_post_instance.to_dict()
# create an instance of AppsetPost from a dict
appset_post_from_dict = AppsetPost.from_dict(appset_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


