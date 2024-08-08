# ResourceDetail

System and Resource Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | [optional] 
**resource_uid** | **str** |  | [optional] 
**resource_uri** | **str** |  | [optional] 

## Example

```python
from dscc.models.resource_detail import ResourceDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceDetail from a JSON string
resource_detail_instance = ResourceDetail.from_json(json)
# print the JSON string representation of the object
print(ResourceDetail.to_json())

# convert the object into a dict
resource_detail_dict = resource_detail_instance.to_dict()
# create an instance of ResourceDetail from a dict
resource_detail_from_dict = ResourceDetail.from_dict(resource_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


