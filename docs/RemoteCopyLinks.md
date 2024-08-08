# RemoteCopyLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[RemoteCopyLink]**](RemoteCopyLink.md) |  | [optional] 
**total** | **int** | Total number of remote partner links. | [optional] 

## Example

```python
from dscc.models.remote_copy_links import RemoteCopyLinks

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteCopyLinks from a JSON string
remote_copy_links_instance = RemoteCopyLinks.from_json(json)
# print the JSON string representation of the object
print(RemoteCopyLinks.to_json())

# convert the object into a dict
remote_copy_links_dict = remote_copy_links_instance.to_dict()
# create an instance of RemoteCopyLinks from a dict
remote_copy_links_from_dict = RemoteCopyLinks.from_dict(remote_copy_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


