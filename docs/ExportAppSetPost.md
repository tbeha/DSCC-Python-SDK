# ExportAppSetPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_group_ids** | **List[Optional[str]]** | HostGroups | 
**proximity** | **str** | Host proximity setting for Active Peer Persistence configuration. Supported values are - PRIMARY, SECONDARY and ALL. Default proximity is PRIMARY. | [optional] 

## Example

```python
from dscc.models.export_app_set_post import ExportAppSetPost

# TODO update the JSON string below
json = "{}"
# create an instance of ExportAppSetPost from a JSON string
export_app_set_post_instance = ExportAppSetPost.from_json(json)
# print the JSON string representation of the object
print(ExportAppSetPost.to_json())

# convert the object into a dict
export_app_set_post_dict = export_app_set_post_instance.to_dict()
# create an instance of ExportAppSetPost from a dict
export_app_set_post_from_dict = ExportAppSetPost.from_dict(export_app_set_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


